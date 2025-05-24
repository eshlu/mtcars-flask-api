# app/predict.py

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('linear_model.pkl')

# List of expected feature names in the correct order
FEATURES = ['cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.get_json()

        # Ensure all required features are provided
        if not all(feature in data for feature in FEATURES):
            return jsonify({
                "error": "Missing one or more required features.",
                "expected_features": FEATURES
            }), 400

        # Extract features in correct order and reshape for model input
        input_values = [data[feature] for feature in FEATURES]
        input_array = np.array(input_values).reshape(1, -1)

        # Make prediction
        predicted_mpg = model.predict(input_array)[0]

        # Return the result
        return jsonify({'predicted_mpg': round(predicted_mpg, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)