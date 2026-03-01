from flask import Flask, request, jsonify
from utils.predictor import predict_job
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TrustHire API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    result = predict_job(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)