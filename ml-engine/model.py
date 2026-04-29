import os
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# =========================
# 📁 LOAD DATASET
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "dataset", "behavioral_data.csv")

df = pd.read_csv(file_path)

features = [
    "work_hours_avg",
    "overtime_days",
    "emails_sent",
    "meetings_count",
    "tasks_completed",
    "days_since_vacation"
]

X = df[features]

# =========================
# 🤖 MODEL
# =========================
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X)

# =========================
# 🔥 RULE SCORE
# =========================
def calculate_rule_score(data):
    score = 0
    if data[0] > 10: score += 20
    if data[1] > 3: score += 20
    if data[2] > 80: score += 10
    if data[3] > 8: score += 10
    if data[4] < 8: score += 10
    if data[5] > 40: score += 20
    return score


# =========================
# 🔮 BASE PREDICTION
# =========================
def predict_base(input_data):
    arr = np.array([input_data])

    anomaly_score = model.decision_function(arr)[0]
    ml_score = (1 - anomaly_score) * 50
    rule_score = calculate_rule_score(input_data)

    final_score = min(100, ml_score + rule_score)

    if final_score < 40:
        risk_level = "Low"
    elif final_score < 70:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return final_score, risk_level


# =========================
# 😈 SMART SUGGESTIONS
# =========================
def generate_suggestions(input_data):
    suggestions = []

    if input_data[0] > 10:
        suggestions.append("🚫 You're working too much — even robots take breaks 🤖")

    if input_data[1] > 3:
        suggestions.append("⏰ Overtime detected. Your bed misses you 🛏️")

    if input_data[2] > 80:
        suggestions.append("📩 Too many emails. Inbox ≠ life goals.")

    if input_data[3] > 8:
        suggestions.append("📅 Meetings overload. Could this be an email instead?")

    if input_data[4] < 8:
        suggestions.append("📉 Productivity low. Try working smarter, not longer.")

    if input_data[5] > 40:
        suggestions.append("🌴 It's been too long... go touch some grass 🌿")

    if not suggestions:
        suggestions.append("😌 You're doing great. Keep the balance!")

    return suggestions


# =========================
# 🧠 LEGEND MODE (SMART COACH)
# =========================
def generate_optimized_plan(input_data):
    optimized = input_data.copy()

    if optimized[0] > 8:
        optimized[0] = 7.5
    if optimized[1] > 2:
        optimized[1] = 1
    if optimized[2] > 60:
        optimized[2] = 40
    if optimized[3] > 6:
        optimized[3] = 4
    if optimized[4] < 10:
        optimized[4] = 12
    if optimized[5] > 30:
        optimized[5] = 10

    return optimized


# =========================
# 🚀 FINAL FUNCTION
# =========================
def predict_burnout(input_data):

    # Base prediction
    score, level = predict_base(input_data)

    # Suggestions
    suggestions = generate_suggestions(input_data)

    # Optimized plan
    optimized_input = generate_optimized_plan(input_data)
    opt_score, opt_level = predict_base(optimized_input)

    return {
        "risk_percentage": f"{round(score, 2)}%",
        "risk_level": level,
        "burnout_signal": "Detected" if level != "Low" else "Normal",
        "suggestions": suggestions,
        "optimized_plan": optimized_input,
        "optimized_risk": f"{round(opt_score, 2)}%"
    }