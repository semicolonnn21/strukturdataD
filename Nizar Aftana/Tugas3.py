import streamlit as st

st.title("Visualisasi Operasi Set")

# Input user
set1_input = st.text_input("Masukkan elemen Set A (pisahkan dengan koma)", "1,2,3,4")
set2_input = st.text_input("Masukkan elemen Set B (pisahkan dengan koma)", "3,4,5,6")

# Konversi ke set
setA = set(map(int, set1_input.split(",")))
setB = set(map(int, set2_input.split(",")))

st.subheader("Hasil Operasi")

# Operasi Set
union = setA | setB
intersection = setA & setB
difference = setA - setB
sym_diff = setA ^ setB

st.write("Union (A ∪ B):", union)
st.write("Intersection (A ∩ B):", intersection)
st.write("Difference (A - B):", difference)
st.write("Symmetric Difference (A ⊕ B):", sym_diff)