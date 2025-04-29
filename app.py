import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\ekpin\Documents\python\data\employees.csv", parse_dates=['hire_date', 'termination_date'])


st.title("📊 HR Dashboard")

# Фильтры
dept = st.selectbox("Отдел", options=['Все'] + df['department'].dropna().unique().tolist())
gender = st.selectbox("Пол", options=['Все', 'Male', 'Female'])

filtered = df.copy()
if dept != 'Все':
    filtered = filtered[filtered['department'] == dept]
if gender != 'Все':
    filtered = filtered[filtered['gender'] == gender]

# Визуализация: гендер
gender_fig = px.histogram(filtered, x="gender", title="Гендерное распределение")
st.plotly_chart(gender_fig)

# Возраст
age_fig = px.box(filtered, y="age", title="Распределение по возрасту")
st.plotly_chart(age_fig)

# Текучесть
df['year'] = df['termination_date'].dt.year
turnover = df['year'].value_counts().sort_index()
st.bar_chart(turnover)
