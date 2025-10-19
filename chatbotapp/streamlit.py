
import streamlit as st
import pandas as pd
import numpy as np
from bot import gemini
st.title("gemini chat bot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💻 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Gemini:** {msg['content']}")


prompt = st.text_input("Ask Gemini something:")
uploaded_image = st.file_uploader("Upload an image (optional):", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Preview", use_container_width=True)

if st.button("Ask Gemini"):
    if prompt or uploaded_image:
        with st.spinner("Thinking..."):
      
            response = gemini(prompt if prompt else "Explain this image to me", uploaded_image)

          
            st.session_state.chat_history.append({"role": "user", "content": prompt if prompt else 'Image'})
            st.session_state.chat_history.append({"role": "gemini", "content": response})


            st.success(response)
    else:
        st.warning("Please ask a question or upload an image or prompt")