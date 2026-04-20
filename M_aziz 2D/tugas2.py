import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Antrian Rumah Hantu UINSSC", layout="wide")

# Inisialisasi State untuk Circular Queue
KAPASITAS = 8

if 'queue' not in st.session_state:
    st.session_state.queue = [None] * KAPASITAS
if 'head' not in st.session_state:
    st.session_state.head = -1
if 'tail' not in st.session_state:
    st.session_state.tail = -1

# Fungsi Operasi Circular Queue
def enqueue(nama):
    if ((st.session_state.tail + 1) % KAPASITAS == st.session_state.head):
        st.error("⚠️ Antrian Penuh! Tunggu pengunjung keluar.")
    else:
        if (st.session_state.head == -1):
            st.session_state.head = 0
        st.session_state.tail = (st.session_state.tail + 1) % KAPASITAS
        st.session_state.queue[st.session_state.tail] = nama
        st.success(f"✅ {nama} berhasil masuk antrian.")

def dequeue():
    if (st.session_state.head == -1):
        st.warning("📭 Antrian Kosong!")
    else:
        pengunjung = st.session_state.queue[st.session_state.head]
        st.session_state.queue[st.session_state.head] = None
        if (st.session_state.head == st.session_state.tail):
            st.session_state.head = -1
            st.session_state.tail = -1
        else:
            st.session_state.head = (st.session_state.head + 1) % KAPASITAS
        st.info(f"👻 {pengunjung} masuk ke dalam Rumah Hantu!")

# Antarmuka Pengguna (UI)
st.title("🎃 Visualisasi Circular Queue: Rumah Hantu")
st.write("Informatika UINSSC - MMXXVI")

# Sidebar untuk Kontrol
with st.sidebar:
    st.header("Kontrol Antrian")
    nama_baru = st.text_input("Nama Pengunjung")
    if st.button("Tambah ke Antrian (Enqueue)"):
        if nama_baru:
            enqueue(nama_baru)
        else:
            st.error("Masukkan nama!")
            
    if st.button("Masuk Wahana (Dequeue)"):
        dequeue()
    
    if st.button("Reset Antrian"):
        st.session_state.queue = [None] * KAPASITAS
        st.session_state.head = -1
        st.session_state.tail = -1
        st.rerun()

# Visualisasi Antrian
st.subheader("Status Slot Antrian (Circular)")
cols = st.columns(KAPASITAS)

for i in range(KAPASITAS):
    with cols[i]:
        # Logika Penentuan Warna dan Label
        is_head = (i == st.session_state.head)
        is_tail = (i == st.session_state.tail)
        isi = st.session_state.queue[i]
        
        # Styling Box
        bg_color = "#2e3136" # Default kosong
        border = "1px solid #555"
        
        if isi:
            bg_color = "#4e0d0d" # Terisi (Warna Merah Gelap)
            border = "2px solid #ff4b4b"
            
        label = ""
        if is_head and is_tail and st.session_state.head != -1:
            label = "🎯 Head & Tail"
        elif is_head:
            label = "🏁 Head"
        elif is_tail:
            label = "🐕 Tail"

        st.markdown(
            f"""
            <div style="
                background-color: {bg_color};
                border: {border};
                padding: 20px;
                text-align: center;
                border-radius: 10px;
                min-height: 120px;
            ">
                <small style="color: #aaa;">Slot {i}</small><br>
                <strong style="font-size: 18px;">{isi if isi else '-'}</strong><br>
                <span style="font-size: 12px; color: #00ff00;">{label}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# Informasi Teknis
st.divider()
st.json({
    "Head Index": st.session_state.head,
    "Tail Index": st.session_state.tail,
    "Full Array": st.session_state.queue
})