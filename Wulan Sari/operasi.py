import streamlit as st
import pandas as pd

st.set_page_config(page_title="Set Operation", layout="wide")
st.title("🛡️ Ultimate Set Analyzer")

col1, col2 = st.columns(2)
with col1:
    set_a = set(st.text_input("Himpunan A (Koma sebagai pemisah):", "Python, Java, C++").split(","))
with col2:
    set_b = set(st.text_input("Himpunan B (Koma sebagai pemisah):", "C++, PHP, Ruby").split(","))

# Membersihkan spasi kosong
set_a = {x.strip() for x in set_a if x.strip()}
set_b = {x.strip() for x in set_b if x.strip()}

st.divider()

selected_op = st.radio("Pilih Operasi:", ["Union", "Intersection", "Difference (A-B)", "Symmetric Difference"], horizontal=True)

if selected_op == "Union":
    res = set_a | set_b
    desc = "Gabungan: Semua elemen unik dari A dan B."
elif selected_op == "Intersection":
    res = set_a & set_b
    desc = "Irisan: Elemen yang ada di A DAN B."
elif selected_op == "Difference (A-B)":
    res = set_a - set_b
    desc = "Selisih: Elemen di A yang TIDAK ADA di B."
else:
    res = set_a ^ set_b
    desc = "Beda Setangkup: Elemen yang hanya ada di salah satu himpunan (bukan keduanya)."

# Visual Card
c1, c2, c3 = st.columns(3)
c1.metric("Ukuran A", len(set_a))
c2.metric("Ukuran B", len(set_b))
c3.metric(f"Hasil {selected_op}", len(res))

st.success(f"**Hasil:** `{res if res else 'Set Kosong'}`")
st.caption(desc)

# Download Button
df_res = pd.DataFrame(list(res), columns=["Elemen Hasil"])
st.download_button("📩 Download Hasil (CSV)", df_res.to_csv(index=False), "hasil_set.csv")