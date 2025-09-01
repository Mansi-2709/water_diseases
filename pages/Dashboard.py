import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Water Disease Dashboard", page_icon=":droplet:",layout="wide")
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/water_diseases/refs/heads/master/water_pollution_disease.csv')

st.sidebar.header("Choose your filter: ")
