
import streamlit as st
import pandas as pd
import numpy as np
from bot import gemini
from PIL import Image

st.title("Gemini ChatBot")

prompt=st.text_input("ask gemini:")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_image:
    st.image(uploaded_image,caption="preview",use_container_width=True)
if st.button("ask"):
    if prompt and uploaded_image:
        response=gemini(prompt,uploaded_image)
        st.success(response)

    elif uploaded_image:
        response=gemini("explain this image to me",uploaded_image)
        st.success(response)
    elif prompt:
        response=gemini(prompt)
        st.success(response)    
    else:
        st.warning("ask something to gemini")    