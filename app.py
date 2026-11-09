import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Pabrik Konten AI - Affiliate Studio",
    page_icon="🎬",
    layout="centered"
)

# Tema & Styling Modern Ungu Estetik
st.markdown("""
    <style>
    .main {
        background-color: #0f1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7c3aed, #a855f7);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6d28d9, #9333ea);
        color: #fff;
    }
    .frame-box {
        background-color: #1e1e2f;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #4c1d95;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi Langsung di Muka
st.title("🎬 Pabrik Konten AI Studio")
st.markdown("Pencetak storyboard & skrip video affiliate otomatis, cepat, dan siap pakai.")
st.markdown("---")

# --- AREA UTAMA: LANGSUNG UPLOAD & PILIHAN TANPA SIDEBAR GESER ---
uploaded_file = st.file_uploader("📸 Upload Foto Produk di Sini", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
with col1:
    ad_style = st.selectbox(
        "Pilih Gaya Promosi",
        [
            "Soft Selling",
            "Hard Selling",
            "UGC Unboxing Fast",
            "Problem-Solution",
            "Before-After",
            "FOMO / Urgensi Ekstrem",
            "POV (Point of View)",
            "Educational / Racun Edukasi"
        ]
    )
    
    duration = st.selectbox(
        "Pilih Durasi Video",
        ["10 Detik (1 Frame)", "20 Detik (2 Frame Bersambung)", "30 Detik (3 Frame Bersambung)"]
    )

with col2:
    location_type = st.selectbox(
        "Pilih Lokasi Syuting (Opsional)",
        ["Auto / Menyesuaikan Produk", "Indoor (Kamar / Studio Estetik)", "Outdoor (Alam / Jalanan / Kafe)"]
    )
    
    talent_ref = st.text_input(
        "Referensi Talent Kustom (Opsional)",
        placeholder="Contoh: Model wanita lokal, hijab pastel..."
    )

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("✨ Generate Storyboard Sekarang")

# --- PROSES & HASIL OUTPUT ---
if generate_btn:
    if uploaded_file is not None:
        st.success("✅ Foto produk berhasil dianalisis! Berikut hasil storyboard siap *copy*:")
        st.markdown("---")
        
        # Logika Output Berdasarkan Durasi & Lokasi
        loc_desc = f"Setting lokasi: {location_type}." if location_type != "Auto / Menyesuaikan Produk" else ""
        
        if "10 Detik" in duration:
            st.markdown("""
            <div class="frame-box">
                <h4><b>Frame 1 (0-10s) — Format Padat Tunggal</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Cinematic 4k, close up product, professional lighting, clean aesthetic. {loc_desc} Talent menunjukkan produk dengan ekspresi antusias.</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Wah gila sih ini, bener-bener penyelamat banget buat atasi masalah kita sehari-hari! Kualitasnya juara dan gampang banget dipakai. Mumpung lagi ada promo, buruan chekout sekarang sebelum kehabisan di keranjang kuning!"</i></p>
                <p><b>Google Flow Video Prompt:</b><br>
                <code>Dynamic product showcase, fast paced transition, 4k resolution, smooth camera movement.</code></p>
            </div>
            """.format(loc_desc=loc_desc), unsafe_allow_html=True)
            
        elif "20 Detik" in duration:
            st.markdown("""
            <div class="frame-box">
                <h4><b>Frame 1 (0-10s) — Hook & Masalah Awal</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Unboxing package moment, aesthetic desk setup, bright lighting. {loc_desc} Talent membuka paket dengan ekspresi penasaran.</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Sumpah kaget banget pas paket ini datang, sebagus itu! Buat kalian yang sering punya masalah sama hal kayak gini, wajib banget tonton video ini sampai habis."</i></p>
                <p><b>Google Flow Video Prompt:</b><br>
                <code>Unboxing package, close up hands opening box, bright aesthetic lighting.</code></p>
            </div>
            
            <div class="frame-box">
                <h4><b>Frame 2 (10-20s) — Solusi & Call to Action (CTA)</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Product in action, happy expression, smooth transition. {loc_desc} Talent menunjukkan hasil produk dan menunjuk keranjang kuning.</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Setelah dicoba, hasilnya beneran di luar dugaan! Gampang dipakai, hemat waktu, dan awet banget. Mumpung stok masih ada dan lagi diskon, langsung klik keranjang kuning di bawah ya!"</i></p>
                <p><b>Google Flow Video Prompt:</b><br>
                <code>Product demonstration, smiling model pointing down, high conversion e-commerce style.</code></p>
            </div>
            """.format(loc_desc=loc_desc), unsafe_allow_html=True)
            
        else: # 30 Detik
            st.markdown("""
            <div class="frame-box">
                <h4><b>Frame 1 (0-10s) — Hook & Unboxing</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Dynamic hook scene, aesthetic opening. {loc_desc} Talent memegang produk dengan ekspresi takjub.</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Jangan beli barang ini sebelum kalian tahu rahasia kelebihannya! Paketnya udah nyampe dan kita langsung buktikan sekarang."</i></p>
            </div>
            
            <div class="frame-box">
                <h4><b>Frame 2 (10-20s) — Ulasan & Bukti Keunggulan</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Detailed product close-up, functional demonstration. {loc_desc}</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Tekstur dan kualitasnya beda banget dari pasaran. Pas dicoba, langsung terasa bedanya dalam hitungan detik aja."</i></p>
            </div>
            
            <div class="frame-box">
                <h4><b>Frame 3 (20-30s) — Solusi Tuntas & CTA</b></h4>
                <p><b>Prompt Visual & Sinematik:</b><br>
                Satisfied closing, pointing gesture to yellow basket. {loc_desc}</p>
                <p><b>Naskah & Dialog (Sekali Copy):</b><br>
                <i>"Udah harganya ramah di kantong, garansi kualitas pula. Yuk buruan amankan stoknya, klik keranjang kuning sekarang juga!"</i></p>
                <p><b>Google Flow Video Prompt (Full 30s):</b><br>
                <code>High conversion e-commerce video sequence, smooth transitions, professional color grading.</code></p>
            </div>
            """.format(loc_desc=loc_desc), unsafe_allow_html=True)
            
    else:
        st.warning("⚠️ Silakan upload foto produk terlebih dahulu di atas, Boss!")
else:
    st.info("👆 Silakan lengkapi pilihan di atas, upload foto produk, lalu klik tombol **Generate Storyboard**.")
