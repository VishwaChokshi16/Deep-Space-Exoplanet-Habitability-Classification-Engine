import os
import joblib
import pandas as pd

class ExoplanetPredictor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(base_dir, "artifacts", "exoplanet_classifier.joblib")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError("Model file missing. Run train.py first.")
        self.pipeline = joblib.load(self.model_path)

    def evaluate_new_planet(self, metrics_dict):
        df_input = pd.DataFrame([metrics_dict])
        prediction = self.pipeline.predict(df_input)[0]
        probabilities = self.pipeline.predict_proba(df_input)[0]
        
        return {
            "class": int(prediction),
            "status": "HIGH-PRIORITY HABITABLE CANDIDATE" if prediction == 1 else "Barren / Hostile Planet",
            "probability": float(probabilities[1] * 100)
        }