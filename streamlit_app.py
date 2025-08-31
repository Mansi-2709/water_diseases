import streamlit as st
import pandas as pd
import xgboost as xg
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

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
  st.write('Input Feature Data')
  Country = st.selectbox('Country', ('USA', 'Nigeria', 'China', 'Indonesia', 'Pakistan', 'Ethiopia', 'Brazil', 'Bangladesh', 'India', 'Mexico'))
  Contaminant_Level = st.slider('Contaminant Level (ppm)', 0.0, 10.0, 4.9)
  Population_Density = st.slider('Population Density (people per km²)', 10.0, 999.0, 505.0)
  Access_to_Clean_Water = st.slider('Access to Clean Water (% of Population)', 30.0, 99.9, 64.6)
  pH_Level = st.slider('pH Level', 6.0, 8.5, 7.2)
  Turbidity = st.slider('Turbidity (NTU)', 0.0, 4.9, 2.4)
  Rainfall = st.slider('Rainfall (mm per year)', 200.0, 2999.0, 1591.8)
  Healthcare_Access_Index = st.slider('Healthcare Access Index (0-100)', 0.1, 99.9, 50.0)
  Dissolved_Oxygen = st.slider('Dissolved Oxygen (mg/L)', 3.0, 10.0, 6.4)
  Nitrate_Level = st.slider('Nitrate Level (mg/L)', 0.0, 49.9, 25.0)
  Temperature = st.slider('Temperature (°C)', 0.0, 39.9, 20.1)
  GDP_per_Capita = st.slider('GDP per Capita (USD)', 521.0, 99948.0, 50036.1)
  Sanitation_Coverage = st.slider('Sanitation Coverage (% of Population)', 20.0, 99.9, 60.3)
  Bacteria_Count = st.slider('Bacteria Count (CFU/mL)', 0.0, 4998.0, 2488.4)
  Region = st.selectbox('Region', ('North', 'South', 'East', 'West', 'Central'))
  data = {'Contaminant Level (ppm)': Contaminant_Level, 
        'Population Density (people per km²)': Population_Density, 
        'Access to Clean Water (% of Population)': Access_to_Clean_Water, 
        'pH Level': pH_Level, 
        'Turbidity (NTU)': Turbidity, 
        'Rainfall (mm per year)': Rainfall, 
        'Healthcare Access Index (0-100)': Healthcare_Access_Index, 
        'Region': Region, 
        'Dissolved Oxygen (mg/L)': Dissolved_Oxygen, 
        'Nitrate Level (mg/L)': Nitrate_Level, 
        'Temperature (°C)': Temperature, 
        'GDP per Capita (USD)': GDP_per_Capita, 
        'Country': Country, 
        'Sanitation Coverage (% of Population)': Sanitation_Coverage, 
        'Bacteria Count (CFU/mL)': Bacteria_Count}
  input_df = pd.DataFrame(data, index=[0])
  input_disease = pd.concat([input_df,X], axis=0)
with st.expander('Input features'):
	input_df
	encoder = LabelEncoder()
	input_disease['Country'] = encoder.fit_transform(input_disease['Country'])
	input_disease['Region'] = encoder.fit_transform(input_disease['Region'])
	X=input_disease[1:]
	clf = xg.XGBRegressor(objective='reg:squarederror', random_state=42)
	params_grid = {
            'n_estimators': [100,200,500],
	        'learning_rate':[0.01, 0.05, 0.1, 0.2],
            'max_depth':[3,6]
        }
	cv=KFold(n_splits=5,random_state=None,shuffle=False)
	grid_search = GridSearchCV(clf, params_grid, cv=cv, scoring='f1_macro', return_train_score=False)
	grid_search.fit(X,y)
	input_df=input_disease[:1]

with st.expander('Predictions'):
	y_pred=grid_search.predict(input_df)
	st.write('Diarrheal Cases per 100,000 people for the given input is :', y_pred)
