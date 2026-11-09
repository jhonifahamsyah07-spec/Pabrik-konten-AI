import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Pabrik Konten AI - Affiliate Studio",
    page_icon="🎬",
    layout="wide"
)

# Tema & Styling Modern Ungu (Sesuai Karakter Brand)
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
        padding: 0.5rem 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6d28d9, #9333ea);
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.title("🎬 Pabrik Konten AI Studio")
st.markdown("---")

# Kolom Samping (Sidebar) untuk Kontrol & Pengaturan
with st.sidebar:
    st.header("⚙️ Kontrol Kreator")
    
    # 1. Upload Foto Produk
    uploaded_file = st.file_uploader("Upload Foto Produk", type=["jpg", "jpeg", "png"])
    
    # 2. Pilihan Gaya Promosi
    ad_style = st.selectbox(
        "Pilih Gaya Promosi (Marketing Style)",
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
    
    # 3. Pilihan Durasi Video
    duration = st.selectbox(
        "Pilih Durasi Video",
        ["10 Detik (1 Frame)", "20 Detik (2 Frame Bersambung)", "30 Detik (3 Frame Bersambung)"]
    )
    
    # 4. Input Referensi Talent Kustom
    talent_ref = st.text_input(
        "Referensi Talent Kustom (Opsional)",
        placeholder="Contoh: Model wanita lokal, casual, hijab pastel..."
    )
    
    generate_btn = st.button("✨ Generate Storyboard")

# Area Utama (Main Content)
if generate_btn:
    if uploaded_file is not None:
        st.success("✅ Foto produk berhasil dianalisis oleh Pabrik Konten AI!")
        
        # Simulasi & Struktur Output Berdasarkan Durasi
        st.markdown("### 📋 Hasil Storyboard & Skrip Konten")
        
        if "10 Detik" in duration:
            st.markdown("#### **Frame 1 (0-10s) — Format Padat Tunggal**")
            st.info("**Visual:** [Hook kuat di awal] + [Isi/solusi singkat produk] + [Akhiri langsung dengan CTA Keranjang Kuning]")
            st.text_area("Naskah / Dialog Talent (10s):", "Wah gila sih ini, bener-bener penyelamat banget buat... (Jelaskan keunggulan utama dalam 3 detik) Yuk, chekout sekarang sebelum kehabisan di keranjang kuning!", height=100, key="f1")
            st.code("Google Flow Prompt: Cinematic 4k, close up product, professional lighting, fast paced transition...", language="text")
            
        elif "20 Detik" in duration:
            st.markdown("#### **Frame 1 (0-10s) — Hook & Pengenalan Masalah**")
            st.info("**Visual:** Momen buka paket / *unboxing* cepat + Menyoroti masalah utama penonton.")
            st.text_area("Naskah Frame 1:", "Sumpah kaget banget pas paket ini datang, sebagus itu! Buat kalian yang sering punya masalah [Isi Masalah], wajib tonton ini.", height=80, key="f1")
            st.code("Google Flow Prompt 1: Unboxing package, aesthetic desk setup, cinematic lighting...", language="text")
            
            st.markdown("#### **Frame 2 (10-20s) — Solusi & Call to Action (CTA)**")
            st.info("**Visual:** Demonstrasi produk beraksi + Penekanan keunggulan + Menunjuk ke keranjang kuning.")
            st.text_area("Naskah Frame 2:", "Setelah dicoba, hasilnya beneran di luar dugaan! Gampang dipakai dan awet banget. Mumpung lagi promo, langsung klik keranjang kuning di bawah ya!", height=80, key="f2")
            st.code("Google Flow Prompt 2: Product in action, happy expression, bright aesthetic, smooth transition...", language="text")
            
        else: # 30 Detik
            st.markdown("#### **Frame 1 (0-10s) — Hook & Unboxing**")
            st.info("**Visual:** Hook kuat dan pembukaan paket yang memancing rasa penasaran.")
            st.text_area("Naskah Frame 1:", "Jangan beli barang ini sebelum tahu rahasia kelebihannya! Paketnya udah nyampe dan kita unboxing sekarang.", height=70, key="f1")
            
            st.markdown("#### **Frame 2 (10-20s) — Pembuktian & Keunggulan**")
            st.info("**Visual:** Ulasan fungsi utama produk secara mendalam dan realistis.")
            st.text_area("Naskah Frame 2:", "Teksturnya/kualitasnya beda banget dari yang lain, pas dicoba langsung terasa bedanya dalam hitungan detik.", height=70, key="f2")
            
            st.markdown("#### **Frame 3 (20-30s) — Solusi Tuntas & CTA**")
            st.info("**Visual:** Penutup menarik + Tombol / gestur menunjuk ke Keranjang Kuning.")
            st.text_area("Naskah Frame 3:", "Udah harganya ramah di kantong, garansi kualitas pula. Yuk buruan amankan stoknya, klik keranjang kuning sekarang!", height=70, key="f3")
            st.code("Google Flow Prompt (Full 30s): Dynamic sequence, high conversion e-commerce video style...", language="text")
            
    else:
        st.warning("⚠️ Silakan upload foto produk terlebih dahulu di menu sebelah kiri, Boss!")
else:
    st.info("👈 Silakan atur preferensi di sebelah kiri, upload foto produk, lalu klik tombol **Generate Storyboard**.")
