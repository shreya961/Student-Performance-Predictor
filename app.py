import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from utils import get_performance_category, generate_suggestions

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("STUDENT PERFORMANCE PREDICTOR")

# -------- INPUTS --------
study_hours = st.slider("Enter your Study Hours", 1, 24, 1)
sleep_hours = st.slider("Enter your Sleep Hours", 1, 24, 1)
attendance = st.number_input("Enter your class attendance (%)", 0, 100, 0)
previous_score = st.number_input("Enter your Previous Score", 0, 100, 0)
assignments = st.selectbox("Assignments you have finished", list(range(0, 10)))

target = st.number_input("Enter your target score", 10, 100, 10)

# -------- BUTTON: PREDICT --------
if st.button(" Predict Score"):
    input_data = np.array([[study_hours, attendance, previous_score, sleep_hours, assignments]])
    prediction = model.predict(input_data)[0]

    # store prediction
    st.session_state["prediction"] = prediction

# -------- SHOW RESULTS (persistent) --------
if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]

    st.subheader(f"PREDICTED SCORE: {round(prediction, 2)}")

    # CATEGORY
    category = get_performance_category(prediction)
    st.subheader(f"PERFORMANCE: {category}")

    

    # -------- PIE CHART --------
    st.subheader(" Contribution of Factors")

    importances = model.feature_importances_
    labels = [
        "Study Hours",
        "Attendance",
        "Previous Score",
        "Sleep Hours",
        "Assignments"
    ]

    plt.figure()
    plt.pie(importances, labels=labels, autopct="%1.1f%%")
    st.pyplot(plt)

    st.info("Higher percentage means greater impact on your score")

    # -------- SUGGESTIONS --------
    st.subheader("Suggestions")
    suggestions = generate_suggestions(study_hours, attendance, sleep_hours, previous_score, assignments)

    if suggestions:
        for s in suggestions:
            st.warning(s)
    else:
        st.success("Excellent! Keep it up ")

    # -------- OPTIONAL GRAPH --------
    if st.checkbox("Show Study Hours Analysis"):
        st.subheader("Impact of Study Hours on Score")

        hours = list(range(1, 11))
        scores = [
            model.predict([[h, attendance, previous_score, sleep_hours, assignments]])[0]
            for h in hours
        ]

        plt.figure()
        plt.plot(hours, scores)
        plt.xlabel("Study Hours")
        plt.ylabel("Predicted Score")
        st.pyplot(plt)

# -------- GOAL FEATURE --------
if st.button(" Required Study Hours"):

    found = False

    for h in range(1, 13):
        pred = model.predict([[h, attendance, previous_score, sleep_hours, assignments]])[0]

        if pred >= target:
            st.success(f"You need approx {h} study hours to reach your goal 🎯")
            found = True
            break

    if not found:
        st.warning("Even with maximum study hours, target may not be achievable 😢")