import streamlit as st
from collections import Counter
import pandas as pd

st.title("Visualisasi Word Count Komentar")

# Input teks komentar
text = st.text_area("Masukkan komentar sosial media:")

if text:
    # Preprocessing sederhana
    words = text.lower().split()

    # Hitung frekuensi kata
    word_count = Counter(words)

    # Tampilkan sebagai dictionary
    st.subheader("Hasil Word Count (Key = Kata, Value = Frekuensi)")
    st.write(dict(word_count))

    # Ubah ke DataFrame
    df = pd.DataFrame(word_count.items(), columns=["Kata", "Frekuensi"])
    df = df.sort_values(by="Frekuensi", ascending=False)

    # Tampilkan tabel
    st.subheader("Tabel Frekuensi Kata")
    st.dataframe(df)

    # Visualisasi grafik
    st.subheader("Grafik Frekuensi Kata")
    st.bar_chart(df.set_index("Kata"))