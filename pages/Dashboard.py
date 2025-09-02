import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Water Disease Dashboard", page_icon=":droplet:",layout="wide")
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/water_diseases/refs/heads/master/water_pollution_disease.csv')

# Sidebar filters
st.sidebar.header("Filters")

# Country filter
countries = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].dropna().unique(),
    default=df["Country"].dropna().unique()
)

# Region filter
regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].dropna().unique(),
    default=df["Region"].dropna().unique()
)

# Water source filter
sources = st.sidebar.multiselect(
    "Select Water Source Type",
    options=df["Water Source Type"].dropna().unique(),
    default=df["Water Source Type"].dropna().unique()
)

# Water treatment filter
treatments = st.sidebar.multiselect(
    "Select Water Treatment",
    options=df["Water Treatment Method"].dropna().unique(),
    default=df["Water Treatment Method"].dropna().unique()
)

# Apply filters
filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["Region"].isin(regions)) &
    (df["Water Source Type"].isin(sources)) &
    (df["Water Treatment Method"].isin(treatments))
]

st.title("🌍 Water Pollution & Disease Dashboard")

st.markdown("Use the filters in the sidebar to explore the data interactively.")

# Example Plot 1: Distribution of water sources
if not filtered_df.empty:
    fig1 = px.histogram(
        filtered_df,
        x="Water Source Type",
        color="Water Treatment Method",
        barmode="group",
        title="Distribution of Water Sources by Treatment"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Example Plot 2: Cases by Country
    if not filtered_df.empty:
        fig2 = px.scatter(filtered_df, x="Year", y="Diarrheal Cases per 100,000 people", color="Country", hover_data=['Region'])
        st.plotly_chart(fig2, use_container_width=True)

    if not filtered_df.empty:
        fig3 = px.sunburst(filtered_df, path=['Region', 'Country'], values='Infant Mortality Rate (per 1,000 live births)', color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(filtered_df['Infant Mortality Rate (per 1,000 live births)'], weights=filtered_df['Infant Mortality Rate (per 1,000 live births)']))
        st.plotly_chart(fig3, use_container_width=True)

    if not filtered_df.empty:
        fig4 = px.scatter(filtered_df, x="GDP per Capita (USD)", y="Cholera Cases per 100,000 people", size="Population Density (people per km²)", color="Country", log_x=True, size_max=60)
        st.plotly_chart(fig4, use_container_width=True)
else:
    st.warning("No data available for the selected filters.")
