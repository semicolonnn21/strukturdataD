import streamlit as st
import time

class Node:
    def __init__(self, warna, durasi):
        self.warna = warna
        self.durasi = durasi
        self.next = None

def inisialisasi_list():
    merah = Node("Merah", 40)
    kuning = Node("Kuning", 5)
    hijau = Node("Hijau", 20)

    merah.next = kuning
    kuning.next = hijau
    hijau.next = merah

    return merah

def main():
    st.title("🚦 Simulasi Lampu Lalu Lintas")
    st.write("Menggunakan Singly Circular Linked List")

    if "simpul_aktif" not in st.session_state:
        st.session_state.simpul_aktif = inisialisasi_list()
        st.session_state.waktu = st.session_state.simpul_aktif.durasi

    simpul = st.session_state.simpul_aktif

    if simpul.warna == "Merah":
        st.error(f"🔴 LAMPU {simpul.warna.upper()}")
    elif simpul.warna == "Kuning":
        st.warning(f"🟡 LAMPU {simpul.warna.upper()}")
    elif simpul.warna == "Hijau":
        st.success(f"🟢 LAMPU {simpul.warna.upper()}")

    st.metric("Sisa Waktu", f"{st.session_state.waktu} detik")

    if st.button("Reset Simulasi"):
        st.session_state.simpul_aktif = inisialisasi_list()
        st.session_state.waktu = st.session_state.simpul_aktif.durasi
        st.rerun()

    time.sleep(1)

    if st.session_state.waktu > 1:
        st.session_state.waktu -= 1
    else:
        st.session_state.simpul_aktif = simpul.next
        st.session_state.waktu = simpul.next.durasi

    st.rerun()

if __name__ == "__main__":
    main()