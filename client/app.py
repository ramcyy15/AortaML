import os
from pathlib import Path

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "")
BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "Logo.png"

st.set_page_config(
    page_title="AortaML",
    page_icon=str(LOGO_PATH),
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --brand-red: #E50609;
        --brand-red-deep: #b90507;
        --brand-red-soft: #fff3f3;
        --brand-red-ghost: #fff5f5;
        --ink: #1a1a1a;
        --muted: #5c6069;
        --panel: #ffffff;
        --panel-border: rgba(229, 6, 9, 0.17);
        --shadow: 0 12px 28px rgba(229, 6, 9, 0.08);
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        font-family: 'Manrope', 'Segoe UI', sans-serif;
        background: linear-gradient(180deg, #fff6f6 0%, #fff 40%, #fff 100%);
        color: var(--ink);
    }

    .block-container {
        padding-top: 1.3rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .brand-shell {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid var(--panel-border);
        border-radius: 22px;
        padding: 0.9rem 1.1rem;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
    }

    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }

    .brand-wrap img {
        width: 60px;
        height: 60px;
        object-fit: contain;
        border-radius: 18px;
        background: white;
        padding: 6px;
        border: 1px solid rgba(17, 24, 39, 0.06);
    }

    .brand-title {
        margin: 0;
        font-size: 2.1rem;
        line-height: 1.05;
        font-weight: 800;
        letter-spacing: -0.05em;
        color: var(--ink);
    }

    .brand-kicker {
        font-size: 0.72rem;
        letter-spacing: 0.17em;
        text-transform: uppercase;
        color: var(--muted);
        margin-top: 0.2rem;
        font-weight: 700;
    }

    .hero {
        background: linear-gradient(135deg, var(--brand-red) 0%, var(--brand-red-deep) 100%);
        border-radius: 28px;
        padding: 1.5rem 1.5rem 1.2rem;
        box-shadow: 0 22px 40px rgba(229, 6, 9, 0.18);
        margin-bottom: 1.35rem;
    }

    .hero p {
        margin: 0.65rem 0 0 0;
        color: rgba(255, 255, 255, 0.82);
        max-width: 760px;
        font-size: 1rem;
        line-height: 1.6;
    }

    div[data-testid="stForm"] {
        background: linear-gradient(180deg, #fff8f8 0%, #ffffff 100%);
        border: 1px solid var(--panel-border);
        border-radius: 26px;
        padding: 1.2rem;
        box-shadow: var(--shadow);
    }

    .panel-header {
        margin: 0 0 0.9rem 0;
        font-size: 1.3rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: var(--ink);
    }

    [data-testid="stNumberInput"],
    [data-testid="stSelectbox"],
    [data-testid="stTextInput"] {
        background: #fff;
        border-radius: 14px;
    }

    [data-testid="stNumberInput"] > div,
    [data-testid="stTextInput"] > div,
    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: #fff !important;
        border-color: rgba(229, 6, 9, 0.28) !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }

    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] input,
    [data-testid="stSelectbox"] [role="combobox"] {
        background: #fff !important;
        color: var(--ink) !important;
        font-weight: 700;
        -webkit-text-fill-color: var(--ink) !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] * {
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
    }

    [data-testid="stSelectbox"] svg {
        color: var(--brand-red) !important;
        fill: var(--brand-red) !important;
    }

    [data-testid="stNumberInput"] button,
    [data-testid="stNumberInputStepDown"],
    [data-testid="stNumberInputStepUp"] {
        background: var(--brand-red) !important;
        color: #fff !important;
        border-color: var(--brand-red) !important;
        opacity: 1 !important;
    }

    [data-testid="stNumberInput"] button:hover,
    [data-testid="stNumberInputStepDown"]:hover,
    [data-testid="stNumberInputStepUp"]:hover {
        background: var(--brand-red-deep) !important;
        color: #fff !important;
        border-color: var(--brand-red-deep) !important;
    }

    [data-testid="stNumberInput"] button svg {
        color: #fff !important;
        fill: #fff !important;
    }

    .stNumberInput label, .stSelectbox label {
        font-weight: 700;
        color: var(--ink);
    }

    .stButton > button,
    [data-testid="stFormSubmitButton"] button {
        background: linear-gradient(135deg, var(--brand-red) 0%, var(--brand-red-deep) 100%) !important;
        color: #fff !important;
        -webkit-text-fill-color: #fff !important;
        border: 1px solid var(--brand-red) !important;
        border-radius: 14px;
        font-weight: 800;
        font-size: 1rem;
        padding: 0.8rem 1.3rem;
        box-shadow: 0 12px 28px rgba(229, 6, 9, 0.22);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
        opacity: 1 !important;
    }

    .stButton > button p,
    [data-testid="stFormSubmitButton"] button p {
        color: #fff !important;
        -webkit-text-fill-color: #fff !important;
    }

    .stButton > button:hover,
    [data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-1px);
        background: var(--brand-red-deep) !important;
        border-color: var(--brand-red-deep) !important;
        box-shadow: 0 14px 30px rgba(229, 6, 9, 0.26);
    }

    .stButton > button:focus-visible,
    [data-testid="stFormSubmitButton"] button:focus-visible,
    [data-testid="stNumberInput"] button:focus-visible {
        outline: 3px solid rgba(229, 6, 9, 0.3) !important;
        outline-offset: 2px;
    }

    .result-card {
        background: linear-gradient(180deg, #ffffff 0%, #fff5f5 100%);
        border: 1px solid rgba(229, 6, 9, 0.14);
        border-radius: 22px;
        padding: 1.2rem;
        box-shadow: var(--shadow);
    }

    .metric-wrap {
        display: flex;
        align-items: baseline;
        gap: 0.5rem;
        margin: 0;
    }

    .metric-wrap .value {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        color: var(--brand-red-deep);
    }

    .metric-wrap .label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--muted);
        font-weight: 700;
    }

    .stAlert, .stSuccess, .stError {
        border-radius: 18px;
        border: none;
        box-shadow: var(--shadow);
        padding: 0.9rem 1rem;
    }

    @media (max-width: 768px) {
        .brand-title {
            font-size: 1.6rem;
        }

        .hero {
            padding: 1.2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="brand-shell">', unsafe_allow_html=True)
brand_col, text_col = st.columns([1, 5])
with brand_col:
    st.image(str(LOGO_PATH), width=58)
with text_col:
    st.markdown('<div class="brand-title">AortaML</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-kicker">heart disease risk intelligence</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
      <p>Review patient data in a cleaner, more confident workflow designed for fast, accurate cardiovascular screening.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="panel-header">Patient profile</p>', unsafe_allow_html=True)

with st.form("risk_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120, 52)
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
        cp = st.number_input("Chest Pain Type (cp)", 0, 3, 0)
        trestbps = st.number_input("Resting Blood Pressure", 0, 250, 125)
        chol = st.number_input("Cholesterol", 0, 600, 212)

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.number_input("Resting ECG (restecg)", 0, 2, 1)
        thalach = st.number_input("Max Heart Rate (thalach)", 0, 250, 168)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])

    with col3:
        oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 10.0, 1.0)
        slope = st.number_input("Slope", 0, 2, 2)
        ca = st.number_input("Number of Major Vessels (ca)", 0, 4, 0)
        thal = st.number_input("Thal", 0, 3, 2)

    submitted = st.form_submit_button("Assess risk")

if submitted:
    if not API_URL:
        st.warning("Add your API_URL in the environment to connect the predictive model.")
    else:
        input_data = {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal,
        }

        try:
            response = requests.post(API_URL, json=input_data, timeout=20)
            if response.status_code != 200:
                st.error("Server request failed. Please check the API connection.")
            else:
                result = response.json()
                prediction = result["prediction"]
                probability = float(result["probability"])
                diagnosis = result["diagnosis"]

                st.markdown(
                    """
                    <div class="result-card">
                        <div class="metric-wrap">
                            <div class="label">Risk probability</div>
                            <div class="value">{:.2f}%</div>
                        </div>
                    </div>
                    """.format(probability * 100),
                    unsafe_allow_html=True,
                )

                if prediction == 1:
                    st.error(f"Model analysis: {diagnosis}")
                else:
                    st.success(f"Model analysis: {diagnosis}")
        except requests.RequestException as exc:
            st.error(f"Request failed: {exc}")
