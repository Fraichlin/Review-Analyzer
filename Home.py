import streamlit as st
from PIL import Image

st.title('NLF Review Analyzer')
st.header('The most accurate restaurant review analyzer you ever seen !')

image = Image.open('./utils/images/review.jpg')

st.image(image,width = 600)
