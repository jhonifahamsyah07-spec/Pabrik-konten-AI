import streamlit as st

st.title("🤖 Pabrik Konten AI - Boss Edition")
st.write("Selamat datang, Boss! Sistem siap digunakan.")

menu = st.selectbox("Pilih Menu:", ["Affiliate", "AI Mini Drama", "Edukasi", "Motion Control"])
topik = st.text_input("Masukkan Ide / Produk:")

if st.button("START / GENERATE"):
    if topik:
        st.success(f"Berhasil memproses menu: {menu} untuk topik: {topik}")
    else:
        st.warning("Mohon isi dulu kolom inputnya, Boss!")
