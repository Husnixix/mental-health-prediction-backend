from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Union
import pandas as pd
import numpy as np
import pickle
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "C:/Users/HP/Models/Mental Health Prediction Model/best_lr_model.pkl"

try:
    if os.path.exists(model_path):
        model = pickle.load(open(model_path, "rb"))
        print("Model loaded successfully")
    else:
        print(f"Model file not found at {model_path}")
        model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

COLUMN_ORDER = [
    'Gender', 'Age', 'Academic Pressure', 'Study Satisfaction',
    'Sleep Duration', 'Dietary Habits',
    'Have you ever had suicidal thoughts ?', 'Study Hours',
    'Financial Stress', 'Family History of Mental Illness'
]

class AssessmentInput(BaseModel):
    values: Dict[str, Union[int, float]]

@app.post("/predict")
async def get_prediction(data: AssessmentInput):

    if model is None:
        return {"error": "Model not loaded. Please check the model file path."}

    missing_fields = [field for field in COLUMN_ORDER if field not in data.values]
    if missing_fields:
        return {"error": f"Missing required fields: {missing_fields}"}

    try:
        ordered_values = [data.values[col] for col in COLUMN_ORDER]

        input_df = pd.DataFrame([ordered_values], columns=COLUMN_ORDER)
        input_df = input_df.astype(float)

        print(f"Input data: {input_df.to_dict('records')[0]}")

    except Exception as e:
        return {"error": f"Data conversion error: {str(e)}"}

    try:
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]

        depression = "Yes" if prediction == 1 else "No"
        confidence = probabilities[int(prediction)] * 100

        print(f"Prediction: {prediction}, Confidence: {confidence:.2f}%")

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

    return {
        "is_depressed": depression,
        "confidence_score": round(confidence, 2)
    }


@app.get("/")
async def root():
    return {"message": "Mental Health Assessment API is running"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)