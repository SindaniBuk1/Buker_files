import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache

def load_data():
	df=pd.read_excel("C:/Users/MATH-BUKER-ANGE/Desktop/Cours et livres/-1/PDS/Analyse des tableaux/DATABASE.xlsx")
	df.dropna(inplace=True)
	num_data=df.select_dtypes(["int","float"])
	num_col=num_data.columns
	text_data=df.select_dtypes(['object'])
	text_col=text_data.columns
	return df,num_col,text_col

df,num_col,text_col=load_data()
st.title("Données d'enquête académique PDS 2020")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(df)
st.sidebar.title("Opérations")
c_b = st.sidebar.checkbox(label="Afficher la base des données")
if c_b:
	st.write(df)

#selection des variables dans la BD
var_select=st.multiselect(label='variables à afficher', options=num_col)
val_num=st.sidebar.checkbox("Numériques")
if val_num:
	st.write(df.select_dtypes(["int","float"]))

