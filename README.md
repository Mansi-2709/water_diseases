# 🌍 Water Disease Prediction App

This App is a multipage app made using streamlit. It has a dashboard exploring the relationship between water quality, environmental factors, and disease outcomes. The app also includes a machine learning model to predict diarrheal cases based on water pollution and socioeconomic indicators.

## ✨ Features

### 📊 Data Exploration Dashboard

- There are filters like Country, Region, Water Source, Water Treatment Method on the sidebar to select the values of the filter to be applied.
- There and visuals like bar chart scatter plot and sunburst chart to explore the relationship between water borne diseases like Diarrheal, Infant Mortality Rate, Cholera, Typhoid and Socioeconomic factors like temperature, rainfall, turbidity, GDP, Contaminant Level, Population Density etc.

### 🔍 Multi-Page Navigation

Dashboard: Interactive charts for data exploration

Prediction: ML model to estimate diarrheal cases per 100,000 people

### 🤖 Machine Learning

- There is a Prediction page too in this App that predicts Diarrheal Cases per 100,000 people using XGBoost Regressor.
- The model uses some important features selected using Information Gain Regression Method out of all the given features.
- The missing values in 'Water Treatment Method' column are filled in using Random Imputation Method.
- Encoded the categorical data and then ued the training data to train the model.
- The user is then asked to provide an input data where they have to provide values for each feature and then the result is predicted.

### 📂 Dataset

The dataset (water_pollution_disease.csv) contains 3,000 records with 24 columns, including:

- Covers 10 countries (e.g., USA, India, China, Brazil, Nigeria, Bangladesh, Mexico, Indonesia, Pakistan, Ethiopia).
- Includes 5 regions per country (e.g., North, South, East, West, Central).
- Spans 26 years (2000-2025).
- Water quality: pH level, turbidity, nitrate, lead concentration, bacteria count
- Health outcomes: Diarrheal, Cholera, Typhoid cases; Infant mortality
- Socioeconomic factors: GDP per capita, Healthcare Access Index, Sanitation coverage
- Environmental factors: Rainfall, Temperature, Urbanization rate, Population density

### 📊 Example Visuals

Some of the charts included:

- Bar graph showing different Water Source Type and how they are treated.
- Sunburst chart showing Infant Mortality Rate over different regions and and countries.
- Scatterplot showing Dairrheal Cases over the years
- Bubble chart showing relationship between Cholera Cases and GDP of a Country.
- Line Chart showing relationship between Typhoid Cases and Contamination Level in a Country.

### 🚀 Deployment

The App is deployed to the streamlit platform where anyone can access it with link below and give the inputs to get the predicted output :
[Water Disease Prediction App](https://waterdiseases.streamlit.app/)

Deploy 🎉
