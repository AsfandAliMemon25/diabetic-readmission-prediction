# app.py
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load XGBoost model
with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load Label Encoder if needed
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Example feature columns in the same order as training
FEATURE_COLUMNS = [
    "age", "gender", "num_medications", "time_in_hospital"
    # Add all other features required by your model
]

@app.route("/")
def home():
    return "XGBoost Flask API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        # Convert input into DataFrame
        input_df = pd.DataFrame([data], columns=FEATURE_COLUMNS)
        
        # Encode categorical features
        if "gender" in input_df.columns:
            input_df["gender"] = le.transform(input_df["gender"])
        
        # Predict
        prediction = model.predict(input_df)[0]
        
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Bind to 0.0.0.0 so Docker can expose it
    app.run(debug=True, host="0.0.0.0", port=8000)
