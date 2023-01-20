import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

upload_file = st.file_uploader('Upload a file containing earthquake data')

if upload_file is not None:
   df = pd.read_csv(upload_file)

   chart = st.radio(
      "Wybierz rodzaj wizualizacji",
      ('Wykres pudelkowy', 'Histogram'))

   if chart == 'Wykres pudelkowy':
      target = st.radio(
         "Wybierz zmienną",
         df.columns.tolist())

      fig, ax = plt.subplots()
      ax.boxplot(df[target])

      st.pyplot(fig)

   if chart == 'Histogram':
      target = st.radio(
         "Wybierz zmienną",
         df.columns.tolist())

      fig, ax = plt.subplots()
      ax.hist(df[target], bins=20)

      st.pyplot(fig)
