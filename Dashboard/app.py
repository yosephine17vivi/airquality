# -*- coding: utf-8 -*-
"""app.py"""  # Change the filename to .py for Streamlit

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('Dashboard/Data Air Quality.csv')

# Convert the 'date' column to datetime type (already done)
df['date'] = pd.to_datetime(df['date'])

# Get the minimum and maximum dates
min_date = df['date'].min()
max_date = df['date'].max()

# Title of the page
st.title('Dashboard Analisis Data Air Quality')

# Sidebar for user inputs
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1163/1163661.png")
    st.sidebar.write('**Nama:** Yosephine Paulina Sianipar')
    st.sidebar.write('**Email:** yosephsianipar17@gmail.com')
    st.sidebar.write('**ML-51**')
 
    # Date input selection
    start_date, end_date = st.date_input(
        label='Pilih Rentang Tanggal',
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Optional: Handle Missing Values (if needed)
# filtered_data = filtered_data.dropna(subset=['date', 'value'])  # Option 1 - remove rows
# OR
# filtered_data.fillna(method='ffill', inplace=True)  # Option 2 - fill missing values

# Filter data based on date range
filtered_data = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Display the filtered data
st.write("Data yang telah difilter berdasarkan rentang tanggal:")
st.dataframe(filtered_data)

# Visualize the data using a seaborn plot
st.subheader('Visualisasi Data Air Quality')
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='date', y='value', data=filtered_data, ax=ax)
st.pyplot(fig)
