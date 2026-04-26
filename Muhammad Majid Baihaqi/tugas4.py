import streamlit as st

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            return "Antrean Penuh"
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
        return "Berhasil Menambah"

    def dequeue(self):
        if (self.front == -1):
            return "Antrean Kosong"
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp

# Antarmuka Streamlit
st.title("Visualisasi Circular Queue")

if 'cq' not in st.session_state:
    st.session_state.cq = CircularQueue(5)

nama = st.text_input("Nama Pasien:")
if st.button("Enqueue"):
    res = st.session_state.cq.enqueue(nama)
    st.write(res)

if st.button("Dequeue"):
    res = st.session_state.cq.dequeue()
    st.write(f"Pasien keluar: {res}")

# Menampilkan representasi visual melingkar
st.write("Isi Antrian Saat Ini:")
st.write(st.session_state.cq.queue)