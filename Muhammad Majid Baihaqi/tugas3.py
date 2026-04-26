import streamlit as st

st.title("Visualisasi Operasi Set")

# Input user
set1_input = st.text_input("Masukkan Set A (pisahkan dengan koma)", "1,2,3")
set2_input = st.text_input("Masukkan Set B (pisahkan dengan koma)", "3,4,5")

# Ubah ke set
setA = set(set1_input.split(","))
setB = set(set2_input.split(","))

st.subheader("Hasil Operasi Set")

if st.button("Proses"):
    union = setA | setB
    intersection = setA & setB
    difference = setA - setB
    sym_diff = setA ^ setB

    st.write("Union:", union)
    st.write("Intersection:", intersection)
    st.write("Difference (A - B):", difference)
    st.write("Symmetric Difference:", sym_diff)