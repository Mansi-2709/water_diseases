import streamlit as st
import pandas as pd

st.title('Water Disease Prediction App')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/water_diseases/refs/heads/master/my_dataframe.csv')
  df
  st.write('**X**')
  X = df.drop('Diarrheal Cases per 100,000 people',axis=1)
  X
  st.write('**y**')
  y = df.Diarrheal Cases per 100,000 people
  y
