import streamlit as st
from collections import Counter
import pandas as pd

st.title("Word Count Komentar Sosial Media")

# Input teks
text = st.text_area("Masukkan komentar:")

if text:
    # Preprocessing sederhana
    words = text.lower().split()

    # Hitung frekuensi
    word_count = Counter(words)

    # Convert ke DataFrame
    df = pd.DataFrame(word_count.items(), columns=["Kata", "Frekuensi"])
    df = df.sort_values(by="Frekuensi", ascending=False)

    st.subheader("Tabel Frekuensi Kata")
    st.dataframe(df)

    st.subheader("Visualisasi")
    st.bar_chart(df.set_index("Kata"))