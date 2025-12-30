# Hospital Readmission Prediction for Diabetic Patients

## Overview
A machine learning project to predict hospital readmission of diabetic patients using historical medical data. The project includes:

- Data preprocessing with safe handling of categorical variables.
- XGBoost model for prediction.
- RESTful Flask API for real-time predictions.
- Docker containerization for easy deployment.

## Features
Key patient and hospitalization features used:

- Demographics: `age`, `gender`, `race`
- Hospitalization: `time_in_hospital`, `admission_type_id`, `discharge_disposition_id`
- Lab & medication data: `num_lab_procedures`, `num_medications`, `insulin`, etc.
- Target: `readmitted` (`<30`, `>30`, `NO`)

## Local Setup
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>
Create environment and install dependencies:

bash
Copy code
conda create -n readmission python=3.11
conda activate readmission
pip install -r requirement.txt
Run Flask API:

bash
Copy code
python app.py
Access at: http://127.0.0.1:8000

API Usage
POST /predict
Request JSON:

json
Copy code
{
    "age": 70,
    "gender": "Male",
    "num_medications": 5,
    "time_in_hospital": 3,
    "race": "Caucasian"
    // add other required features
}
Response JSON:

json
Copy code
{
    "prediction": ">30"
}
Docker Deployment
Build Docker image:

bash
Copy code
docker build -t xgb-flask-api .
Run container:

bash
Copy code
docker run -p 8000:8000 xgb-flask-api

Notes
Handles unseen categorical values safely during prediction.
Can be deployed to cloud platforms: AWS, GCP Cloud Run, Heroku.
Handles unseen categorical values safely during prediction.

Can be deployed to cloud platforms: AWS, GCP Cloud Run, Heroku.
