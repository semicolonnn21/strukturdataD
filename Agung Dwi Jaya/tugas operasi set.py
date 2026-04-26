import streamlit as st

# Input dua set
set_A = st.text_input("Masukkan elemen Set A (pisahkan dengan koma)", "1,2,3,4")
set_B = st.text_input("Masukkan elemen Set B (pisahkan dengan koma)", "3,4,5,6")

# Konversi ke tipe set
A = set(map(str.strip, set_A.split(",")))
B = set(map(str.strip, set_B.split(",")))

st.write("### Hasil Operasi Set")
st.write("Set A:", A)
st.write("Set B:", B)

# Operasi
st.write("Union:", A.union(B))
st.write("Intersection:", A.intersection(B))
st.write("Difference (A - B):", A.difference(B))
st.write("Difference (B - A):", B.difference(A))
st.write("Symmetric Difference:", A.symmetric_difference(B))
