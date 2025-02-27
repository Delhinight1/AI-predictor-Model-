import streamlit as st  # Import Streamlit
from joblib import load  # Import joblib
from numpy import array  # Import numpy
# Load the trained model
model = load("model.pkl")

# Customizing the page layout
st.set_page_config(page_title="Placement Package Predictor", page_icon="🎓", layout="centered")

# Styling
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        .main {
            @apply bg-gray-100 p-5 rounded-lg shadow-md;
        }
        .stTextInput, .stNumberInput, .stButton > button {
            @apply text-lg;
        }
        .stNumberInput input {
            @apply p-2 rounded-md;
        }
        .stButton > button {
            @apply bg-green-500 text-white rounded-md py-2 px-4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 Placement Package Predictor</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Enter your CGPA to predict the expected placement package.</p>", 
    unsafe_allow_html=True
)

# Input field
gpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")

# Predict button
if st.button("Predict Package 💰"):
    input_features = array([[gpa]])
    prediction = model.predict(input_features)[0]
    
    st.markdown(
        f"""<div style='background-color: #DFF0D8; padding: 15px; border-radius: 5px; text-align: center;'>
        <h3 style='color: black'>Predicted Package: <span style='color: #4CAF50;'>{prediction:.2f} LPA</span></h3>
        </div>""",
        unsafe_allow_html=True
    )