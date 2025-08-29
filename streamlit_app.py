import streamlit as st
import pandas as pd

st.title('Water Disease Prediction App')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/water_diseases/refs/heads/master/my_dataframe.csv')
  df
  
