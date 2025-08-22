import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("titanic2.pkl", "rb"))

st.title("🚢 Titanic Survival Predictor Dashboard")

st.write("Enter passenger details to predict survival:")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
fare = st.number_input("Fare (Ticket Price)", min_value=0.0, value=50.0)

# Convert categorical values
sex = 1 if sex == "male" else 0   # Assuming model expects male=1, female=0

# Create input array
features = np.array([[pclass, sex, age, fare]])

# Prediction button
if st.button("Predict Survival"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ The passenger would have SURVIVED!")
    else:
        st.error("❌ The passenger would NOT have survived.")
