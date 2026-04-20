import streamlit as st

# Pengaturan Judul Halaman
st.set_page_config(page_title="Tugas Mandiri Struktur Data", layout="wide")

st.title("Tugas Mandiri: Set & Dictionary")
st.write("Presented by: Informatika UINSSC 2026")

# Membuat Tab untuk memisahkan Tugas 1 dan Tugas 2
tab1, tab2 = st.tabs(["1. Visualisasi Operasi Set", "2. Word Count Dictionary"])

# --- TUGAS 1: OPERASI SET ---
with tab1:
    st.header("Visualisasi Operasi Set")
    st.write("Masukkan angka dipisahkan dengan koma (contoh: 1,2,3,4,5)")

    col1, col2 = st.columns(2)
    with col1:
        input_a = st.text_input("Set A", "1, 2, 3, 4, 5")
    with col2:
        input_b = st.text_input("Set B", "4, 5, 6, 7, 8")

    # Proses Input String ke Set
    try:
        set_a = set(map(int, input_a.split(','))) if input_a else set()
        set_b = set(map(int, input_b.split(','))) if input_b else set()

        st.divider()
        
        # Operasi Set
        res_union = set_a | set_b
        res_inter = set_a & set_b
        res_diff = set_a - set_b
        res_symm = set_a ^ set_b

        # Tampilan Hasil
        c1, c2 = st.columns(2)
        c1.success(f"**Union (A ∪ B):** \n\n {res_union}")
        c2.info(f"**Intersection (A ∩ B):** \n\n {res_inter}")
        
        c3, c4 = st.columns(2)
        c3.warning(f"**Difference (A - B):** \n\n {res_diff}")
        c4.error(f"**Symmetric Difference (A Δ B):** \n\n {res_symm}")

    except ValueError:
        st.error("Mohon masukkan angka saja, dipisahkan dengan koma.")

# --- TUGAS 2: WORD COUNT DICTIONARY ---
with tab2:
    st.header("Word Count Komentar Sosial Media")
    
    komentar = st.text_area("Masukkan komentar di sini:", 
                           "Struktur data sangat seru! Belajar struktur data di Informatika UINSSC sangat menyenangkan.")

    if st.button("Hitung Frekuensi Kata"):
        if komentar:
            # Membersihkan teks (lowercase dan hapus tanda baca sederhana)
            clean_text = komentar.lower().replace('.', '').replace(',', '').replace('!', '')
            daftar_kata = clean_text.split()

            # Implementasi Dictionary untuk Word Count
            word_count = {}
            for kata in daftar_kata:
                if kata in word_count:
                    word_count[kata] += 1
                else:
                    word_count[kata] = 1

            # Visualisasi
            st.subheader("Hasil Perhitungan (Dictionary)")
            st.write(word_count)

            # Visualisasi dengan Bar Chart
            st.subheader("Visualisasi Grafik")
            st.bar_chart(word_count)
        else:
            st.warning("Silakan masukkan teks terlebih dahulu.")

st.sidebar.info("Gunakan aplikasi ini untuk menyelesaikan Tugas Mandiri Struktur Data.")