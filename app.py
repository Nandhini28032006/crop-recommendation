<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import os

app = Flask(__name__)

# --- Load your trained model safely ---
model_path = os.path.join(os.path.dirname(__file__), "crop_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

# --- Home page route ---
@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    if request.method == "POST":
        try:
            data = request.form
            df = pd.DataFrame([{
                'N': float(data['N']),
                'P': float(data['P']),
                'K': float(data['K']),
                'temperature': float(data['temperature']),
                'humidity': float(data['humidity']),
                'ph': float(data['ph']),
                'rainfall': float(data['rainfall'])
            }])
            pred = model.predict(df)[0]
            prediction_text = f"🌾 Recommended Crop: {pred} 🌾"
        except Exception as e:
            prediction_text = f"⚠ Error: {e}"
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("crop_model.pkl", "rb"))

# Home page route
@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    if request.method == "POST":
        try:
            data = request.form
            df = pd.DataFrame([{
                'N': float(data['N']),
                'P': float(data['P']),
                'K': float(data['K']),
                'temperature': float(data['temperature']),
                'humidity': float(data['humidity']),
                'ph': float(data['ph']),
                'rainfall': float(data['rainfall'])
            }])
            pred = model.predict(df)[0]
            prediction_text = f"🌾 Recommended Crop: {pred} 🌾"
        except Exception as e:
            prediction_text = f"⚠ Error: {e}"
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)

>>>>>>> c09774f28c4f379649e66d8308bda3a60242800f
