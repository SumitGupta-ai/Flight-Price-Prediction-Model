# ✈️ Flight Price Prediction Web Application

---

## 📌 Project Overview

The **Flight Price Prediction Web Application** is an end-to-end Machine Learning project that predicts flight ticket prices based on user inputs such as **source city, destination city, number of stops, journey duration, airline, and travel date**.

The project integrates **Machine Learning**, **Flask backend**, and **HTML/CSS frontend**, and is **fully deployed on Render** for real-time usage.

---

## 🌐 Live Demo 

🔗 **Deployed Application:**
https://flight-price-prediction-model.onrender.com/

---

## 🧠 Machine Learning Model

* **Algorithm Used:** XGBoost Regressor
* **Problem Type:** Regression
* **Target Variable:** Flight Price
* **Training Platform:** Jupyter Notebook

### 🔹 Features Used

* Airline
* Source City
* Destination City
* Number of Stops (Non-stop, 1 stop, 2 stops, 2+ stops)
* Journey Duration (e.g. `2.25` hours format)
* Date of Journey

---

## 🛠️ Tech Stack

### 🔹 Programming & ML

* Python
* NumPy
* Pandas
* Scikit-learn
* XGBoost
* Joblib

### 🔹 Backend

* Flask
* Gunicorn

### 🔹 Frontend

* HTML5
* CSS3
* Bootstrap

### 🔹 Deployment

* Render (Cloud Platform)
* Git & GitHub

---

## 🎯 Key Features

* ✅ Real-time flight price prediction
* ✅ User-friendly web interface
* ✅ Input validation (same source & destination not allowed)
* ✅ Robust handling of categorical values
* ✅ Production-ready Flask application
* ✅ Deployed on cloud (Render)

---

## 📂 Project Structure

```
Flight-Price-Prediction-Model/
│
├── app.py
├── Flight-price-pred.ipynb
├── requirements.txt
├── README.md
│
├── model/
│   └── Flight_Price_Prediction.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── runtime.txt
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/Flight-Price-Prediction-Model.git
cd Flight-Price-Prediction-Model
```

### 2️⃣ Create virtual environment & activate

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Training

The model was trained in **Jupyter Notebook**, including:

* Data cleaning
* Feature engineering
* Handling categorical variables
* Model training & evaluation
* Model serialization using `joblib`

The trained model is stored as:

```
model/Flight_Price_Prediction.pkl
```

---

## ⚠️ Validation & Error Handling

* ❌ Same source and destination city not allowed
* ❌ Invalid stop selection handled safely
* ❌ Unseen categories prevented during prediction

---

## 📈 Future Improvements

* Add more airlines and routes
* Improve UI with JavaScript
* Add API endpoint support
* Dockerize application
* Deploy on AWS / GCP

---

## 👨‍💻 Author

**Sumit Gupta**
Machine Learning Enthusiast |

🔗 GitHub: https://github.com/SumitGupta-ai

---

## ⭐ Acknowledgements

* Kaggle (Dataset inspiration)
* Scikit-learn & XGBoost community
* Render platform for deployment

---

⭐ **If you like this project, give it a star!**



