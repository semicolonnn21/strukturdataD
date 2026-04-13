import streamlit as st
import time

# --- STRUKTUR DATA (Sesuai Materi Linked List) ---

class Node:
    def __init__(self, warna, pesan, durasi):
        self.warna = warna
        self.pesan = pesan
        self.durasi = durasi
        self.next = None  # Ini 'pointer' ke data selanjutnya

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_lampu(self, warna, pesan, durasi):
        new_node = Node(warna, pesan, durasi)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Nunjuk ke diri sendiri (Circular)
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head # Ekor nunjuk ke Kepala lagi

# --- SETUP STREAMLIT ---
st.set_page_config(page_title="Lampu Merah Linked List", page_icon="🚦")
st.title("🚦 Simulasi Lampu Merah ")

# Fungsi buat gambar lampu (biar keren dikit pakai CSS)
def draw_light(color):
    red = "#FF0000" if color == "merah" else "#330000"
    yellow = "#FFFF00" if color == "kuning" else "#333300"
    green = "#00FF00" if color == "hijau" else "#003300"
    
    return f"""
    <div style="background-color: #222; padding: 20px; border-radius: 40px; width: 100px; display: flex; flex-direction: column; align-items: center; gap: 10px; border: 4px solid #444;">
        <div style="width: 60px; height: 60px; background-color: {red}; border-radius: 50%;"></div>
        <div style="width: 60px; height: 60px; background-color: {yellow}; border-radius: 50%;"></div>
        <div style="width: 60px; height: 60px; background-color: {green}; border-radius: 50%;"></div>
    </div>
    """

# --- INISIALISASI DATA ---
# Kita buat urutan: Merah -> Kuning -> Hijau -> Kuning (lalu balik ke Merah)
traffic_system = CircularLinkedList()
traffic_system.tambah_lampu("merah", "BERHENTI!", 40)
traffic_system.tambah_lampu("kuning", "SIAP-SIAP!", 5)
traffic_system.tambah_lampu("hijau", "JALAN!", 20)
traffic_system.tambah_lampu("kuning", "PELAN-PELAN!", 5)

# --- JALANKAN SIMULASI ---
placeholder = st.empty()
current_node = traffic_system.head

try:
    while True:
        with placeholder.container():
            st.markdown(draw_light(current_node.warna), unsafe_allow_html=True)
            
            # Menampilkan pesan sesuai warna
            if current_node.warna == "merah":
                st.error(f"{current_node.pesan} ({current_node.durasi} detik)")
            elif current_node.warna == "kuning":
                st.warning(f"{current_node.pesan} ({current_node.durasi} detik)")
            else:
                st.success(f"{current_node.pesan} ({current_node.durasi} detik)")
        
        time.sleep(current_node.durasi)
        
        # PINDAH KE NODE BERIKUTNYA (Inilah inti dari Linked List)
        current_node = current_node.next

except KeyboardInterrupt:
    st.write("Selesai.")