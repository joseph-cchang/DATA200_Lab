#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

fish_df = pd.read_csv('Fish.csv')
toy_df = pd.read_csv("toy_dataset.csv")

st.markdown("""<style>.big-font {font-size:12px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a display of the fish dataframe: </p>', unsafe_allow_html=True)
st.dataframe(fish_df)

if st.button("Click here to see a condensed Dataframe"):
    st.dataframe(fish_df[['Species', 'Weight', 'Height']])

st.write("Here is a histogram graph")
n_bins = 10
fig, ax = plt.subplots()
ax.hist(fish_df['Height'], edgecolor = "black")
ax.set_title("Histogram of Height")
ax.set_xlabel('Height Value')
ax.set_ylabel('Count')
st.pyplot(fig)
st.write("This histogram shows the height of the fish. The most common fish height is between the 5.0 - 7.5, with around 40 counts. Overall, the distribution seems skew right.")


st.write("Here is a scatterplot graph")
fig, ax = plt.subplots()
ax.scatter(fish_df['Height'], fish_df['Weight'])
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Weight vs Height")
st.pyplot(fig)
st.write("This scatterplot is harder to infer, but a exponential graph could be used to infer. After 7.5 in Height, it's more difficult to access.")


st.write("Here is a bar graph")
fish_df.groupby(['Species'])['Length1'].mean()
fig, ax = plt.subplots()
species = fish_df['Species'].unique()
mean_len1 = fish_df.groupby(['Species'])['Length1'].mean()
ax.bar(species, mean_len1)
ax.set_xlabel('Species')
ax.set_ylabel('Mean Length 1')
ax.set_title('Species by the Mean of Length 1')
st.pyplot(fig)
st.write("This bar graph shows the mean of length 1 of all the species. Here we can see that on average, Parkki has the highest at around 40. The lowest is Pike at around 11.")



st.markdown("""<style>.big-font {font-size:12px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a display of the toy dataframe: </p>', unsafe_allow_html=True)
st.dataframe(toy_df)


