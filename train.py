from src.data_pipeline import generate_astronomical_data, build_space_pipeline
from src.model_trainer import SpaceModelTrainer
from sklearn.model_selection import train_test_split

def execute_training():
    print("[SYSTEM] Fetching data and training model...")
    df = generate_astronomical_data()
    X = df.drop("Habitability_Target", axis=1)
    y = df["Habitability_Target"]
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    
    preprocessor = build_space_pipeline()
    trainer = SpaceModelTrainer()
    trainer.train_and_export_model(X_train, y_train, preprocessor)
    print("[SUCCESS] Training complete. artifacts/exoplanet_classifier.joblib created.")

if __name__ == "__main__":
    execute_training()