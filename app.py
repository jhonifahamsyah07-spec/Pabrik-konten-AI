// Fungsi untuk memanggil AI dan menghasilkan storyboard bersih khusus affiliate
async function generateStoryboardScript(productName, productFeatures, promoStyle, duration) {
  
  // System instructions / Prompt ketat untuk AI
  const systemInstruction = `
  Kamu adalah AI Content Director profesional untuk affiliate marketer. 
  Tugasmu adalah menganalisis produk dan membuat storyboard video short-form.
  
  ATURAN MUTLAK:
  1. WAJIB menyebutkan nama produk secara spesifik (${productName}) dalam naskah dan prompt visual. Jangan gunakan teks template generik!
  2. Format output WAJIB HANYA menampilkan dua hal per frame agar mudah disalin (sekali copy):
     - 🎬 Prompt Visual & Sinematik
     - 📋 Naskah & Dialog (Sekali Copy)
  3. Jangan sertakan kalimat pembuka, basa-basi, atau penutup. Langsung berikan format kodenya saja!
  `;

  const userPrompt = `
  Produk: ${productName}
  Keunggulan: ${productFeatures}
  Gaya Promosi: ${promoStyle}
  Durasi Video: ${duration}
  `;

  try {
    // Contoh pemanggilan model AI di backend Node.js
    const response = await aiModel.generateContent({
      contents: [
        { role: 'user', parts: [{ text: systemInstruction }, { text: userPrompt }] }
      ]
    });

    return response.text; // Mengembalikan hasil teks yang sudah bersih
  } catch (error) {
    console.error("Gagal generate storyboard:", error);
    return "Terjadi kesalahan saat memproses produk.";
  }
}
