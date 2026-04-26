import streamlit as st

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Queue penuh!"
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        return f"{value} ditambahkan."

    def dequeue(self):
        if self.front == -1:
            return "Queue kosong!"
        elif self.front == self.rear:
            val = self.queue[self.front]
            self.front = self.rear = -1
            return f"{val} dihapus."
        else:
            val = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return f"{val} dihapus."

    def display(self):
        if self.front == -1:
            return []
        elements = []
        i = self.front
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return elements

# Streamlit UI
st.title("Visualisasi Circular Queue")

queue_size = st.sidebar.number_input("Ukuran Queue", min_value=3, max_value=10, value=5)
cq = CircularQueue(queue_size)

if "cq" not in st.session_state:
    st.session_state.cq = CircularQueue(queue_size)

action = st.radio("Pilih Aksi", ["Enqueue", "Dequeue", "Tampilkan"])

if action == "Enqueue":
    val = st.text_input("Masukkan nilai:")
    if st.button("Tambahkan"):
        st.write(st.session_state.cq.enqueue(val))

elif action == "Dequeue":
    if st.button("Hapus"):
        st.write(st.session_state.cq.dequeue())

elif action == "Tampilkan":
    st.write("Isi Queue saat ini:")
    st.write(st.session_state.cq.display())
