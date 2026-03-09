import base64
import streamlit as st
from load_css import load_css

load_css()



st.set_page_config(page_title="Steganography Detection Bot")


@st.cache_data
def get_base64_background(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


try:
    bin_str = get_base64_background("assets\decoding.webp")
except FileNotFoundError:
    bin_str = "" 

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{bin_str}");
    background-size: cover;
    background-attachment: fixed; 
    background-position: center;
}}

.title-box {{
    text-align: center;
    font-size: clamp(24px, 5vw, 48px); /* Responsive : s'adapte à l'écran */
    font-weight: bold;
    color: #006d77;
    padding: 20px;
    border: 4px solid #0b3d2e;
    border-radius: 15px;
    width: 80%;
    margin: 100px auto; /* Centre verticalement un peu plus */
    background: rgba(255,255,255,0.85);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
    transition: transform 0.3s ease;
}}

.title-box:hover {{
    transform: translateY(-5px) scale(1.02);
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box">Steganography Detection Bot</div>', unsafe_allow_html=True)