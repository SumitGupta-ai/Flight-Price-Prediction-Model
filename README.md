✈️ Flight Price Prediction Web App
📌 Project Description

Flight Price Prediction Web Application ek end-to-end Machine Learning + Flask based project hai jo user ke input ke basis par flight ticket price predict karta hai.

Ye project ML + Web dono ko combine karta hai aur real-world deployment ready hai.

🚀 Project Overview

Machine Learning model trained & saved

Flask backend

HTML/CSS frontend

User-friendly form

Deployment ready structure

🧠 Machine Learning Details

Model Used: XGBoost Regressor

Preprocessing Techniques:

OneHotEncoder (categorical features)

OrdinalEncoder

StandardScaler

Model File: Flight_Price_Prediction.pkl

Libraries: scikit-learn, xgboost, pandas, numpy

🖥️ Web Application Features

Clean & professional UI

Same source & destination city not allowed

Stops handled properly:

zero

one

two_more

Duration format supported: 2.25

Instant price prediction

📂 Project Structure
Flight Price Prediction/
│
├── app.py
├── Flight_Price_Prediction.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── notebooks/
    └── model_training.ipynb

⚙️ Installation & Setup (Local)
1️⃣ Clone Repository
git clone https://github.com/SumitGupta-ai/Flight-Price-Prediction-Model.git
cd Flight-Price-Prediction-Model

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask App
python app.py

5️⃣ Open Browser
http://127.0.0.1:5000/

🌐 Deployment

Ye project Render / Railway / AWS pe deploy ho sakta hai.

Gunicorn command:

gunicorn app:app

🛠️ Technologies Used

Python

Flask

HTML / CSS

Scikit-learn

XGBoost

Pandas

NumPy

Joblib

Gunicorn

📊 Input Features

Airline

Source City

Destination City

Departure Time

Arrival Time

Stops

Class

Duration

Days Left

📌 Future Improvements

Authentication system

Better UI (Bootstrap / React)

Live flight data API

Model optimization

Docker support

👨‍💻 Author

Sumit Gupta
GitHub: https://github.com/SumitGupta-ai


