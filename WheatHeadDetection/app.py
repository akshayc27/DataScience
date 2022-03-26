import streamlit as st 
#from PIL import Image
#from classify import predict


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
