import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

df = pd.read_csv('./utils/dataset_cleaned.csv')
image = Image.open('./utils/images/bar_chart.png')
st.title('Dataset')
st.caption('We have 4 columns : text,stars,length and text_cleaned')
st.caption("stars represent the review's note, the most it's high the most the review is positive")
st.dataframe(df)
st.title('Number of text per stars')
st.image(image,width = 500)

stars = list(df.stars.value_counts().index)
index = np.argsort(stars)
stars.sort()
values = df.stars.value_counts().values
values = [values[i] for i in index]


