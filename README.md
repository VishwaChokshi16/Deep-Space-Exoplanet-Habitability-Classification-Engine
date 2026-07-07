# 🌌 Deep-Space Exoplanet Habitability Analytics Engine

An end-to-end Machine Learning web application that utilizes an ensemble Random Forest Classifier to process planetary telescope readings and predict habitability candidate status. Features an API-driven architecture powered by Flask, providing a clean, dynamic frontend UI.

## 🚀 Key Features
* **Full Data & Transformation Pipelines:** Handles corrupted telescope inputs dynamically by utilizing Scikit-Learn's `SimpleImputer` and `StandardScaler` tracking.
* **Ensemble Learning Engine:** Employs a `Random Forest Classifier` optimized with balanced class weight adjustments to accurately isolate rare habitable candidates (~6% frequency).
* **API-Driven Architecture:** Exposes machine learning predictions via an asynchronous Flask server interacting natively with raw user frontend payloads.
* **Dynamic Frontend Visualizations:** Animates data distributions and model certainty indices using custom CSS progress meters based on API telemetry inputs.

## 📂 Project Architecture
```
space-ml-engine/
│
├── artifacts/             # Serialized model binaries (Hidden via .gitignore)
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py   # Data simulation & scaling pipelines
│   ├── model_trainer.py   # Ensemble model training configurations
│   └── predictor.py       # Production runtime inference gateway
│
├── templates/
│   └── index.html         # Frontend interface layout
│
├── static/
│   ├── style.css          # Frontend visual styling
│   └── app.js             # API transmission handler
│
├── requirements.txt       # Unified package list
├── app.py                 # Flask app server bridge
└── train.py               # Model generation script ```

## **Made By**
Vishwa Chokshi
