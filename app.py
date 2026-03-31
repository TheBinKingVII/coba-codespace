import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Belajar Streamlit", layout="wide")

# Judul
st.title("1. Elemen Dasar di Streamlit 📝")
st.header("Ini adalah Header (Level 2)")
st.subheader("Ini adalah Subheader (Level 3)")

# Garis Pembatas
st.divider()

# Teks
st.write("Ini pakai **st.write()**. Bisa buat nampilin teks, dataframe, dll")
st.markdown("Ini pakai **st.markdown()**. Cocok buat teks panjang dengan *styling* khusus.")
st.text("Ini pakai st.text(). Styling bintang **tidak** jadi tebal.")
st.caption("Ini pakai st.caption(). Teks kecil dan pudar, cocok buat footnote.")

st.divider()

df = pd.read_csv('data_hp.csv')

st.write("Bisa juga nampilin data:")
st.write(df)
