import streamlit as st
import time

# =============================================
# CIRCULAR LINKED LIST IMPLEMENTATION
# =============================================

class Node:
    """Node dalam Circular Linked List"""
    def __init__(self, color: str, duration: int, label: str):
        self.color = color        # nama warna
        self.duration = duration  # durasi dalam detik
        self.label = label        # label tampilan
        self.next = None          # pointer ke node berikutnya


class CircularLinkedList:
    """Circular Linked List untuk siklus lampu lalu lintas"""
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, color: str, duration: int, label: str):
        new_node = Node(color, duration, label)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # circular: tunjuk ke diri sendiri
            self.current = self.head
        else:
            # Cari node terakhir (yang next-nya head)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # tutup lingkaran

    def get_current(self) -> Node:
        return self.current

    def next_state(self):
        """Pindah ke node berikutnya (circular)"""
        self.current = self.current.next

    def get_all_nodes(self) -> list:
        """Kembalikan semua node sebagai list"""
        nodes = []
        temp = self.head
        while True:
            nodes.append(temp)
            temp = temp.next
            if temp == self.head:
                break
        return nodes


# =============================================
# INISIALISASI CIRCULAR LINKED LIST
# =============================================

def init_traffic_light() -> CircularLinkedList:
    cll = CircularLinkedList()
    cll.append("red",    40, "MERAH")   # 40 detik
    cll.append("green",  20, "HIJAU")   # 20 detik
    cll.append("yellow",  5, "KUNING")  #  5 detik
    return cll


# =============================================
# STREAMLIT APP
# =============================================

st.set_page_config(
    page_title="Lampu Lalu Lintas - Circular Linked List",
    page_icon="🚦",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@300;500;700&display=swap');

    .main { background-color: #0f0f0f; }
    .stApp { background-color: #111; color: #eee; }

    .title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        color: #fff;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        letter-spacing: 0.1em;
    }
    .light-box {
        background: #1a1a1a;
        border: 2px solid #333;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 0 auto;
        max-width: 320px;
        box-shadow: 0 0 40px rgba(0,0,0,0.5);
    }
    .light-circle {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 15px auto;
        border: 4px solid #2a2a2a;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .node-box {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        background: #1a1a1a;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 8px 12px;
        margin: 4px;
        display: inline-block;
        color: #aaa;
    }
    .node-active {
        border-color: #fff;
        color: #fff;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# STATE MANAGEMENT
# =============================================

if "cll" not in st.session_state:
    st.session_state.cll = init_traffic_light()

if "time_left" not in st.session_state:
    st.session_state.time_left = st.session_state.cll.get_current().duration

if "running" not in st.session_state:
    st.session_state.running = False

if "cycle_count" not in st.session_state:
    st.session_state.cycle_count = 0

cll: CircularLinkedList = st.session_state.cll
current_node = cll.get_current()

# =============================================
# HEADER
# =============================================

st.markdown('<div class="title">🚦 Lampu Lalu Lintas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">STRUKTUR DATA · CIRCULAR LINKED LIST · INFORMATIKA UINSSC MMXXVI</div>', unsafe_allow_html=True)

# =============================================
# TRAFFIC LIGHT DISPLAY
# =============================================

color_map = {
    "red":    {"hex": "#ff2020", "glow": "rgba(255,32,32,0.6)",   "off": "#3a1010"},
    "green":  {"hex": "#20ff60", "glow": "rgba(32,255,96,0.6)",   "off": "#103a18"},
    "yellow": {"hex": "#ffdd00", "glow": "rgba(255,221,0,0.6)",   "off": "#3a3010"},
}

light_placeholder = st.empty()
timer_placeholder = st.empty()

def render_light(node: Node, time_left: int):
    c = color_map[node.color]
    total = node.duration
    pct = (time_left / total) * 100

    # Warna lampu: aktif atau mati
    r_style = f'background:{color_map["red"]["hex"]};box-shadow:0 0 40px {color_map["red"]["glow"]};' if node.color == "red" else f'background:{color_map["red"]["off"]};'
    g_style = f'background:{color_map["green"]["hex"]};box-shadow:0 0 40px {color_map["green"]["glow"]};' if node.color == "green" else f'background:{color_map["green"]["off"]};'
    y_style = f'background:{color_map["yellow"]["hex"]};box-shadow:0 0 40px {color_map["yellow"]["glow"]};' if node.color == "yellow" else f'background:{color_map["yellow"]["off"]};'

    html = f"""
    <div class="light-box">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:1.4rem;font-weight:700;color:{c['hex']};margin-bottom:8px;">
            {node.label}
        </div>
        <div class="light-circle" style="{r_style}"></div>
        <div class="light-circle" style="{y_style}"></div>
        <div class="light-circle" style="{g_style}"></div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:3rem;font-weight:700;color:#fff;margin-top:16px;">
            {time_left:02d}
        </div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#555;margin-top:4px;">
            DETIK TERSISA
        </div>
        <div style="background:#222;border-radius:10px;height:8px;margin:16px 8px 8px;overflow:hidden;">
            <div style="height:100%;width:{pct:.1f}%;background:{c['hex']};border-radius:10px;transition:width 0.5s linear;"></div>
        </div>
    </div>
    """
    return html

# =============================================
# CIRCULAR LINKED LIST VISUALIZATION
# =============================================

def render_cll(cll: CircularLinkedList, current: Node):
    nodes = cll.get_all_nodes()
    icons = {"red": "🔴", "green": "🟢", "yellow": "🟡"}
    parts = []
    for i, node in enumerate(nodes):
        is_active = (node == current)
        cls = "node-box node-active" if is_active else "node-box"
        parts.append(f'<span class="{cls}">{icons[node.color]} {node.label} ({node.duration}s)</span>')
        if i < len(nodes) - 1:
            parts.append('<span style="color:#555;font-family:monospace;font-size:1rem;"> → </span>')
    # Tutup lingkaran
    parts.append('<span style="color:#555;font-family:monospace;"> ↩ (circular)</span>')
    return f'<div style="text-align:center;margin:20px 0;">{"".join(parts)}</div>'

# =============================================
# CONTROLS
# =============================================

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("▶ Mulai" if not st.session_state.running else "⏸ Pause", use_container_width=True):
        st.session_state.running = not st.session_state.running

with col2:
    if st.button("⏭ Skip", use_container_width=True):
        cll.next_state()
        st.session_state.time_left = cll.get_current().duration
        st.session_state.cycle_count += 1
        st.rerun()

with col3:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.cll = init_traffic_light()
        st.session_state.time_left = 40
        st.session_state.running = False
        st.session_state.cycle_count = 0
        st.rerun()

# =============================================
# RENDER CURRENT STATE
# =============================================

current_node = cll.get_current()
light_placeholder.markdown(render_light(current_node, st.session_state.time_left), unsafe_allow_html=True)

# CLL Visualization
st.markdown(render_cll(cll, current_node), unsafe_allow_html=True)

# Info stats
col_a, col_b = st.columns(2)
with col_a:
    st.metric("Siklus ke-", st.session_state.cycle_count + 1)
with col_b:
    st.metric("Total durasi siklus", "65 detik")

# =============================================
# COUNTDOWN LOGIC (Auto-refresh setiap 1 detik)
# =============================================

if st.session_state.running:
    time.sleep(1)
    st.session_state.time_left -= 1

    if st.session_state.time_left <= 0:
        # Pindah ke node berikutnya dalam circular linked list
        cll.next_state()
        st.session_state.time_left = cll.get_current().duration
        st.session_state.cycle_count += 1

    st.rerun()