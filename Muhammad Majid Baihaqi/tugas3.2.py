import streamlit as st
from collections import Counter

st.title("Word Count Komentar Sosial Media")

text = st.text_area("Masukkan komentar:")

if st.button("Hitung"):
    words = text.lower().split()
    count = Counter(words)

    st.subheader("Hasil Word Count")
    st.write(dict(count))