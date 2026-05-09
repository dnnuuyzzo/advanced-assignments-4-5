import streamlit as st
import pandas as pd
import joblib

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('model.joblib')

model = load_model()

# Title and description
st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

# Display logo if it exists
try:
    st.image("assets/logo.png", width=150)
except:
    pass

st.title("🚢 Titanic Survival Predictor")
st.markdown("""
This app predicts whether a passenger would have survived the Titanic disaster based on their details.
""")

# Sidebar for inputs
st.sidebar.header("Passenger Details")

def user_input_features():
    pclass = st.sidebar.selectbox("Ticket Class (Pclass)", (1, 2, 3), help="1 = 1st, 2 = 2nd, 3 = 3rd")
    sex = st.sidebar.selectbox("Sex", ("male", "female"))
    embarked = st.sidebar.selectbox("Port of Embarkation", ("S", "C", "Q"), help="S = Southampton, C = Cherbourg, Q = Queenstown")
    sibsp = st.sidebar.slider("Number of Siblings/Spouses Aboard (SibSp)", 0, 8, 0)
    parch = st.sidebar.slider("Number of Parents/Children Aboard (Parch)", 0, 6, 0)
    fare = st.sidebar.number_input("Passenger Fare", min_value=0.0, value=32.0, step=0.1)
    
    data = {
        'Pclass': pclass,
        'Sex': sex,
        'Embarked': embarked,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare
    }
    features = pd.DataFrame(data, index=[0])
    return features

df_input = user_input_features()

# Display inputs
st.subheader("Passenger Information Summary")
st.write(df_input)

# Prediction
if st.button("Predict Survival"):
    prediction = model.predict(df_input)
    prediction_proba = model.predict_proba(df_input)
    
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.success("✅ This passenger would likely have **SURVIVED**.")
    else:
        st.error("❌ This passenger would likely **NOT HAVE SURVIVED**.")
        
    st.subheader("Prediction Probability")
    st.write(f"Survival Probability: {prediction_proba[0][1]:.2%}")
    st.write(f"Fatality Probability: {prediction_proba[0][0]:.2%}")

# Footer
st.markdown("---")
st.markdown("Created for Weekly Class GDGoC Assignments.")
