import streamlit as st
from PIL import Image
import google.generativeai as genai
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Healthcare Assistant 🇮🇳",
    page_icon="🩺",
    layout="wide"
)

# --- Gemini Configuration ---
genai.configure(api_key="AIzaSyBwN_gOTSq367tHm4n3ABGS50gyzBhWMBs")
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# --- Advanced CSS for Full-Scale Interface ---
st.markdown("""
    <style>
    body, html {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #eafaf1, #f0f8ff);
        color: #333;
    }
    .main {
        background: #fff;
        padding: 40px;
        margin: 30px;
        border-radius: 20px;
        box-shadow: 0 6px 30px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #00695c;
        color: white;
        padding: 14px 30px;
        font-size: 20px;
        border-radius: 12px;
        transition: 0.3s;
        border: none;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #004d40;
        transform: scale(1.05);
    }
    .header-title {
        font-size: 42px;
        color: #004d40;
        font-weight: bold;
        padding-bottom: 10px;
    }
    .subtext {
        font-size: 18px;
        color: #666;
    }
    .big-container {
        display: flex;
        flex-direction: row;
        gap: 50px;
        margin-top: 30px;
    }
    .section {
        flex: 1;
        padding: 20px;
        background: #f9fcfb;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    footer {
        text-align: center;
        font-size: 14px;
        margin-top: 60px;
        padding: 20px;
        background-color: #e0f2f1;
        border-top: 2px solid #80cbc4;
        color: #004d40;
        border-radius: 0 0 12px 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="header-title">🩺 Unified AI Healthcare Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">AI-powered diagnosis & personalized care plans for rural healthcare workers and patients</div>', unsafe_allow_html=True)

# --- Main Section Layout ---
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=250)
    st.markdown("### 📥 Upload Patient Data")
    uploaded_image = st.file_uploader("Upload Medical Image (X-ray, Retina, Skin)", type=["jpg", "png", "jpeg"])
    uploaded_pdf = st.file_uploader("Upload Scanned Notes / Prescriptions", type=["pdf", "jpg", "png"])

with col2:
    st.markdown("### 📝 Enter Symptoms & History")
    symptoms = st.text_area("Describe the patient’s symptoms and relevant history")
    language = st.selectbox("Choose output language", ["English", "Hindi", "Tamil", "Telugu"])
    st.warning("🎤 Voice input coming soon!")

# --- Diagnosis Button ---
st.markdown("---")
if st.button("💡 Run Diagnosis and Recommendation"):
    with st.spinner("Analyzing medical data with AI..."):
        time.sleep(1.5)

        prompt = f"""
        Analyze the following patient data and generate:
        - Diagnosis
        - Personalized treatment plan
        - Alerts or risk flags
        - EHR-style summary (translated to {language})

        Symptoms and History: {symptoms if symptoms else 'Not provided'}
        """

        input_blocks = [prompt]
        if uploaded_image:
            image = Image.open(uploaded_image)
            input_blocks.append(image)
        elif uploaded_pdf:
            input_blocks.append(uploaded_pdf)

        response = model.generate_content(input_blocks)

    st.success("✅ Diagnosis Completed")
    st.balloons()

    st.subheader("🧠 AI Diagnosis & Recommendations")
    st.markdown(response.text)

    st.download_button("📄 Download Report", data=response.text, file_name="ai_diagnosis_report.txt")

# --- Footer ---
st.markdown("""
<footer>
    👣 Designed with ❤️ for inclusive rural healthcare across India 🇮🇳<br><br>
    &copy; 2025 • AI Health Assist Project • All rights reserved
</footer>
""", unsafe_allow_html=True)
