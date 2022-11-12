import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
import pickle
import sys
sys.path.append('./utils')
from preprocessing import preprocess_text
st.title("Extract topic(s) and sentiment popularity from your review")


topic_labels = {
    0 : 'manager_service',
    1 : 'general_meal_quality',
    2 : 'menu_pizza',
    3 : 'menu_chicken',
    4 : 'value_for_money',
    5 : 'waiting_time',
    6 : 'menu_burger',
    7 : 'quality_place',
    8 : 'experience',
    9 : 'drink_quality',
    10 : 'delivery_service',
    11 : 'notice_frequency',
    12 : 'general_service_quality',
    13 : 'menu_sushi',
    14 : 'overall score'
}

with open(r"./utils/model_loic.", "rb") as input_file:
  model = pickle.load(input_file)

with open(r"./utils/vectorizer_loic", "rb") as input_file:
  vectorizer = pickle.load(input_file)

def predict(text, nombre_topics):
  blob = TextBlob(text)
  polarity = blob.sentiment.polarity
  text = preprocess_text(text)
  result = []
  if polarity < 0:
    t_list = []
    t_list.append(text)
    t = vectorizer.transform(t_list)
    topics = model.transform(t)
    topics = list(topics[0])
    temp = sorted(topics,reverse=True)
    topics_sort = [topics.index(i) for i in temp]
    result = [topic_labels[i] for i in topics_sort]
    return [result[:int(nombre_topics)],polarity]
  else: 
    return [result,polarity]


with st.form(key='my_form'):    
    text = st.text_area('Enter your text')
    topic_number = st.selectbox('Choose the number of topic', list(np.arange(1,16)))
    submitted = st.form_submit_button('Detect topics')
    if submitted:
      result = predict(text,topic_number)
      if len(result[0]) == 0:
        if result[1] == 0:
          st.info('Your review is neutral --> Polarity : {0:.2f}'.format(result[1]))
        else:
          st.info('Your review is positive :)  --> Polarity : {0:.2f}'.format(result[1]))
      else:
        st.info('Your review is negative :(  --> Polarity : {0:.2f}'.format(result[1]))
        st.info('Topic(s) : '+str([i for i in result[0]]))
          

