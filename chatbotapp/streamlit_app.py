import streamlit as st
import pandas as pd
import numpy as np
from bot import gemini

st.title("Gemini Chat Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])


prompt = st.text_input("Ask Gemini something:")
uploaded_image = st.file_uploader("Upload an image (optional):", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Preview", use_container_width=True)

if st.button("Ask Gemini"):
    if prompt or uploaded_image:
        with st.spinner("Thinking..."):
            response = gemini(prompt if prompt else "Explain this image to me", uploaded_image)

            st.session_state.chat_history.append({"role": "USER: ", "content": prompt if prompt else 'Image'})
            st.session_state.chat_history.append({"role": "GEMINI: ", "content": response})

            st.success(response)
    else:
        st.warning("Please ask a question or upload an image or prompt")
