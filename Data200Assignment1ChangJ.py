#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


fish_df = pd.read_csv('Fish.csv')
toy_df = pd.read_csv("toy_dataset.csv")

st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Joseph Chang </p>', unsafe_allow_html=True)
st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> DATA 200 Assignment 1</p>', unsafe_allow_html=True)

st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a display of the fish dataframe: </p>', unsafe_allow_html=True)
st.dataframe(fish_df)

if st.button("Click here to see a condensed Dataframe"):
    st.dataframe(fish_df[['Species', 'Weight', 'Height']])

# Graph 1
st.write("Here is a histogram graph:")
n_bins = 10
fig, ax = plt.subplots()
ax.hist(fish_df['Height'], edgecolor = "black")
ax.set_title("Histogram of Height")
ax.set_xlabel('Height Value')
ax.set_ylabel('Count')
st.pyplot(fig)
st.write("This histogram shows the height of the fish. The most common fish height is between the 5.0 - 7.5, with around 40 counts. Overall, the distribution seems skew right.")

# Graph 2
st.write("Here is a scatterplot graph:")
fig, ax = plt.subplots()
ax.scatter(fish_df['Height'], fish_df['Weight'])
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Weight vs Height")
st.pyplot(fig)
st.write("This scatterplot is harder to infer, but a exponential graph could be used to infer. After 7.5 in Height, it's more difficult to access.")

# Graph 3
st.write("Here is a bar graph:")
fish_df.groupby(['Species'])['Width'].mean()
fig, ax = plt.subplots()
species = fish_df['Species'].unique()
mean_wid = fish_df.groupby(['Species'])['Width'].mean()
ax.bar(species, mean_wid)
ax.set_xlabel('Species')
ax.set_ylabel('Mean Width')
ax.set_title('Species by the Mean Width')
st.pyplot(fig)
st.write("This bar graph shows the mean wid of all the species. Here we can see that on average, Parkki has the highest at around 40. The lowest is Pike at around 11.")

# Graph 4
st.write("Here is a stem plot:")
fig, ax = plt.subplots()
ax.stem(fish_df['Height'], fish_df['Width'])
ax.set_xlabel("Height")
ax.set_ylabel("Width")
ax.set_title("Height vs Width")
st.pyplot(fig)
st.write("This stem plot ....")

st.markdown("""<style>.big-font {font-size:20px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a display of the toy dataframe: </p>', unsafe_allow_html=True)
st.dataframe(toy_df)

if st.button("Click here to see the dataframe only in Mountain View"):
    df_MW = df[df['City']=="Mountain View"]
    st.dataframe(df_MW)

# Graph 5
'''
st.write("Here is another histogram graph:")
fig, ax = plt.subplots()
ax.hist(df_MW['Income'], edgecolor = "black")
ax.set_title("Histogram of Income in Mountain View")
ax.set_xlabel('Income Value')
ax.set_ylabel('Count')
st.pyplot(fig)
st.write("This bar graph shows the histogram of income for people living in Mountain View.")
'''

st.write("Here is a boxplot:")
fig, ax = plt.subplots()
ax.boxplot(df_MW['Income'])
ax.set_title("Boxplot of Income in Mountain View")
ax.set_xlabel('Income Value')
ax.set_ylabel('Value')
st.pyplot(fig)
st.write("This bar graph shows the histogram of income for people living in Mountain View.")


