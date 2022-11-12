import streamlit as st
from PIL import Image

image = Image.open('./utils/images/profil2.png')

st.image(image,width = 200)
st.title('Loïc Fraichlin Ngongang')
st.header('Data Scientist | Full Stack Developer')
st.caption('Email: ngongangloic151@gmail.com')
st.caption('Tel: +33 0767080270')
st.caption('LinkedIn: [linkedin.com/in/loicngongang](https://www.linkedin.com/in/loicngongang/)')
st.caption('Github: [github.com/Fraichlin](https://github.com/Fraichlin)')#st.write("[link](https://s)")
