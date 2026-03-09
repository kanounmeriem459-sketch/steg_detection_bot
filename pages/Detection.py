import streamlit as st
import numpy as np
from PIL import Image
from model_loader import load_my_model

from load_css import load_css

load_css()

st.set_page_config(page_title="Steganography Detection Bot")

st.markdown("""
<style>

/* Background couleur */
.stApp{
background-color: darkcyan;
}
            
/* Titre Detection */
.detection-title{
text-align:center;
font-size:50px;
color:#004D40;
font-weight:bold;
margin-top:20px;
transition: all 0.3s ease;
cursor:pointer;
}

/* Effet hover titre */
.detection-title:hover{
color:black;
text-shadow: 4px 4px 15px rgba(0,0,0,0.8);
transform: scale(1.05);
}

/* File uploader label (texte "Upload an image") */
.css-1emrehy.edgvbvh3{
font-size:24px !important;  /* plus grand */
font-weight:bold !important;  /* en gras */
color: #004D40 !important;    /* couleur vert foncé */
}

/* Result box */
.result-box{
background-color: rgba(255,255,255,0.9);
padding:25px;
border-radius:12px;
max-width:700px;
margin:20px auto;
box-shadow:0 6px 20px rgba(0,0,0,0.3);
border-left:6px solid #004D40;
text-align:center;
font-size:20px;
}

</style>
""", unsafe_allow_html=True)


# Titre
st.markdown('<div class="detection-title">Steganography Detection</div>', unsafe_allow_html=True)


# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

# Fake model pour test
model = load_my_model()

if uploaded_file:
    image = Image.open(uploaded_file)
  
    st.image(image, use_container_width=True)
   

    if st.button("Analyze"):
        img = np.array(image).reshape(1,-1)
        prediction = model.predict(img)
        confidence = prediction[0][0]

        if confidence > 0.5:
            st.markdown(f'<div class="result-box" style="border-left:6px solid red;">Hidden data detected ({confidence*100:.1f}%)</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-box" style="border-left:6px solid green;">Image looks safe ({(1-confidence)*100:.1f}%)</div>', unsafe_allow_html=True)