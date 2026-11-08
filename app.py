import streamlit as st

st.set_page_config(page_title="Pabrik Konten AI - Boss Edition Pro", page_icon="🎬", layout="centered")

st.title("🎬 Pabrik Konten AI - Auto Flow Edition")
st.markdown("Cukup upload gambar & ketuk-ketuk, AI yang urus sisanya!")

st.markdown("---")

# 1. Setup Utama (Tanpa perlu ketik nama/keunggulan produk manual)
st.subheader("1. Upload & Setup Aset")
produk_img = st.file_uploader("Upload Foto Produk:", type=["jpg", "jpeg", "png"])
if produk_img is not None:
    st.image(produk_img, caption="Foto Produk Terunggah & Dianalisis AI", use_container_width=True)
    st.success("AI berhasil mendeteksi produk dari foto!")

talent_option = st.selectbox(
    "Pilih Talent:", 
    ["Custom AI Avatar (Brand Sendiri)", "AI Model Wanita Lokal (Friendly & Natural)", "AI Model Pria Profesional", "AI Otomatis Menyesuaikan"]
)

st.markdown("---")

# 2. Pengaturan Durasi & Strategi
st.subheader("2. Pengaturan Durasi & Mode Marketing")
mode_marketing = st.radio("Pilih Mode Marketing:", ["Soft Selling (Storytelling & Emosional)", "Hard Selling (Tegas & Urgensi Tinggi)"])

pilihan_durasi = st.selectbox("Pilih Durasi Video:", ["10 Detik (1 Frame)", "20 Detik (2 Frame)", "30 Detik (3 Frame)", "60 Detik (6 Frame)"])

# Hitung jumlah frame otomatis berdasarkan durasi
if "20 Detik" in pilihan_durasi:
    total_frame = 2
elif "30 Detik" in pilihan_durasi:
    total_frame = 3
elif "60 Detik" in pilihan_durasi:
    total_frame = 6
else:
    total_frame = 1

st.info(f"💡 Durasi terpilih: **{pilihan_durasi}** | Otomatis jadi **{total_frame} Frame Storyboard**.")

st.markdown("---")

# 3. Tombol Generate & Download
if st.button("🚀 GENERATE STORYBOARD OTOMATIS"):
    if produk_img is not None:
        st.success("Storyboard & Naskah Berhasil Diracik oleh AI!")
        
        # Simpan teks hasil generate untuk tombol download
        hasil_teks = f"=== PABRIK KONTEN AI - STORYBOARD ===\n" \
                     f"Talent: {talent_option}\n" \
                     f"Mode: {mode_marketing}\n" \
                     f"Durasi: {pilihan_durasi} ({total_frame} Frame)\n\n"
        
        st.markdown(f"### 📋 Hasil Storyboard Siap Bawa ke Google Flow")
        st.markdown(f"**Talent:** {talent_option} | **Mode:** {mode_marketing}")
        st.markdown("---")
        
        for i in range(1, total_frame + 1):
            frame_text = f"--- FRAME {i} (10 Detik) ---\n"
            st.markdown(f"#### 🎞️ Storyboard Frame {i} (10 Detik)")
            
            if i == 1:
                v_desc = f"Talent ({talent_option}) menunjukkan produk dari foto dengan ekspresi antusias."
                n_desc = f"\"Wah, jujur ini salah satu temuan produk paling mantap yang wajib kalian tahu...\""
                p_desc = f"Cinematic 4k shot, talent showcasing product from upload image, highly detailed, 10s."
            elif i == total_frame:
                v_desc = f"Close-up produk dengan animasi teks keranjang kuning menyala."
                n_desc = f"\"Stok terbatas banget, buruan klik keranjang kuning sekarang sebelum kehabisan!\""
                p_desc = f"Product close up shot, glowing checkout button, dynamic motion, 10s."
            else:
                v_desc = f"Aksi penggunaan produk secara nyata untuk memperlihatkan fungsi utamanya."
                n_desc = f"\"Nih lihat sendiri hasilnya, bener-bener praktis dan fungsional banget dipakai harian.\""
                p_desc = f"Action shot demonstrating product use, high resolution, 10s."
            
            st.markdown(f"* **Visual Scene:** {v_desc}")
            st.markdown(f"* **Naskah / Dialog:** {n_desc}")
            st.markdown(f"* **Prompt Google Flow:** `{p_desc}`")
            st.markdown("---")
            
            hasil_teks += f"{frame_text}Visual: {v_desc}\nNaskah: {n_desc}\nPrompt: {p_desc}\n\n"

        # Tombol Download Storyboard dalam bentuk file text (.txt)
        st.download_button(
            label="📥 DOWNLOAD STORYBOARD (TXT)",
            data=hasil_teks,
            file_name="Storyboard_Google_Flow.txt",
            mime="text/plain"
        )
        
        st.info("💡 **Tips:** Klik tombol download di atas untuk menyimpan file teks storyboard, lalu copas prompt-nya ke Google Flow!")
    else:
        st.warning("Mohon upload foto produknya dulu ya, Boss! Biar AI bisa langsung baca gambarnya.")
