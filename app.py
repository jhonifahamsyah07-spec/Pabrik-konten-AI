
import streamlit as st

st.set_page_config(page_title="Pabrik Konten AI - Boss Edition", page_icon="🤖", layout="centered")

st.title("🤖 Pabrik Konten AI - Boss Edition")
st.markdown("Pabrik konten otomatis untuk Affiliate & Mini Drama AI. **Tinggal ketuk, skrip langsung jadi!**")

# Pilihan Menu
menu = st.selectbox(
    "Pilih Jenis Konten:", 
    ["AI Mini Drama (60 Detik)", "Konten Affiliate TikTok/Reels"]
)

topik = st.text_input("Masukkan Ide / Produk:", placeholder="Contoh: Penjual kopi keliling sore hari")

if st.button("🚀 START / GENERATE SKRIP"):
    if topik:
        st.success("Berhasil memproses! Ini draf skrip siap pakai untuk Boss:")
        
        if "Mini Drama" in menu:
            st.markdown("---")
            st.markdown("### 🎬 Skrip AI Mini Drama (60 Detik)")
            st.markdown(f"**Tema/Ide:** {topik}")
            st.markdown("**Format:** 6 Adegan x 10 Detik (Ideal untuk Omni-Flash 1.1)")
            
            st.markdown("""
            * **Karakter Utama:** Pak Rudi (Penjual kopi keliling yang sabar dan ramah).
            * **Setting Waktu:** Sore hari menjelang senja di pinggir jalan kota.
            * **Suasana:** Hangat, sinematik, penuh emosi perjuangan hidup.
            """)
            
            # Rincian Scene
            st.markdown("#### 📝 Rincian Scene:")
            st.markdown("1. **Scene 1 (0-10d):** *Medium Shot* Pak Rudi menyalakan kompor kecil di gerobaknya. Asap kopi mengepul hangat di tengah keramaian lalu lintas sore.")
            st.markdown("2. **Scene 2 (10-20d):** *Close-up* wajah Pak Rudi yang tersenyum ramah menyambut pelanggan pertama seorang pekerja kantor yang kelelahan.")
            st.markdown("3. **Scene 3 (20-30d):** *POV Shot* tangan menyeduh kopi hitam kental dengan latar belakang langit senja berwarna jingga kemerahan.")
            st.markdown("4. **Scene 4 (30-40d):** *Two Shot* Pelanggan meminum kopi, tersenyum lega seolah beban kerjanya hilang seketika.")
            st.markdown("5. **Scene 5 (40-50d):** *Wide Shot* Suasana malam mulai turun, lampu-lampu jalan menyala, gerobak kopi Pak Rudi tetap ramai dikunjungi.")
            st.markdown("6. **Scene 6 (50-60d):** *Ending Shot* Pak Rudi merapikan gelas dengan senyuman penuh syukur. *Fade out to black*.")
            
            st.info("💡 **Tips Prompt AI:** Gunakan durasi 10 detik per *scene* agar konsistensi karakter Pak Rudi tetap terjaga dengan baik!")
            
        else:
            st.markdown("---")
            st.markdown("### 🛍️ Skrip Konten Affiliate")
            st.markdown(f"**Produk:** {topik}")
            
            st.markdown("""
            * **Durasi:** 30 - 45 Detik
            * **Hook (0-5d):** "Siapa nih yang masih punya masalah sama produk ini? Wajib tonton sampai habis!"
            * **Body / Penjelasan (5-25d):** Jelaskan keunggulan utama produk, bahan berkualitas, dan cara pakainya dengan bahasa santai.
            * **Call to Action / Ending (25-45d):** "Yuk, buat Boss yang nggak mau kehabisan, langsung klik keranjang kuning di bawah sekarang juga!"
            """)
            st.info("💡 **Tips Affiliate:** Tambahkan *angle* video produk secara *real* saat dipakai agar penonton lebih percaya.")
            
    else:
        st.warning("Mohon isi dulu kolom ide atau produknya ya, Boss!")
