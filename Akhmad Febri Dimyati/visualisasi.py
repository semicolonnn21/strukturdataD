import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Tugas 1: Operasi Set", page_icon="📊")

st.title("📊 Visualisasi Operasi Set (Himpunan)")
st.markdown("---")

# Input Himpunan dari User
col1, col2 = st.columns(2)

with col1:
    input_a = st.text_input("Masukkan Anggota Himpunan A (pisahkan dengan koma):", "1, 2, 3, 4, 5")
    # Ubah input string jadi set angka/huruf
    set_a = set([x.strip() for x in input_a.split(",") if x.strip()])

with col2:
    input_b = st.text_input("Masukkan Anggota Himpunan B (pisahkan dengan koma):", "4, 5, 6, 7, 8")
    set_b = set([x.strip() for x in input_b.split(",") if x.strip()])

st.write(f"**Himpunan A:** `{set_a if set_a else '{}'}`")
st.write(f"**Himpunan B:** `{set_b if set_b else '{}'}`")
st.markdown("---")

# Pilihan Operasi Set
operasi = st.radio(
    "Pilih Operasi yang Ingin Ditampilkan:",
    ("Union (Gabungan)", "Intersection (Irisan)", "Difference (Selisih)", "Symmetric Difference"),
    horizontal=True
)

# Logika Perhitungan
if operasi == "Union (Gabungan)":
    hasil = set_a.union(set_b)
    penjelasan = "Gabungan semua anggota A dan B (A ∪ B)"
    simbol = "A ∪ B"
    
elif operasi == "Intersection (Irisan)":
    hasil = set_a.intersection(set_b)
    penjelasan = "Anggota yang ada di A sekaligus ada di B (A ∩ B)"
    simbol = "A ∩ B"

elif operasi == "Difference (Selisih)":
    pilih_selisih = st.selectbox("Pilih Arah Selisih:", ["A - B", "B - A"])
    if pilih_selisih == "A - B":
        hasil = set_a.difference(set_b)
        penjelasan = "Anggota A yang tidak ada di B"
        simbol = "A - B"
    else:
        hasil = set_b.difference(set_a)
        penjelasan = "Anggota B yang tidak ada di A"
        simbol = "B - A"

else: # Symmetric Difference
    hasil = set_a.symmetric_difference(set_b)
    penjelasan = "Anggota A dan B, kecuali yang ada di keduanya (Irisan dibuang)"
    simbol = "A Δ B"

# Menampilkan Hasil
st.subheader(f"Hasil {operasi}")
st.info(f"**Keterangan:** {penjelasan}")

# Kotak hasil yang menonjol
st.success(f"**{simbol} =** `{hasil if hasil else 'set kosong / ∅'}`")

# Statistik Sederhana
st.write(f"Jumlah elemen hasil: **{len(hasil)}**")

st.markdown("---")
st.caption("Dibuat oleh: Akhmad Febri Dimyati")