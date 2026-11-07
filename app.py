import streamlit as st

st.set_page_config(page_title="Pabrik Konten AI - Boss Edition Pro", page_icon="🚀", layout="centered")

st.title("🤖 Pabrik Konten AI - Pro Edition")
st.markdown("Pabrik konten otomatis berbasis *Workflow* interaktif untuk kebutuhan kreator & affiliate.")

# Pilihan Menu Utama
menu = st.selectbox(
    "Pilih Modul Konten:", 
    ["Affiliate Generator", "AI Mini Drama Studio", "Edukasi & Tips Kreatif"]
)

st.markdown("---")

if "Affiliate" in menu:
    st.subheader("🛍️ Modul Konten Affiliate Interaktif")
    
    # 1. Upload Foto Produk
    uploaded_file = st.file_uploader("1. Upload Foto Produk:", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview Foto Produk Boss", use_container_width=True)
        st.success("Foto produk berhasil diunggah!")

    # 2. Masukkan Nama & Keunggulan Produk
    nama_produk = st.text_input("2. Masukkan Nama Produk:", placeholder="Contoh: Sepatu Sneakers Anti Air")
    keunggulan = st.text_area("Keunggulan / Benefit Utama:", placeholder="Contoh: Anti air, ringan dipakai lari, tidak bikin bau kaki.")

    # 3. Pilih Durasi Video
    durasi = st.selectbox("3. Pilih Durasi Video:", ["15 Detik (Fast & Catchy)", "30 Detik (Standard TikTok/Reels)", "60 Detik (Detailed Review)"])

    # 4. Pilih Gaya Penjualan
    gaya = st.radio("4. Pilih Gaya Penjualan:", ["Hard Selling (Tegas & Urgensi Tinggi)", "Soft Selling (Storytelling & Emosional)"])

    # 5. Pilih Jumlah Frame Storyboard
    jumlah_frame = st.slider("5. Pilih Jumlah Frame Storyboard:", min_value=3, max_value=8, value=5)

    st.markdown("---")

    # 6. Tombol Generate
    if st.button("🚀 6. GENERATE STORYBOARD & PROMPT"):
        if nama_produk and keunggulan:
            st.success("Storyboard & Prompt Affiliate Berhasil Dibuat!")
            st.markdown(f"### 📋 Hasil Perencanaan Konten: {nama_produk}")
            st.markdown(f"**Gaya:** {gaya} | **Durasi:** {durasi} | **Total Frame:** {jumlah_frame}")
            
            for i in range(1, jumlah_frame + 1):
                st.markdown(f"#### 🎬 Frame {i}")
                if i == 1:
                    st.markdown(f"* **Visual:** Close-up produk {nama_produk} dengan pencahayaan sinematik.")
                    st.markdown(f"* **Hook/Dialog:** \"Jujur kaget banget pas nyobain {nama_produk} ini...\"")
                    st.markdown(f"* **Prompt AI Video:** *Product close up shot, cinematic lighting, ultra-detailed, 8k, 5s.*")
                elif i == jumlah_frame:
                    st.markdown(f"* **Visual:** Teks keranjang kuning / tombol checkout menyala.")
                    st.markdown(f"* **Call to Action:** \"Stok terbatas buat Boss, buruan klik keranjang kuning sekarang!\"")
                    st.markdown(f"* **Prompt AI Video:** *Call to action screen, glowing shopping cart icon, dynamic, 5s.*")
                else:
                    st.markdown(f"* **Visual:** Menunjukkan keunggulan: *{keunggulan}*.")
                    st.markdown(f"* **Dialog:** \"Nih lihat sendiri buktinya, bener-bener fungsional banget.\"")
                    st.markdown(f"* **Prompt AI Video:** *Action shot demonstrating product features, realistic, 5s.*")
                st.markdown("---")
        else:
            st.warning("Mohon isi Nama Produk dan Keunggulannya dulu ya, Boss!")

else:
    st.subheader("🎬 Modul AI Mini Drama & Edukasi")
    topik_umum = st.text_input("Masukkan Ide Cerita / Topik:", placeholder="Contoh: Perjuangan kurir paket")
    jml_scene = st.slider("Pilih Jumlah Scene Storyboard:", min_value=3, max_value=6, value=4)
    
    if st.button("🚀 GENERATE MINI DRAMA"):
        if topik_umum:
        # Menghasilkan output mini drama dinamis sesuai jumlah scene yang dipilih
            st.success("Storyboard Mini Drama Siap Dieksekusi!")
            st.markdown(f"### 🎥 Storyboard: {topik_umum}")
            for s in range(1, jml_scene + 1):
                st.markdown(f"#### 🎞️ Scene {s} (Durasi: 10 Detik)")
                st.markdown(f"* **Visual Scene:** Penggambaran adegan ke-{s} untuk tema {topik_umum}.")
                st.markdown(f"* **Dialog Tokoh:** *\"Dialog emosional atau narasi untuk adegan {s}...\"*")
                st.markdown(f"* **Prompt AI Video (Omni-Flash 1.1):** *Cinematic scene {s}, dramatic angle, 10s.*")
                st.markdown("---")
        else:
            st.warning("Mohon isi ide ceritanya dulu, Boss!")
