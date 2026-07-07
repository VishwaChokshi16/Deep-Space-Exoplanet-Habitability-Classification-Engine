import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

class SpaceModelTrainer:
    def __init__(self):
        self.artifacts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
        os.makedirs(self.artifacts_dir, exist_ok=True)
        self.model_path = os.path.join(self.artifacts_dir, "exoplanet_classifier.joblib")

    def train_and_export_model(self, X_train, y_train, preprocessor):
        full_pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42))
        ])
        full_pipeline.fit(X_train, y_train)
        joblib.dump(full_pipeline, self.model_path)
        return full_pipeline