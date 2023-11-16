#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('toy_dataset.csv')
df_MW = df[df['City']=="Mountain View"]

st.write("Here is my first graph:")
st.dataframe(df_MW)

fig, ax = plt.subplots()
ax.hist(df_MW['Income'], edgecolor = "black")
ax.set_title("Histogram of Income in Mountain View")
ax.set_xlabel('Income Value')
ax.set_ylabel('Count')

st.pyplot(fig)


# In[ ]:





# In[ ]:




