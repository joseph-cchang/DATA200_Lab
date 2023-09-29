#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Fish.csv')

st.write("Here is a display of the fish dataframe:")
st.dataframe(df)


st.write("Here is a condensed dataframe")
st.dataframe(df[['Species', 'Weight', 'Height']])


st.write("Here is a histogram graph")
n_bins = 10
fig, ax = plt.subplots()
ax.hist(df['Height'], edgecolor = "black")
ax.set_title("Histogram of Height")
ax.set_xlabel('Height Value')
ax.set_ylabel('Count')

st.pyplot(fig)
st.write("This histogram shows the height of the fish. The most common fish height is between the 5.0 - 7.5, with around 40 counts. Overall, the distribution seems skew right.")
st.button("Click me")
st.download_button("Download file", df)


st.write("Here is a scatterplot graph")
fig, ax = plt.subplots()
ax.scatter(df['Height'], df['Weight'])
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Weight vs Height")
st.pyplot(fig)

st.write("This scatterplot is harder to infer, but a exponential graph could be used to infer. After 7.5 in Height, it's more difficult to access.")


# In[ ]:




