import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Circular Queue",
    page_icon="🔁",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Fira+Code:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
.stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: #e0e0e0; }

.judul {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 700;
    color: #e94560;
    margin-bottom: 4px;
    text-shadow: 0 0 20px rgba(233,69,96,0.4);
}
.subjudul {
    text-align: center;
    font-family: 'Fira Code', monospace;
    font-size: 0.78rem;
    color: #a0a0c0;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

hr { border-color: #e9456030 !important; }

.stButton > button {
    font-family: 'Fira Code', monospace !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    width: 100% !important;
    transition: all 0.2s !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; }

label {
    font-family: 'Fira Code', monospace !important;
    font-size: 0.75rem !important;
    color: #a0a0c0 !important;
}

.stTextInput > div > div > input {
    background: #0d1b2a !important;
    border: 1px solid #e9456050 !important;
    color: #e0e0e0 !important;
    font-family: 'Fira Code', monospace !important;
    border-radius: 8px !important;
}

.kartu {
    background: rgba(13, 27, 42, 0.8);
    border: 1px solid #e9456030;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 10px;
    backdrop-filter: blur(10px);
}
.kartu-judul {
    font-family: 'Fira Code', monospace;
    font-size: 0.68rem;
    color: #e94560;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.elemen-chip {
    display: inline-block;
    background: #e9456020;
    border: 1px solid #e9456060;
    color: #e94560;
    font-family: 'Fira Code', monospace;
    font-size: 0.8rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    margin: 3px;
}
.elemen-chip.front {
    background: #00b4d820;
    border-color: #00b4d860;
    color: #00b4d8;
}
.elemen-chip.rear {
    background: #06d6a020;
    border-color: #06d6a060;
    color: #06d6a0;
}

.log-item {
    font-family: 'Fira Code', monospace;
    font-size: 0.78rem;
    padding: 6px 12px;
    border-radius: 6px;
    margin-bottom: 4px;
    background: #0d1b2a;
    border-left: 3px solid #e94560;
    color: #c0c0d0;
}
.log-ok   { border-left-color: #06d6a0 !important; }
.log-err  { border-left-color: #e94560 !important; }
.log-warn { border-left-color: #ffd166 !important; }
</style>
""", unsafe_allow_html=True)


# ── Circular Queue ────────────────────────────────────────────────────────────
class CircularQueue:
    def __init__(self, cap):
        self.cap   = cap
        self.data  = [None] * cap
        self.front = -1
        self.rear  = -1
        self.size  = 0

    def is_empty(self): return self.size == 0
    def is_full(self):  return self.size == self.cap

    def enqueue(self, val):
        if self.is_full():
            return False, f"Queue penuh! ({self.cap}/{self.cap})"
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.cap  # wrap-around
        self.data[self.rear] = val
        self.size += 1
        return True, f"Enqueue '{val}' → indeks [{self.rear}]"

    def dequeue(self):
        if self.is_empty():
            return False, "Queue kosong!", None
        val = self.data[self.front]
        self.data[self.front] = None
        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.cap  # wrap-around
        self.size -= 1
        return True, f"Dequeue '{val}' dari indeks [{self.front if self.front != -1 else (self.front+self.cap)%self.cap}]", val


# ── Draw ──────────────────────────────────────────────────────────────────────
def draw_cq(cq: CircularQueue):
    n      = cq.cap
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#1a1a2e")

    R_OUT, R_IN = 1.0, 0.52
    angles = [2 * np.pi * i / n - np.pi / 2 for i in range(n)]

    COLOR_EMPTY    = "#0d1b2a"
    COLOR_FILLED   = "#533483"
    COLOR_FRONT    = "#00b4d8"
    COLOR_REAR     = "#06d6a0"
    COLOR_BOTH     = "#e94560"

    for i in range(n):
        a0 = angles[i] - np.pi / n + 0.04
        a1 = angles[i] + np.pi / n - 0.04
        theta = np.linspace(a0, a1, 40)

        xo = R_OUT * np.cos(theta)
        yo = R_OUT * np.sin(theta)
        xi = R_IN  * np.cos(theta[::-1])
        yi = R_IN  * np.sin(theta[::-1])

        if cq.data[i] is not None:
            if i == cq.front and i == cq.rear: c = COLOR_BOTH
            elif i == cq.front:                c = COLOR_FRONT
            elif i == cq.rear:                 c = COLOR_REAR
            else:                              c = COLOR_FILLED
        else:
            c = COLOR_EMPTY

        ax.fill(np.concatenate([xo, xi]),
                np.concatenate([yo, yi]),
                color=c, alpha=0.85, zorder=2)
        ax.plot(np.concatenate([xo, xi[::-1], [xo[0]]]),
                np.concatenate([yo, yi[::-1], [yo[0]]]),
                color="#1a1a2e", lw=2, zorder=3)

        mid = angles[i]
        # Indeks (luar)
        ax.text(1.18 * np.cos(mid), 1.18 * np.sin(mid), str(i),
                ha="center", va="center", fontsize=8,
                color="#606080", fontfamily="monospace", zorder=4)

        # Nilai (dalam)
        vx, vy = 0.75 * np.cos(mid), 0.75 * np.sin(mid)
        val = cq.data[i]
        ax.text(vx, vy,
                str(val) if val is not None else "·",
                ha="center", va="center", fontsize=10, fontweight="bold",
                color="#ffffff" if val else "#2a2a4a",
                fontfamily="monospace", zorder=4)

        # Label F/R
        lbl = ""
        if i == cq.front and i == cq.rear: lbl = "F/R"
        elif i == cq.front:                lbl = "F"
        elif i == cq.rear:                 lbl = "R"
        if lbl:
            ax.text(1.36 * np.cos(mid), 1.36 * np.sin(mid), lbl,
                    ha="center", va="center", fontsize=7, fontweight="bold",
                    color="#ffd166", fontfamily="monospace", zorder=5)

    # Lingkaran tengah
    circle = plt.Circle((0, 0), R_IN - 0.02, color="#0d1b2a", zorder=1)
    ax.add_patch(circle)
    ax.text(0, 0.08, f"{cq.size}/{cq.cap}",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color="#e94560", fontfamily="monospace", zorder=4)
    ax.text(0, -0.12, "ISI/MAX",
            ha="center", va="center", fontsize=7,
            color="#606080", fontfamily="monospace", zorder=4)

    # Panah wrap-around
    theta_arrow = np.linspace(0.1, 2 * np.pi - 0.1, 100)
    ax.plot(1.52 * np.cos(theta_arrow), 1.52 * np.sin(theta_arrow),
            color="#e9456030", lw=1.5, linestyle="--", zorder=1)
    ax.annotate("", xy=(1.52 * np.cos(0.05), 1.52 * np.sin(0.05)),
                xytext=(1.52 * np.cos(0.2), 1.52 * np.sin(0.2)),
                arrowprops=dict(arrowstyle="->", color="#e9456060", lw=1.5))

    # Legend
    legend = [
        mpatches.Patch(color=COLOR_FRONT,  label="Front (F)"),
        mpatches.Patch(color=COLOR_REAR,   label="Rear (R)"),
        mpatches.Patch(color=COLOR_BOTH,   label="F & R"),
        mpatches.Patch(color=COLOR_FILLED, label="Terisi"),
        mpatches.Patch(color=COLOR_EMPTY,  label="Kosong"),
    ]
    ax.legend(handles=legend, loc="lower center",
              bbox_to_anchor=(0.5, -0.1), ncol=5,
              frameon=False, fontsize=7, labelcolor="#a0a0c0")

    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    return fig


# ── Session ───────────────────────────────────────────────────────────────────
if "cq"  not in st.session_state: st.session_state.cq  = CircularQueue(8)
if "log" not in st.session_state: st.session_state.log = []
cq = st.session_state.cq

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown('<div class="judul">🔁 Circular Queue</div>', unsafe_allow_html=True)
st.markdown('<div class="subjudul">WRAP-AROUND · ELEMEN TERAKHIR → AWAL</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Diagram
fig = draw_cq(cq)
st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.markdown("<hr>", unsafe_allow_html=True)

# Kontrol
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    val = st.text_input("Nilai", placeholder="Masukkan nilai...", label_visibility="collapsed")
with c2:
    if st.button("➕ Enqueue"):
        if val.strip():
            ok, msg = cq.enqueue(val.strip())
            st.session_state.log.append(("ok" if ok else "err", msg))
            st.rerun()
        else:
            st.session_state.log.append(("warn", "Masukkan nilai dulu!"))
            st.rerun()
with c3:
    if st.button("➖ Dequeue"):
        ok, msg, _ = cq.dequeue()
        st.session_state.log.append(("ok" if ok else "err", msg))
        st.rerun()

cap_baru = st.slider("Kapasitas", 4, 12, cq.cap)
if cap_baru != cq.cap:
    st.session_state.cq  = CircularQueue(cap_baru)
    st.session_state.log = []
    st.rerun()

col_reset = st.columns([3, 1])
with col_reset[1]:
    if st.button("🔄 Reset"):
        st.session_state.cq  = CircularQueue(cq.cap)
        st.session_state.log = []
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# Info
ka, kb, kc, kd = st.columns(4)
ka.metric("Size",  f"{cq.size}/{cq.cap}")
kb.metric("Front", cq.front if cq.front != -1 else "-")
kc.metric("Rear",  cq.rear  if cq.rear  != -1 else "-")
kd.metric("Status", "PENUH" if cq.is_full() else ("KOSONG" if cq.is_empty() else "AKTIF"))

# Isi queue
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="kartu"><div class="kartu-judul">Isi Queue (Front → Rear)</div>', unsafe_allow_html=True)
if not cq.is_empty():
    chips = ""
    for i in range(cq.size):
        idx = (cq.front + i) % cq.cap
        cls = "front" if i == 0 else ("rear" if i == cq.size - 1 else "")
        chips += f'<span class="elemen-chip {cls}">[{idx}] {cq.data[idx]}</span>'
        if i < cq.size - 1:
            chips += ' <span style="color:#e9456060;">→</span> '
    st.markdown(chips + "</div>", unsafe_allow_html=True)
else:
    st.markdown('<span style="color:#606080;font-family:\'Fira Code\',monospace;font-size:0.85rem;">— Queue kosong —</span></div>', unsafe_allow_html=True)

# Log
if st.session_state.log:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="kartu-judul" style="color:#e94560;font-family:\'Fira Code\',monospace;font-size:0.68rem;letter-spacing:2px;">LOG OPERASI</div>', unsafe_allow_html=True)
    for status, msg in reversed(st.session_state.log[-5:]):
        cls = f"log-{status}"
        st.markdown(f'<div class="log-item {cls}">› {msg}</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;font-family:\'Fira Code\',monospace;font-size:0.65rem;color:#3a3a55;">CIRCULAR QUEUE VISUALIZER · STREAMLIT</p>', unsafe_allow_html=True)