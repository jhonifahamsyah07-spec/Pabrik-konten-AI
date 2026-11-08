import streamlit as st

st.set_page_config(page_title="Pabrik Konten AI - Boss Edition Pro", page_icon="🎬", layout="centered")

st.title("🎬 Pabrik Konten AI - Flow Edition")
st.markdown("Pabrik Storyboard & Prompt otomatis untuk Google Flow & Video AI.")

st.markdown("---")

# 1. Upload Produk & Pilih Talent
st.subheader("1. Setup Aset Utama")
produk_img = st.file_uploader("Upload Foto Produk:", type=["jpg", "jpeg", "png"])
if produk_img is not None:
    st.image(produk_img, caption="Foto Produk Terunggah", use_container_width=True)

talent_option = st.selectbox(
    "Pilih Talent:", 
    ["Custom AI Avatar (Brand Sendiri)", "AI Model Wanita Lokal (Friendly & Natural)", "AI Model Pria Profesional", "Biarkan AI yang Memilihkan"]
)

nama_produk = st.text_input("Nama / Topik Produk:", placeholder="Contoh: Sepatu Sneakers Anti Air / Kopi Herbal")
keunggulan = st.text_area("Keunggulan Produk:", placeholder="Contoh: Ringan, anti air, harga terjangkau.")

st.markdown("---")

# 2. Mode Marketing & Durasi
st.subheader("2. Pengaturan Durasi & Strategi")
mode_marketing = st.radio("Pilih Mode Marketing:", ["Soft Selling (Storytelling & Emosional)", "Hard Selling (Tegas & Urgensi Tinggi)"])

# Pilihan Durasi (Otomatis hitung frame: 10 detik per frame standar AI)
pilihan_durasi = st.selectbox("Pilih Durasi Video:", ["10 Detik (1 Frame)", "20 Detik (2 Frame)", "30 Detik (3 Frame)", "60 Detik (6 Frame)"])

# Hitung jumlah frame berdasarkan durasi yang dipilih
if "20 Detik" in pilihan_durasi:
    total_frame = 2
elif "30 Detik" in pilihan_durasi:
    total_frame = 3
elif "60 Detik" in pilihan_durasi:
    total_frame = 6
else:
    total_frame = 1

st.info(f"💡 Durasi terpilih: **{pilihan_durasi}** | Sistem otomatis memecah menjadi **{total_frame} Frame Storyboard** (masing-masing 10 detik).")

st.markdown("---")

# 3. Tombol Generate
if st.button("🚀 GENERATE STORYBOARD & PROMPT GOOGLE FLOW"):
    if nama_produk and keunggulan:
        st.success("Berhasil! Storyboard siap dibawa ke Google Flow:")
        st.markdown(f"### 📋 Rencana Konten: {nama_produk}")
        st.markdown(f"**Talent:** {talent_option} | **Mode:** {mode_marketing} | **Total:** {total_frame} Frame")
        st.markdown("---")
        
        # Looping frame otomatis sesuai durasi
        for i in range(1, total_frame + 1):
            st.markdown(f"#### 🎞️ Storyboard Frame {i} (10 Detik)")
            
            if i == 1:
                st.markdown(f"* **Visual Scene:** Talent ({talent_option}) memegang produk {nama_produk} dengan ekspresi kaget/tertarik.")
                st.markdown(f"* **Naskah / Dialog:** \"Sumpah, baru tahu ada {nama_produk} sebagus ini...\"")
                st.markdown(f"* **Prompt Google Flow:** *Cinematic 4k shot, talent holding {nama_produk}, expressive face, professional lighting, 10s.*")
            elif i == total_frame:
                st.markdown(f"* **Visual Scene:** Close-up produk dengan teks keranjang kuning menyala.")
                st.markdown(f"* **Naskah / Dialog:** \"Jangan sampai kehabisan, langsung klik keranjang di bawah ya!\"")
                st.markdown(f"* **Prompt Google Flow:** *Product close up shot, glowing checkout button, dynamic motion, 10s.*")
            else:
                st.markdown(f"* **Visual Scene:** Memperlihatkan keunggulan: *{keunggulan}*.")
                st.markdown(f"* **Naskah / Dialog:** \"Nih lihat sendiri buktinya, bener-bener fungsional banget buat dipakai sehari-hari.\"")
                st.markdown(f"* **Prompt Google Flow:** *Action shot demonstrating product features, high resolution, 10s.*")
                
            st.markdown("---")
            
        st.info("💡 **Tips Eksekusi:** Salin teks **Prompt Google Flow** di atas satu per satu ke *tool* generator video AI untuk merender tiap frame-nya!")
    else:
        st.warning("Mohon isi dulu Nama / Topik Produk dan Keunggulannya, Boss!")
