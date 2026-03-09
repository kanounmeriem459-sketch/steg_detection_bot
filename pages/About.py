import streamlit as st
from load_css import load_css

load_css()


st.set_page_config(page_title="About - Steganography Detection Bot")

# CSS design
st.markdown("""
<style>

/* Background couleur */
.stApp{
background-color:darkcyan;
}

/* Bannière logo en haut */
.banner img{
width:100%;
height:180px;
object-fit:cover;
border-radius:8px;
}

/* Titre About */
.about-title{
text-align:center;
font-size:50px;
color:#006d77;
font-weight:bold;
margin-top:20px;
transition: all 0.3s ease;
cursor:pointer;
}

/* Effet quand on survole */
.about-title:hover{
color:black;
text-shadow: 2px 2px 10px rgba(0,0,0,0.6);
transform: scale(1.05);
}
.about-title:hover{
color:black;
text-shadow:0 0 10px #00fff7, 0 0 20px #00fff7;
}
.about-title:hover{
color:black;
text-shadow:4px 4px 15px rgba(0,0,0,0.8);
}

/* Description */
.about-box{
background-color: rgba(255,255,255,0.9);
padding:40px;
border-radius:12px;
max-width:850px;
margin:40px auto;
box-shadow:0 8px 25px rgba(0,0,0,0.25);
border-left:8px solid #004D40;
}

/* Texte description */
.about-text{
text-align:center;
font-size:22px;
color:#1b1b1b;
line-height:1.8;
}

</style>
""", unsafe_allow_html=True)


# Bannière logo
st.image("assets/Logo-NSCS.png", use_container_width=True)

# Titre
st.markdown(
    '<div class="about-title">About</div>',
    unsafe_allow_html=True
)

# Description
st.markdown(
"""
<div class="about-box">
<div class="about-text">

This project detects hidden messages inside images using **CNN & ML** steganography detection.

The system analyzes uploaded images to determine whether hidden data exists
inside the file using advanced machine learning techniques.

This platform was created for **cybersecurity research and educational purposes**.

</div>
""",
unsafe_allow_html=True
)