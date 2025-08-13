# Mental Health Prediction

**Mental Health Prediction** is a machine learning project that uses a Logistic Regression model to predict whether a person is experiencing depression based on lifestyle, behavioral, and psychological factors.

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/husni-haniffa/mental-health-prediction-backend
   ```

2. **Navigate to the project directory**
   ```bash
   cd mental-health-prediction-backend
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. **Configure the model path**
   
   Update the model path in your configuration file according to your system. For example:
   ```
   ./best_lr_model.pkl
   ```
   
**Note:** The model file is included in the cloned repository. You can either use this path directly or place the model file in any other folder on your system and update the configuration file accordingly.

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

8. **Backend server will be available at:**
   
   Visit: [http://localhost:8000](http://localhost:8000)

### Frontend Setup

To complete the full application setup, you'll also need to configure the frontend:

**Frontend Repository:** [mental-health-prediction-frontend](https://github.com/husni-haniffa/mental-health-prediction-frontend)

Please follow the setup instructions in the backend repository to get the complete system running.
