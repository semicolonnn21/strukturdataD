import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# Pengaturan Judul Aplikasi
st.set_page_config(page_title="Social Media Word Count", layout="wide")
st.title("📊 Visualisasi Word Count Komentar Sosial Media")

# 1. Contoh Data Komentar (Bisa diganti dengan upload CSV nantinya)
data_komentar = [
    "aplikasi ini sangat bagus dan bermanfaat",
    "keren sekali fiturnya sangat membantu",
    "kurang suka dengan update terbaru",
    "bagus banget aplikasinya sangat lancar",
    "fiturnya sangat keren dan sangat cepat",
    "biasa saja sih tidak ada yang spesial",
    "sangat puas dengan layanan ini sangat ramah"
]

# 2. Pemrosesan Kata (Data Cleaning Sederhana)
def get_word_frequencies(text_list):
    all_words = " ".join(text_list).lower()
    # Menghapus karakter non-alfabet
    words = re.findall(r'\b\w+\b', all_words)
    
    # Menghitung frekuensi (Key: Kata, Value: Frekuensi)
    return Counter(words)

word_counts = get_word_frequencies(data_komentar)

# Mengonversi ke DataFrame untuk visualisasi
df_words = pd.DataFrame(word_counts.items(), columns=['Kata', 'Frekuensi']).sort_values(by='Frekuensi', ascending=False)

# 3. Tampilan Streamlit
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Top 10 Kata Terbanyak")
    # Menampilkan 10 kata teratas dalam bentuk Bar Chart
    st.bar_chart(df_words.head(10).set_index('Kata'))

with col2:
    st.subheader("☁️ Word Cloud")
    # Membuat Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

# Menampilkan Tabel Data
st.divider()
st.subheader("📋 Tabel Frekuensi Lengkap")
st.dataframe(df_words, use_container_width=True)