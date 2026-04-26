import streamlit as st

st.title("🔄 Pro Circular Queue Simulator")

if 'queue' not in st.session_state:
    st.session_state.q_list = [None] * 5
    st.session_state.head = -1
    st.session_state.tail = -1

size = 5

def enqueue(val):
    if ((st.session_state.tail + 1) % size == st.session_state.head):
        st.error("Queue Overlow! (Penuh)")
    elif st.session_state.head == -1:
        st.session_state.head = 0
        st.session_state.tail = 0
        st.session_state.q_list[st.session_state.tail] = val
    else:
        st.session_state.tail = (st.session_state.tail + 1) % size
        st.session_state.q_list[st.session_state.tail] = val

def dequeue():
    if st.session_state.head == -1:
        st.warning("Queue Underflow! (Kosong)")
    elif st.session_state.head == st.session_state.tail:
        st.session_state.q_list[st.session_state.head] = None
        st.session_state.head = -1
        st.session_state.tail = -1
    else:
        st.session_state.q_list[st.session_state.head] = None
        st.session_state.head = (st.session_state.head + 1) % size

# UI
val = st.text_input("Data:")
c1, c2, c3 = st.columns(3)
if c1.button("📥 Masuk (Enqueue)"): enqueue(val)
if c2.button("📤 Keluar (Dequeue)"): dequeue()
if c3.button("♻️ Reset"): 
    st.session_state.q_list = [None] * 5
    st.session_state.head, st.session_state.tail = -1, -1

# Visualisasi Memory
st.write("### RAM Preview:")
cols = st.columns(size)
for i in range(size):
    with cols[i]:
        is_head = "⬅️ H" if i == st.session_state.head else ""
        is_tail = "⬅️ T" if i == st.session_state.tail else ""
        color = "green" if st.session_state.q_list[i] else "gray"
        st.markdown(f"""
            <div style="background:{color}; padding:20px; border-radius:5px; text-align:center; color:white;">
            {st.session_state.q_list[i] if st.session_state.q_list[i] else '0'}
            </div>
            <div style="font-size:10px; text-align:center;">Idx {i}<br>{is_head}<br>{is_tail}</div>
        """, unsafe_allow_html=True)