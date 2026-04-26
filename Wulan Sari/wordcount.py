import streamlit as st
import pandas as pd

st.title("📊 Smart Word Processor")

text_input = st.text_area("Input Teks Panjang:", placeholder="Paste artikel atau jurnal di sini...")

if text_input:
    words = text_input.lower().split()
    clean_words = [w.strip(".,!?:;") for w in words]
    
    # Statistik Pro
    total_words = len(clean_words)
    unique_words = len(set(clean_words))
    avg_len = sum(len(w) for w in clean_words) / total_words if total_words > 0 else 0
    longest_word = max(clean_words, key=len) if clean_words else ""

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Kata", total_words)
    m2.metric("Kata Unik", unique_words)
    m3.metric("Rata-rata Huruf", f"{avg_len:.1f}")

    st.write(f"🚩 **Kata Terpanjang:** `{longest_word}` ({len(longest_word)} Huruf)")

    # Bar Chart Manual (Bawaan Streamlit)
    freq = {}
    for w in clean_words: freq[w] = freq.get(w, 0) + 1
    chart_data = pd.DataFrame(freq.items(), columns=["Kata", "Frekuensi"]).sort_values("Frekuensi", ascending=False).head(10)
    
    st.subheader("Top 10 Kata Terbanyak")
    st.bar_chart(chart_data.set_index("Kata"))