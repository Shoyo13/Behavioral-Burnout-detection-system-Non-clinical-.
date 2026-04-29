import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from config import API_URL
st.set_page_config(page_title="Burnout AI", layout="wide")
# =========================
# 🎨 UI STYLE
# =========================
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.stSlider > div > div {
    background: linear-gradient(90deg, #00FF9C, #FFD166, #FF4D6D);
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI-Powered Burnout Detection System")

# =========================
# 🔐 LOGIN
# =========================
if "user" not in st.session_state:
    st.session_state.user = ""

if not st.session_state.user:
    u = st.text_input("Enter User ID")
    if st.button("Login"):
        st.session_state.user = u
        st.rerun()
    st.stop()

user_id = st.session_state.user
st.success(f"Logged in as: {user_id}")

# =========================
# 🎚 INPUTS
# =========================
col1, col2 = st.columns(2)

with col1:
    work = st.slider("Work Hours", 5, 14, 8)
    overtime = st.slider("Overtime Days", 0, 7, 1)
    emails = st.slider("Emails Sent", 10, 120, 40)

with col2:
    meetings = st.slider("Meetings Count", 0, 15, 5)
    tasks = st.slider("Tasks Completed", 5, 20, 12)
    vacation = st.slider("Days Since Vacation", 0, 90, 20)

# =========================
# 🚀 ANALYZE
# =========================
if st.button("🚀 Analyze Burnout"):

    with st.spinner("🧠 AI analyzing your life choices..."):

        data = {
            "user_id": user_id,
            "work_hours_avg": work,
            "overtime_days": overtime,
            "emails_sent": emails,
            "meetings_count": meetings,
            "tasks_completed": tasks,
            "days_since_vacation": vacation
        }

        res = requests.post(f"{API_URL}/predict-burnout", json=data)
        result = res.json()

        # ✅ STORE RESULT (IMPORTANT FIX)
        st.session_state["result"] = result

# =========================
# 📊 DISPLAY RESULT
# =========================
if "result" in st.session_state:
    result = st.session_state["result"]
    risk_val = float(result["risk_percentage"].replace("%", ""))
    # 🎯 GAUGE
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_val,
        title={"text": "Burnout Risk %"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 40], "color": "green"},
                {"range": [40, 70], "color": "orange"},
                {"range": [70, 100], "color": "red"},
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)
    st.subheader(f"🔥 Risk Level: {result['risk_level']}")
    # 🧠 AI INSIGHT
    if risk_val > 70:
        vibe = "🔥 You're on the edge. Take a break NOW."
    elif risk_val > 40:
        vibe = "⚠️ You're managing… but not sustainably."
    else:
        vibe = "😎 You're chill. Keep it that way."
    st.info(vibe)
    # 💡 Suggestions
    st.subheader("💡 Smart Suggestions")
    for s in result["suggestions"]:
        st.write("✔", s)
        
    # =========================
    # 🧠 SMART COACH (LEGEND MODE)
    # =========================
    st.subheader("🧠 Smart Coach (Optimization Engine)")
    opt = result.get("optimized_plan", None)
    if opt:
        st.success("📉 Optimized Plan Generated")
        labels = ["Work Hours", "Overtime", "Emails", "Meetings", "Tasks", "Vacation"]
        for i in range(len(labels)):
            st.write(f"{labels[i]} → {opt[i]}")

        st.subheader("📊 Expected Outcome")
        st.info(f"Optimized Risk: {result['optimized_risk']}")
        
    # =========================
    # 📊 CONTRIBUTION GRAPH
    # =========================
    st.subheader("📊 Stress Contribution")
    labels = ["Work", "Overtime", "Emails", "Meetings", "Tasks", "Vacation"]
    values = [work, overtime, emails, meetings, tasks, vacation]
    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h'
    ))
    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 🧪 SIMULATION (FIXED)
    # =========================
    st.subheader("🧪 What-If Simulator")
    sim_work = st.slider("Simulated Work Hours", 5, 14, work)
    sim_overtime = st.slider("Simulated Overtime", 0, 7, overtime)
    if st.button("Run Simulation"):

        sim_data = {
            "user_id": user_id,
            "work_hours_avg": sim_work,
            "overtime_days": sim_overtime,
            "emails_sent": emails,
            "meetings_count": meetings,
            "tasks_completed": tasks,
            "days_since_vacation": vacation
        }
        res = requests.post(f"{API_URL}/predict-burnout", json=sim_data)
        sim_result = res.json()

        sim_risk = float(sim_result["risk_percentage"].replace("%", ""))

        st.subheader("🔮 Simulation Result")
        st.success(f"New Risk: {sim_result['risk_level']} ({sim_result['risk_percentage']})")

        # ✅ SAFE COMPARISON
        if sim_risk < risk_val:
            st.success("📉 Risk reduced! Good decision 👍")
        else:
            st.error("📈 Risk increased! Not a good move 🚨")

# =========================
# 📈 HISTORY (FINAL FIXED)
# =========================
st.subheader("📈 History")

if st.button("Load History"):

    try:
        res = requests.get(f"{API_URL}/history/{user_id}")
        data = res.json()["history"]

        if data:
            df = pd.DataFrame(data, columns=[
                "ID","User","Work","Overtime","Emails",
                "Meetings","Tasks","Vacation","Risk","Percent"
            ])

            df["Percent"] = df["Percent"].str.replace("%","").astype(float)

            st.dataframe(df)

            # ✅ GRAPH INSIDE BLOCK
            st.subheader("📈 Burnout Trend (Easy View)")

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=list(range(len(df))),
                y=df["Percent"],
                mode='lines+markers',
                name='Burnout Risk',
                line=dict(width=3)
            ))

            # 🎨 Zones
            fig.add_hline(y=40, line_dash="dash", line_color="green")
            fig.add_hline(y=70, line_dash="dash", line_color="red")

            fig.update_layout(
                xaxis_title="Time (Predictions)",
                yaxis_title="Burnout Risk (%)",
                title="Burnout Risk Over Time",
                template="plotly_dark"
            )

            st.plotly_chart(fig, use_container_width=True)

            # 🧠 Explanation
            st.markdown("""
🟢 Below 40% → Low Risk  
🟡 40–70% → Moderate Risk  
🔴 Above 70% → High Risk  
""")

        else:
            st.warning("No history found")

    except:
        st.error("⚠️ Backend not running or API error")