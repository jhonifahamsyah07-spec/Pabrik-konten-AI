import streamlit as st

st.set_page_config(page_title="Pabrik Konten AI - Boss Edition", page_icon="🤖", layout="centered")

st.title("🤖 Pabrik Konten AI - Boss Edition")
st.markdown("Pabrik konten otomatis lengkap dengan **Storyboard, Dialog, & AI Prompt**. Tinggal klik, langsung eksekusi!")

# Pilihan Menu Lengkap
menu = st.selectbox(
    "Pilih Jenis Konten:", 
    [
        "AI Mini Drama (Storyboard & Dialog)", 
        "Konten Affiliate TikTok/Reels", 
        "Edukasi & Tips Kreatif", 
        "Motion Control & Prompt Kamera"
    ]
)

topik = st.text_input("Masukkan Ide / Produk:", placeholder="Contoh: Kurir paket di tengah hujan / Kopi susu kekinian")

if st.button("🚀 START / GENERATE KONTEN"):
    if topik:
        st.success("Berhasil memproses! Ini storyboard & skrip lengkap siap pakai untuk Boss:")
        
        if "Mini Drama" in menu:
            st.markdown("---")
            st.markdown("### 🎬 Storyboard & Skrip AI Mini Drama (60 Detik)")
            st.markdown(f"**Tema/Ide:** {topik}")
            st.markdown("**Format:** 6 Adegan x 10 Detik (Sempurna untuk Omni-Flash 1.1)")
            
            st.markdown("""
            * **Karakter Utama:** Tokoh utama yang gigih dan berdedikasi tinggi.
            * **Setting Waktu:** Sore/Malam hari dengan pencahayaan sinematik dramatis.
            """)
            
            st.markdown("#### 📝 Rincian Scene & Dialog:")
            
            st.markdown("---")
            st.markdown("**Scene 1 (0-10 detik): Opening Hook**")
            st.markdown("* **Visual / Kamera:** *Wide shot*, cuaca mendung, tokoh berdiri menatap jalanan.")
            st.markdown("* **Dialog / Suara:** *\"Kadang hidup nggak kasih tahu kapan badai datang, tapi kita yang harus tetep jalan.\"*")
            st.markdown("* **Prompt AI Video:** *Cinematic wide shot, dramatic weather, highly detailed, 8k, 10s.*")

            st.markdown("---")
            st.markdown("**Scene 2 (10-20 detik): Konflik / Tantangan**")
            st.markdown("* **Visual / Kamera:** *Close-up* ekspresi wajah kelelahan tapi penuh tekad.")
            st.markdown("* **Dialog / Suara:** *\"Capek? Pasti. Tapi kalau berhenti sekarang, impian tinggal angan-angan.\"*")
            st.markdown("* **Prompt AI Video:** *Close up emotional portrait, realistic lighting, 10s.*")

            st.markdown("---")
            st.markdown("**Scene 3 (20-30 detik): Aksi Utama**")
            st.markdown("* **Visual / Kamera:** *Medium shot* saat tokoh mulai bergerak fokus menyelesaikan tugas.")
            st.markdown("* **Dialog / Suara:** *\"Nggak ada hasil yang mengkhianati usaha. Bismillah.\"*")
            st.markdown("* **Prompt AI Video:** *Action shot, dynamic angle, cinematic atmosphere, 10s.*")

            st.markdown("---")
            st.markdown("**Scene 4 (30-40 detik): Titik Balik Emosional**")
            st.markdown("* **Visual / Kamera:** Interaksi hangat atau momen kelegaan.")
            st.markdown("* **Dialog / Suara:** *\"Makasih ya, Pak/Bu. Ini sangat berarti buat saya.\"*")
            st.markdown("* **Prompt AI Video:** *Two shot, warm emotional interaction, cinematic, 10s.*")

            st.markdown("---")
            st.markdown("**Scene 5 (40-50 detik): Klimaks**")
            st.markdown("* **Visual / Kamera:** Senja mulai berganti malam, lampu kota menyala indah (*bokeh*).")
            st.markdown("* **Dialog / Suara:** *Musik latar menghentak pelan, suasana penuh rasa syukur.*")
            st.markdown("* **Prompt AI Video:** *Night city lights bokeh, beautiful cinematic lighting, 10s.*")

            st.markdown("---")
            st.markdown("**Scene 6 (50-60 detik): Ending & Moral Cerita**")
            st.markdown("* **Visual / Kamera:** *Slow zoom-out* senyuman ikhlas dari tokoh utama. *Fade out*.")
            st.markdown("* **Dialog / Suara:** *\"Jangan patah semangat buat hari ini, Boss. Besok kita coba lebih keras lagi.\"*")
            st.markdown("* **Prompt AI Video:** *Portrait slow zoom out, inspiring ending, cinematic fade, 10s.*")
            
            st.info("💡 **Tips Omni-Flash 1.1:** Gunakan teks prompt di atas per scene secara berurutan agar konsistensi karakter terjaga!")

        elif "Affiliate" in menu:
            st.markdown("---")
            st.markdown("### 🛍️ Skrip Konten Affiliate TikTok/Reels")
            st.markdown(f"**Produk:** {topik}")
            st.markdown("""
            * **Hook (0-5d):** "Jujur, awalnya aku ragu sama produk ini, tapi setelah dicobain... wah gila sih!"
            * **Body (5-25d):** Tunjukkan detail produk, bahan, dan manfaat utamanya dengan gaya santai.
            * **CTA / Ending (25-45d):** "Stok terbatas ya, buat yang mau samaan langsung klik keranjang kuning di bawah!"
            """)

        elif "Edukasi" in menu:
            st.markdown("---")
            st.markdown("### 📚 Skrip Konten Edukasi & Tips")
            st.markdown(f"**Topik:** {topik}")
            st.markdown("""
            * **Hook (0-5d):** "Tiga rahasia yang jarang orang tahu soal {topik}!"
            * **Poin 1, 2, 3:** Penjelasan singkat padat berisi.
            * **Ending:** "Simpan video ini kalau nanti butuh ya, Boss!"
            """)

        else:
            st.markdown("---")
            st.markdown("### 🎥 Generator Motion Control & Kamera")
            st.markdown(f"**Kebutuhan:** {topik}")
            st.markdown("""
            * **Camera Movement:** Pan-left, Slow Zoom-in, Crane Shot.
            * **Lighting Style:** Cinematic Golden Hour / Moody Neon Cyberpunk.
            * **Prompt Siap Pakai:** Optimized for AI Video Generation tools.
            """)
            
    else:
        st.warning("Mohon isi dulu kolom ide atau produknya ya, Boss!")
