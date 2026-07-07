from flask import Flask, render_template, request, jsonify
from src.predictor import ExoplanetPredictor

app = Flask(__name__)

# Initialize the predictor engine global client
try:
    predictor = ExoplanetPredictor()
except Exception:
    predictor = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if predictor is None:
        return jsonify({"error": "Model has not been trained yet. Run train.py first."}), 500
    
    try:
        data = request.json
        # Extract inputs and explicitly parse to float matrices
        metrics = {
            "Distance_from_Star_AU": float(data["distance"]),
            "Planet_Mass_Earths": float(data["mass"]),
            "Stellar_Luminosity_Suns": float(data["luminosity"]),
            "Atmospheric_Greenhouse_Factor": float(data["greenhouse"])
        }
        
        result = predictor.evaluate_new_planet(metrics)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)