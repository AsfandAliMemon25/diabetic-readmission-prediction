# Diabetes Patient Readmission Prediction

![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2.2-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.5.3-green)
![Numpy](https://img.shields.io/badge/Numpy-1.23.5-red)

Welcome to the Diabetes Patient Readmission Prediction repository! This project is aimed at developing a machine-learning model to predict whether a diabetes patient is likely to be readmitted to the hospital within 30 days. Predicting readmission can help healthcare providers better allocate resources and improve patient care.

## Overview
## Table of Contents
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
-
- A machine learning project to predict hospital readmission of diabetic patients using historical medical data. This project demonstrates data preprocessing, XGBoost modeling, Flask API deployment, and Docker containerization for real-time predictions.

  ## Install dependencies
pip install -r requirement.txt

## Usage

Once you have installed the required dependencies, you can use the provided Jupyter notebooks to explore the project:

- `readmission-prediction.ipynb`: Explore and preprocess the dataset and Train and evaluate machine learning models for readmission prediction.
- `readmission-prediction-AutoML.ipynb`: Train and evaluate ML models using AutoML tools such as auto-sklearn and H2O. Make sure to run and generate cleaned data using the previous notebook.

You can run these notebooks step by step to understand and interact with the project.


Data Preprocessing: Safe handling of categorical variables.
Model: XGBoost for accurate predictions.
API: RESTful Flask API for real-time predictions.
Containerization: Dockerized for easy deployment.
Cloud Deployment: Live on Google Cloud Run, accessible globally.

## Features
Key patient and hospitalization features used:

- Demographics: `age`, `gender`, `race`
- Hospitalization: `time_in_hospital`, `admission_type_id`, `discharge_disposition_id`
- Lab & medication data: `num_lab_procedures`, `num_medications`, `insulin`, etc.
- Target: `readmitted` (`<30`, `>30`, `NO`)

## Local Setup
1. Clone the repository:

## Create environment and install dependencies:
conda create -n readmission python=3.11
conda activate readmission


## Local Setup
python app.py
Access at: http://127.0.0.1:8000

## API Usage
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

## Docker Deployment
Build Docker image:
docker build -t xgb-flask-api .

Run container:
docker run -p 8000:8000 xgb-flask-api

## Cloud Deployment
gcloud run deploy xgb-flask-api \
    --image gcr.io/diabetic-readmission-api/xgb-flask-api \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated

## Live API
The API is live and can be accessed at:
https://xgb-flask-api-344385015348.us-central1.run.app

## Notes
Handles unseen categorical values safely during prediction.
Suitable for production-ready demonstration of ML model serving.
