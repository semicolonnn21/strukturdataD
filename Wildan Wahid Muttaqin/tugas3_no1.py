import streamlit as st

st.title("Visualisasi Operasi Set")

# Input dari user
set1_input = st.text_input("Masukkan elemen Set A (pisahkan dengan koma)", "1,2,3,4")
set2_input = st.text_input("Masukkan elemen Set B (pisahkan dengan koma)", "3,4,5,6")

# Konversi ke set
setA = set(set1_input.split(","))
setB = set(set2_input.split(","))

st.subheader("Hasil Operasi")

# Union
union = setA | setB
st.write("Union (A ∪ B):", union)

# Intersection
intersection = setA & setB
st.write("Intersection (A ∩ B):", intersection)

# Difference
difference_AB = setA - setB
difference_BA = setB - setA
st.write("Difference (A - B):", difference_AB)
st.write("Difference (B - A):", difference_BA)

# Symmetric Difference
sym_diff = setA ^ setB
st.write("Symmetric Difference (A Δ B):", sym_diff)