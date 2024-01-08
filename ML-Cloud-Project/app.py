from flask import Flask, request
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return {'prediction': prediction[0]}
