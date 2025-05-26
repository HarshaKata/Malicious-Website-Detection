from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from feature_extractor import URLFeatureExtractor  # make sure it's in same folder
import traceback

app = Flask(__name__)
CORS(app)

model = joblib.load("url_classifier_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        url = data.get("url")
        extractor = URLFeatureExtractor()
        features = extractor.extract(url)
        feature_df = pd.DataFrame([features])

        # Fill missing columns
        for col in model.feature_names_in_:
            if col not in feature_df.columns:
                feature_df[col] = 0

        prediction = model.predict(feature_df)[0]
        probability = model.predict_proba(feature_df)[0]

        result = {
            "url": url,
            "prediction": "Legitimate" if prediction == 1 else "Phishing",
            "probability": {
                "phishing": float(probability[0]),
                "legitimate": float(probability[1])
            }
        }

        if not extractor.http_accessible:
            result["warnings"] = "Warning: The page couldn't be accessed. Prediction is based only on URL-based features."

        return jsonify(result)
    
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
