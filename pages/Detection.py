import streamlit as st
import numpy as np
from PIL import Image
from model_loader import load_my_model

st.title("Steganography Detection")

model = load_my_model()

uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image)

    if st.button("Analyze"):

        img = np.array(image).reshape(1,-1)

        prediction = model.predict(img)

        confidence = prediction[0][0]

        if confidence > 0.5:
            st.error(f"Hidden data detected ({confidence*100:.1f}%)")

        else:
            st.success("Image looks safe")