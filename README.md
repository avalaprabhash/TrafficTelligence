# TrafficTelligence
# 🚦 TrafficTelligence

A machine learning-powered Flask web application that predicts real-time traffic volume based on weather and time-based parameters. Built to help urban planners, developers, and curious minds estimate traffic flow with intelligent, data-driven insights.

---

## 🌐 Live Demo

Coming soon at: [https://avalaprabhash.github.io/TrafficTelligence](https://avalaprabhash.github.io/TrafficTelligence)

---

## 📊 Features

- Predicts traffic volume based on inputs like temperature, rain, snow, weather, holidays, and time
- Trained using a Random Forest Regressor for robust performance
- Clean HTML form interface and optional routing to traffic condition pages
- Modular Flask app architecture
- Preprocessing tools and model artifacts stored with pickle

---

## 🧠 Machine Learning Workflow

- Cleaned and preprocessed historical traffic volume dataset
- Handled missing values via imputation
- Encoded categorical features (`holiday`, `weather`) using LabelEncoder
- Applied StandardScaler for feature normalization
- Trained and evaluated multiple models
- Saved the best-performing model (`RandomForestRegressor`) and preprocessing tools

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Jinja2 Templates
- **Backend**: Python, Flask
- **ML**: scikit-learn, XGBoost, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn (for EDA)
- **Deployment**: GitHub Pages (planned), Localhost

---

## 📁 Directory Structure

TrafficTelligence/ │ ├── app.py ├── scale.pkl ├── encoder.pkl ├── imputer.pkl ├── model.pkl ├── requirements.txt ├── traffic volume.csv ├── traffic volume.ipynb └── templates/ ├── index.html ├── result.html ├── chance.html └── noChance.html


---


## ▶️ Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

python app.py

🚀 Roadmap
[ ] Add prediction-based redirection to chance/noChance pages

[ ] Integrate live weather API

[ ] Deploy with custom domain: traffiq.ai

[ ] Add charts and historical comparisons in UI

🙋‍♂️ Author
PRABHAS Avala 🧠 Passionate about machine learning, web development, and building things that work.
