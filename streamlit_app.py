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
  y = df[['Diarrheal Cases per 100,000 people']]
  y

with st.expander('Input your data'):
  Country = st.selectbox('Country', ('USA', 'Nigeria', 'China', 'Indonesia', 'Pakistan', 'Ethiopia', 'Brazil', 'Bangladesh', 'India', 'Mexico'))
  Contaminant Level = st.slider('Contaminant Level (ppm)', 0.0, 10.0, 4.9)
  Population Density = st.slider('Population Density (people per km²)', 10.0, 999.0, 505.0)
  Access to Clean Water = st.slider('Access to Clean Water (% of Population)', 30.0, 99.9, 64.6)
  pH Level = st.slider('pH Level', 6.0, 8.5, 7.2)
  Turbidity = st.slider('Turbidity (NTU)', 0.0, 4.9, 2.4)
  Rainfall = st.slider('Rainfall (mm per year)', 200.0, 2999.0, 1591.8)
  Healthcare Access Index = st.slider('Healthcare Access Index (0-100)', 0.1, 99.9, 50.0)
  Dissolved Oxygen = st.slider('Dissolved Oxygen (mg/L)', 3.0, 10.0, 6.4)
  Nitrate Level = st.slider('Nitrate Level (mg/L)', 0.0, 49.9, 25.0)
  Temperature = st.slider('Temperature (°C)', 0.0, 39.9, 20.1)
  GDP per Capita = st.slider('GDP per Capita (USD)', 521.0, 99948.0, 50036.1)
  Sanitation Coverage = st.slider('Sanitation Coverage (% of Population)', 20.0, 99.9, 60.3)
  Bacteria Count = st.slider('Bacteria Count (CFU/mL)', 0.0, 4998.0, 2488.4)
  Region = st.selectbox('Region', ('North', 'South', 'East', 'West', 'Central'))
