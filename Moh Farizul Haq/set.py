import streamlit as st

st.set_page_config(page_title="Operasi Himpunan", layout="wide")

st.title("🧮 Visualisasi Operasi Himpunan")
st.markdown("Aplikasi ini membantu memahami konsep dasar teori himpunan secara interaktif.")

# Input Section
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Himpunan A")
        input_a = st.text_area("Masukkan anggota (pisahkan dengan koma):", "A, B, C, D, E", key="a")
        set_a = set([x.strip() for x in input_a.split(",") if x.strip()])
        st.info(f"Isi A: `{set_a}`")

    with col2:
        st.subheader("Himpunan B")
        input_b = st.text_area("Masukkan anggota (pisahkan dengan koma):", "D, E, F, G", key="b")
        set_b = set([x.strip() for x in input_b.split(",") if x.strip()])
        st.success(f"Isi B: `{set_b}`")

st.divider()

# Operasi Section
st.subheader("Pilih Operasi Matematika")
ops = st.selectbox("Pilih Operasi:", 
                  ["Gabungan (Union)", "Irisan (Intersection)", "Selisih (Difference)", "Beda Setangkup (Symmetric Difference)"])

# Logika dan Penjelasan
if ops == "Gabungan (Union)":
    hasil = set_a.union(set_b)
    rumus = "A ∪ B = {x | x ∈ A atau x ∈ B}"
    penjelasan = "Menggabungkan semua anggota dari kedua himpunan tanpa duplikasi."
    warna = "blue"

elif ops == "Irisan (Intersection)":
    hasil = set_a.intersection(set_b)
    rumus = "A ∩ B = {x | x ∈ A dan x ∈ B}"
    penjelasan = "Hanya mengambil anggota yang ada di kedua himpunan sekaligus."
    warna = "green"

elif ops == "Selisih (Difference)":
    sub_ops = st.radio("Arah Selisih:", ["A - B", "B - A"], horizontal=True)
    if sub_ops == "A - B":
        hasil = set_a.difference(set_b)
        rumus = "A - B = {x | x ∈ A dan x ∉ B}"
        penjelasan = "Anggota yang ada di A tapi tidak dimiliki oleh B."
    else:
        hasil = set_b.difference(set_a)
        rumus = "B - A = {x | x ∈ B dan x ∉ A}"
        penjelasan = "Anggota yang ada di B tapi tidak dimiliki oleh A."
    warna = "orange"

else:
    hasil = set_a.symmetric_difference(set_b)
    rumus = "A Δ B = (A - B) ∪ (B - A)"
    penjelasan = "Semua anggota A dan B kecuali irisan mereka."
    warna = "red"

# Menampilkan Hasil
st.markdown(f"### 📝 Rumus: `{rumus}`")
st.write(penjelasan)

# Layout Hasil dengan Metric
res_col1, res_col2 = st.columns([3, 1])
with res_col1:
    st.code(f"Hasil Akhir: {hasil if hasil else 'Himpunan Kosong (∅)'}", language="python")

with res_col2:
    st.metric("Jumlah Anggota", len(hasil))

# Footer
st.markdown("---")
st.caption("Struktur Data - Visualisasi Himpunan Interaktif")