#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Fish.csv')

st.write("Here is a display of the fish dataframe:")
st.dataframe(df)


st.write("Here is a histogram graph")
n_bins = 10
fig, ax = plt.subplots()
ax.hist(df['Height'], edgecolor = "black")
ax.set_title("Histogram of Height")
ax.set_xlabel('Height Value')
ax.set_ylabel('Count')

st.pyplot(fig)


st.write("Here is a scatterplot graph")
fig, ax = plt.figure()
ax.scatter(df['Height'], df['Weight'])
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Weight vs Height")
st.pyplot(fig)


