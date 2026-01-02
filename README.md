**Diabetic Patient Readmission Prediction AP**

**## Overview**
A machine learning project to predict hospital readmission of diabetic patients using historical medical data. This project demonstrates data preprocessing, XGBoost modeling, Flask API deployment, and Docker containerization for real-time predictions.


Data Preprocessing: Safe handling of categorical variables.
Model: XGBoost for accurate predictions.
API: RESTful Flask API for real-time predictions.
Containerization: Dockerized for easy deployment.
Cloud Deployment: Live on Google Cloud Run, accessible globally.

**## Features**
Key patient and hospitalization features used:

- Demographics: `age`, `gender`, `race`
- Hospitalization: `time_in_hospital`, `admission_type_id`, `discharge_disposition_id`
- Lab & medication data: `num_lab_procedures`, `num_medications`, `insulin`, etc.
- Target: `readmitted` (`<30`, `>30`, `NO`)

**## Local Setup**
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>

Create environment and install dependencies:
conda create -n readmission python=3.11
conda activate readmission

**Install dependencies:
pip install -r requirement.txt

Run Flask API:
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
docker build -t xgb-flask-api .

Run container:
docker run -p 8000:8000 xgb-flask-api

Cloud Deployment
gcloud run deploy xgb-flask-api \
    --image gcr.io/diabetic-readmission-api/xgb-flask-api \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated

Live API
The API is live and can be accessed at:
https://xgb-flask-api-344385015348.us-central1.run.app

Notes
Handles unseen categorical values safely during prediction.
Suitable for production-ready demonstration of ML model serving.
