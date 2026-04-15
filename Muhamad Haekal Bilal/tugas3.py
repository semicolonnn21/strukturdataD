import streamlit as st
import time

class Node:
    def _init_(self, warna, durasi, emoji):
        self.warna = warna
        self.durasi = durasi
        self.emoji = emoji 
        self.next = None

class CircularLinkedList:
    def _init_(self):
        self.head = None

    def tambah_lampu(self, warna, durasi, emoji):
        node_baru = Node(warna, durasi, emoji)
        
        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            temp.next = node_baru
            node_baru.next = self.head

st.title("Simulasi Lampu Lalu Lintas")
st.write("Menggunakan Circular Linked List")

if 'lampu_lalu_lintas' not in st.session_state:
    lampu = CircularLinkedList()
    lampu.tambah_lampu("MERAH", 40, "🔴")
    lampu.tambah_lampu("HIJAU", 20, "🟢")
    lampu.tambah_lampu("KUNING", 5, "🟡")
    st.session_state.lampu_lalu_lintas = lampu

tombol_mulai = st.button("Mulai Simulasi")

tempat_lampu = st.empty()
tempat_waktu = st.empty()

if tombol_mulai:
    bantu = st.session_state.lampu_lalu_lintas.head
    
   
    while True:
        
        tempat_lampu.markdown(f"## {bantu.emoji} Lampu {bantu.warna} Menyala!")
        
        for sisa in range(bantu.durasi, 0, -1):
            tempat_waktu.subheader(f"Sisa waktu: {sisa} detik")
            time.sleep(1) 

        bantu = bantu.next