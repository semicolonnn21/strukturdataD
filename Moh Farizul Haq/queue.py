import streamlit as st

class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        self.log = []

    def enqueue(self, value):
        if ((self.tail + 1) % self.k == self.head):
            self.log.append(f"❌ Gagal: Antrian Penuh saat mau input '{value}'")
            return False
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
        self.log.append(f"✅ Enqueue: '{value}' masuk di Index {self.tail}")
        return True

    def dequeue(self):
        if (self.head == -1):
            self.log.append("❌ Gagal: Antrian Kosong!")
            return None
        
        removed_val = self.queue[self.head]
        self.queue[self.head] = None
        
        if (self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
            
        self.log.append(f"🗑️ Dequeue: '{removed_val}' keluar")
        return removed_val

# Inisialisasi Session State
if 'cq' not in st.session_state:
    st.session_state.cq = CircularQueue(6)

st.set_page_config(page_title="Circular Queue", layout="wide")
st.title("🔄 Circular Queue Visualizer")

# Layout Utama
col_control, col_viz = st.columns([1, 2])

with col_control:
    st.subheader("⚙️ Kontrol Antrian")
    new_val = st.text_input("Data Baru:", placeholder="Contoh: A atau 10")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Enqueue", use_container_width=True):
            if new_val:
                st.session_state.cq.enqueue(new_val)
            else:
                st.warning("Isi data dulu!")
    with c2:
        if st.button("Dequeue", use_container_width=True):
            st.session_state.cq.dequeue()

    st.markdown("---")
    st.subheader("📜 Log Aktivitas")
    for line in reversed(st.session_state.cq.log[-5:]): # Tampilkan 5 log terakhir
        st.write(line)

with col_viz:
    st.subheader("📍 Visualisasi Memori")
    
    # Membuat grid melingkar sederhana (3 kolom x 2 baris untuk 6 slot)
    q_size = st.session_state.cq.k
    data = st.session_state.cq.queue
    head = st.session_state.cq.head
    tail = st.session_state.cq.tail
    
    cols = st.columns(q_size)
    for i in range(q_size):
        with cols[i]:
            # Penanda Head & Tail
            pointers = []
            if i == head: pointers.append("🟢 HEAD")
            if i == tail: pointers.append("🔴 TAIL")
            
            # Warna Box
            bg_color = "#2e3136" if data[i] is None else "#0e6251"
            border_color = "#f1c40f" if (i == head or i == tail) else "#566573"
            
            st.markdown(f"""
                <div style="
                    border: 3px solid {border_color};
                    background-color: {bg_color};
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    min-height: 80px;
                ">
                    <h3 style="margin:0; color:white;">{data[i] if data[i] is not None else "-"}</h3>
                    <small style="color:#bdc3c7;">Index {i}</small>
                </div>
                <div style="text-align:center; margin-top:5px; font-size:12px; font-weight:bold;">
                    {"<br>".join(pointers)}
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.info("""
    **Prinsip Kerja V2:**
    - Jika `Tail` mencapai batas akhir, ia akan kembali ke `Index 0` (Wrap-around).
    - `Head` adalah pintu keluar, `Tail` adalah pintu masuk.
    """)

# Tombol Reset
if st.sidebar.button("Reset Antrian"):
    st.session_state.cq = CircularQueue(6)
    st.rerun()