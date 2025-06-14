import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Anggaran", layout="wide")

st.title("📊 Dashboard Anggaran & Realisasi")
st.write("Upload data anggaran dan realisasi, lalu lihat visualisasinya!")

# Upload file Excel
uploaded_file = st.file_uploader("Upload File Excel (format: kode_kegiatan, anggaran, realisasi)", type=["xlsx"])

if uploaded_file:
    # Baca data
    df = pd.read_excel(uploaded_file)

    # Validasi kolom
    expected_cols = ["kode_kegiatan", "nama_kegiatan", "anggaran", "realisasi"]
    if not all(col in df.columns for col in expected_cols):
        st.error("Kolom tidak sesuai. Harus ada: kode_kegiatan, nama_kegiatan, anggaran, realisasi")
    else:
        # Hitung persentase realisasi
        df["persentase"] = (df["realisasi"] / df["anggaran"] * 100).round(2)

        # Tampilkan tabel
        st.subheader("📋 Tabel Anggaran dan Realisasi")
        st.dataframe(df)

        # Chart batang
        st.subheader("📈 Grafik Realisasi per Kegiatan")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(df["nama_kegiatan"], df["persentase"], color="skyblue")
        ax.set_xlabel("Persentase Realisasi (%)")
        ax.set_ylabel("Nama Kegiatan")
        ax.set_xlim(0, 110)
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig)

        # Ringkasan
        total_anggaran = df["anggaran"].sum()
        total_realisasi = df["realisasi"].sum()
        rata2_realisasi = (total_realisasi / total_anggaran * 100).round(2)

        st.subheader("🧮 Ringkasan")
        st.metric("Total Anggaran", f"Rp {total_anggaran:,.0f}")
        st.metric("Total Realisasi", f"Rp {total_realisasi:,.0f}")
        st.metric("Rata-rata Realisasi", f"{rata2_realisasi:.2f}%")
