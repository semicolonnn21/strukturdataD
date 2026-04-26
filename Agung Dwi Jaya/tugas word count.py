import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt

# Input komentar
comments = st.text_area("Masukkan komentar sosial media", 
                        "Streamlit sangat bagus, saya suka belajar Python dengan Streamlit!")

# Tokenisasi kata
words = comments.lower().split()
word_count = Counter(words)

st.write("### Frekuensi Kata")
st.write(dict(word_count))

# Visualisasi dengan bar chart
fig, ax = plt.subplots()
ax.bar(word_count.keys(), word_count.values())
plt.xticks(rotation=45)
st.pyplot(fig)
