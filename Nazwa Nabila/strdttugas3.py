import streamlit as st
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

st.title("Visualisasi Operasi Set")

# Input dari pengguna
col1, col2 = st.columns(2)
with col1:
    set_a_input = st.text_input("Elemen Set A (pisahkan dengan koma)", "1, 2, 3, 4, 5")
with col2:
    set_b_input = st.text_input("Elemen Set B (pisahkan dengan koma)", "4, 5, 6, 7, 8")

# Konversi input menjadi set
set_a = set([x.strip() for x in set_a_input.split(",")])
set_b = set([x.strip() for x in set_b_input.split(",")])

# Pilihan Operasi
operasi = st.selectbox("Pilih Operasi Set:", 
                      ["Union", "Intersection", "Difference (A-B)", "Symmetric Difference"])

# Logika Operasi
if operasi == "Union":
    hasil = set_a.union(set_b)
    label = "A ∪ B"
elif operasi == "Intersection":
    hasil = set_a.intersection(set_b)
    label = "A ∩ B"
elif operasi == "Difference (A-B)":
    hasil = set_a.difference(set_b)
    label = "A - B"
else:
    hasil = set_a.symmetric_difference(set_b)
    label = "A Δ B"

# Tampilkan Hasil Teks
st.write(f"**Hasil {label}:** {hasil}")

# Visualisasi dengan Diagram Venn
fig, ax = plt.subplots()
v = venn2([set_a, set_b], set_labels=('Set A', 'Set B'))
plt.title(f"Visualisasi {operasi}")
st.pyplot(fig)