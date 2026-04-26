import streamlit as st

# Nama: Muhamad Haekal Bilal 
# Tugas Struktur Data: Set & Dictionary

st.title("Manchester United Analysis Center")

#1 : SET 
st.header("1. Skuad Analysis (Set)")

skuad_inti = {"Lammens", "Dalot", "Mainoo", "Bruno", "Cunha", "Sesko", "Mbeumo"}
pemain_cedera = {"Shaw", "Malacia", "Yoro", "Maguire"}

st.write(f"Pemain Inti: {skuad_inti}")
st.write(f"Daftar Cedera: {pemain_cedera}")

pilihan = st.selectbox("Cek Status Pemain:", ["Pemain Siap Tanding", "Pemain Utama yang Cedera", "Total Semua Pemain"])

if pilihan == "Pemain Siap Tanding":
    hasil = skuad_inti - pemain_cedera
    st.success(f"Daftar Pemain: {hasil}")
elif pilihan == "Pemain Utama yang Cedera":
    hasil = skuad_inti & pemain_cedera
    st.warning(f"Daftar Pemain: {hasil}")
else:
    hasil = skuad_inti | pemain_cedera
    st.info(f"Total Semua Pemain: {hasil}")

st.divider()

#2: DICTIONARY 
st.header("2. Fans Comment Analyzer (Dictionary)")

komentar = st.text_area("Masukkan Komentar Fans MU:", "GGMU! United menang, GGMU!")

if st.button("Hitung Kata"):
    kata_kata = komentar.lower().replace("!", "").replace(".", "").split()
    counts = {}
    
    for k in kata_kata:
        counts[k] = counts.get(k, 0) + 1
    
    st.write("Statistik Kata (Format Dictionary):")
    st.json(counts)