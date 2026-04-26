import streamlit as st
import pandas as pd
from collections import Counter
import re

st.title("📊 Word Count Analisis Komentar")
st.write("Aplikasi ini menghitung frekuensi kemunculan kata.")

comments = st.text_area("Tempelkan teks komentar di sini:", "Wah barangnya bagus banget, saya suka banget barangnya.")

if comments:
    clean_text = re.sub(r'[^\w\s]', '', comments.lower())
    words = clean_text.split()

    if words:
        word_counts = Counter(words)
        df = pd.DataFrame(word_counts.items(), columns=["Kata", "Frekuensi"])
        df = df.sort_values(by="Frekuensi", ascending=False).reset_index(drop=True)

        st.dataframe(df)
        st.bar_chart(df.set_index("Kata"))