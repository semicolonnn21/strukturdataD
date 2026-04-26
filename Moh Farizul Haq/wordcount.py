import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Word Count V2", layout="centered")

st.title("📝 Word Count Visualizer")
st.write("Menghitung frekuensi kata dan menampilkan grafik dengan Matplotlib.")

# Input Teks
user_text = st.text_area("Masukkan teks di sini:", "Struktur data sangat penting. Belajar struktur data itu seru!", height=200)

# Sidebar Pengaturan
st.sidebar.header("Filter")
min_freq = st.sidebar.slider("Minimal Muncul", 1, 5, 1)

if user_text:
    # Proses Teks (Case Folding & Split)
    words = user_text.lower().split()
    # Bersihkan tanda baca
    clean_words = [w.strip(".,!?:;\"()") for w in words if len(w) > 1]
    
    # Hitung Frekuensi
    word_freq = {}
    for word in clean_words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Filter berdasarkan minimal frekuensi
    filtered_freq = {k: v for k, v in word_freq.items() if v >= min_freq}
    
    if filtered_freq:
        # Urutkan data
        sorted_words = dict(sorted(filtered_freq.items(), key=lambda item: item[1], reverse=True)[:10])
        
        # Buat Plot Matplotlib
        fig, ax = plt.subplots()
        ax.bar(sorted_words.keys(), sorted_words.values(), color='skyblue')
        ax.set_xlabel('Kata')
        ax.set_ylabel('Frekuensi')
        ax.set_title('10 Kata Paling Sering Muncul')
        plt.xticks(rotation=45)

        # Tampilkan di Streamlit
        st.pyplot(fig)
        
        # Tampilkan Tabel juga
        st.subheader("Detail Data")
        df = pd.DataFrame(list(sorted_words.items()), columns=['Kata', 'Jumlah'])
        st.table(df)
    else:
        st.warning("Tidak ada kata yang memenuhi minimal frekuensi.")