import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Credit Scoring App",
    page_icon="💳",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ffffff, #e0e7ff);
}

/* Global Text */
html, body, [class*="css"] {
    color: #111827 !important;
}

/* Header Card */
.header-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.main-title {
    text-align: center;
    color: #6d28d9;
    font-size: 40px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #374151;
    font-size: 18px;
}

/* Labels */
label {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Number Inputs */
.stNumberInput input {
    color: #111827 !important;
    background-color: white !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    color: #111827 !important;
    background-color: white !important;
}

/* Button */
.stButton > button {
    background-color: #7c3aed;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    width: 100%;
    height: 55px;
}

.stButton > button:hover {
    background-color: #5b21b6;
    color: white;
}

/* Result Cards */
.result-success {
    padding: 15px;
    border-radius: 12px;
    background-color: #dcfce7;
    color: #166534;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

.result-danger {
    padding: 15px;
    border-radius: 12px;
    background-color: #fee2e2;
    color: #991b1b;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("credit_scoring_model.pkl")

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header-card">
    <div class="main-title">💳 Credit Scoring Prediction</div>
    <div class="sub-title">
        CodeAlpha Machine Learning Internship Project
    </div>
</div>
""", unsafe_allow_html=True)

st.write("### Enter Customer Details")

# =========================
# INPUT FIELDS
# =========================
col1, col2 = st.columns(2)

with col1:

    person_age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    person_income = st.number_input(
        "Annual Income",
        min_value=0,
        value=50000
    )

    person_emp_length = st.number_input(
        "Employment Length (Years)",
        min_value=0.0,
        value=2.0
    )

    loan_amnt = st.number_input(
        "Loan Amount",
        min_value=0,
        value=10000
    )

    loan_int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        value=10.0
    )

with col2:

    loan_percent_income = st.number_input(
        "Loan Percent Income",
        min_value=0.0,
        value=0.20
    )

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length",
        min_value=0,
        value=5
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        [0, 1, 2, 3]
    )

    loan_intent = st.selectbox(
        "Loan Intent",
        [0, 1, 2, 3, 4, 5]
    )

    loan_grade = st.selectbox(
        "Loan Grade",
        [0, 1, 2, 3, 4, 5, 6]
    )

cb_person_default_on_file = st.selectbox(
    "Previous Default On File",
    [0, 1]
)

# =========================
# PREDICTION
# =========================
if st.button("🔍 Predict Credit Risk"):

    input_data = pd.DataFrame([[
        person_age,
        person_income,
        person_home_ownership,
        person_emp_length,
        loan_intent,
        loan_grade,
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        cb_person_default_on_file,
        cb_person_cred_hist_length
    ]], columns=[
        'person_age',
        'person_income',
        'person_home_ownership',
        'person_emp_length',
        'loan_intent',
        'loan_grade',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_default_on_file',
        'cb_person_cred_hist_length'
    ])

    prediction = model.predict(input_data)[0]

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == 0:
        st.markdown(
            """
            <div class="result-success">
            ✅ LOW CREDIT RISK
            </div>
            """,
            unsafe_allow_html=True
        )
        

    else:
        st.markdown(
            """
            <div class="result-danger">
            ⚠️ HIGH CREDIT RISK
            </div>
            """,
            unsafe_allow_html=True
        )