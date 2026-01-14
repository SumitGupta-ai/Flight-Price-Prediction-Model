from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("Flight_Price_Prediction.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        source_city = request.form["source_city"]
        destination_city = request.form["destination_city"]

        if source_city == destination_city:
            error = "Source and Destination city cannot be same"
            return render_template("index.html", error=error)

        df = pd.DataFrame([{
            "airline": request.form["airline"],
            "source_city": source_city,
            "destination_city": destination_city,
            "departure_time": request.form["departure_time"],
            "arrival_time": request.form["arrival_time"],
            "stops": request.form["stops"],
            "class": request.form["class"],
            "duration": float(request.form["duration"]),
            "days_left": int(request.form["days_left"])
        }])

        prediction = round(model.predict(df)[0], 2)

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
