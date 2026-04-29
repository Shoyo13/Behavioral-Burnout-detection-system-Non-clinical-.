# 🧠 AI-Powered Behavioral Burnout Detection System

An intelligent system that predicts burnout risk using behavioral data and provides actionable insights, simulations, and optimization strategies.

---

## 🚀 Features

- 🔍 **Burnout Risk Prediction**
  - Uses Machine Learning (Isolation Forest)
  - Hybrid scoring with rule-based logic

- 📊 **Interactive Dashboard**
  - Built with Streamlit
  - Real-time user input sliders

- 📈 **Trend Analysis**
  - Tracks burnout history over time
  - Visualized using Plotly charts

- 🧪 **What-If Simulation**
  - Test different behavioral scenarios
  - See how risk changes dynamically

- 🧠 **Smart Coach (Optimization Engine)**
  - Suggests improved behavior
  - Predicts reduced burnout risk

- 💾 **History Tracking**
  - Stores user data in SQLite
  - Allows trend monitoring

---

## 🏗️ Tech Stack

| Layer        | Technology        |
|-------------|------------------|
| Frontend    | Streamlit        |
| Backend     | FastAPI          |
| ML Model    | Scikit-learn     |
| Database    | SQLite           |
| Visualization | Plotly         |
| Language    | Python           |

---

## 📂 Project Structure
burnout-detection-system/
│
├── dataset/
│ └── behavioral_data.csv
│
├── ml-engine/
│ ├── api.py
│ ├── model.py
│ ├── dashboard.py
│ ├── database.py
│ ├── config.py
│ └── requirements.txt
│
└── README.md


---

## ⚙️ How to Run the Project

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/burnout-detection-system.git
cd burnout-detection-system

🔹 2. Install Dependencies
pip install -r ml-engine/requirements.txt
🔹 3. Run Backend (FastAPI)
cd ml-engine
uvicorn api:app --reload
🔹 4. Run Frontend (Streamlit)
streamlit run dashboard.py

📊 Sample Inputs
Work Hours
Overtime Days
Emails Sent
Meetings Count
Tasks Completed
Days Since Vacation

🎯 Output
Burnout Risk Percentage
Risk Level (Low / Moderate / High)
Smart Suggestions
Optimized Plan
Simulation Results
Historical Trends

🧠 Model Details
Algorithm: Isolation Forest
Detects anomalies in behavioral patterns
Combined with rule-based scoring for better accuracy

📈 Risk Levels
Range	Level
0–40	Low
40–70	Moderate
70–100	High

⚠️ Limitations
Uses structured synthetic dataset
Not trained on real-world medical data
Basic anomaly detection model

🔮 Future Enhancements
Integration with real datasets (Kaggle / enterprise)
Advanced ML models (Random Forest, XGBoost)
Mobile application
Real-time monitoring system
Java Spring Boot backend
HR dashboard integration

🎓 Academic Context
This project was developed as part of the B.Tech Computer Science & Engineering curriculum.

## 👤 Author

**Shoyab Ali**  
B.Tech Computer Science & Engineering  
University of Petroleum & Energy Studies  

Passionate about building AI-driven systems and intelligent dashboards.  
This project demonstrates full-stack ML integration with real-time analytics, simulation, and decision support.

GitHub: https://github.com/Shoyo13


⭐ If you found this useful

Give it a ⭐ on GitHub!


---

# 🚀 FINAL STEP

After pasting:

👉 Save file  
👉 Go to Source Control  
👉 Commit:

```text
Updated professional README

👉 Click Sync Changes