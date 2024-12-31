import streamlit as st
# Set page config harus berada di luar fungsi main dan di awal script
st.set_page_config(
    page_title="Kalkulator Balita",
    page_icon="👶",
    layout="wide"
)
from bb_baru import hitung_bbi_balita
from usia_baru import hitung_usia
from tb_baru import hitung_tinggi_badan_balita_ui


def main():
    st.markdown("""
        <style>
            .stApp {
            background-color: #FFFACD;
        }
            [data-testid="stSidebar"]{
            background-color: #A9A9A9;
            color: black;
        }
            [data-testid="stSidebar"] * {
            color: black !important;
            font-size: 14px;
    }
        </style>
""", unsafe_allow_html=True)
    st.title("📊 Informasi Kesehatan Balita Posyandu")
    menu = st.sidebar.selectbox(
        "Pilih Fitur:",
        ["Beranda", "Kalkulator Usia", "Kalkulator BBI", "Kalkulator Tinggi Badan"]
    )
    st.image("img/gbmr.balita.jpg")
    if menu == "Beranda":
        st.title("Selamat Datang di Website Informasi kesehatan Balita")
        st.markdown("Aplikasi ini dirancang untuk membantu Anda memantau perkembangan si kecil. Untuk mendapatkan hasil yang akurat, pastikan data yang Anda masukkan sudah benar.")
        st.info("Adapun data sesuai masukan WHO bahwa Usia balita 1-5 tahun")
        st.write("""
        Aplikasi ini menyediakan beberapa kalkulator untuk membantu Anda menghitung:
        * Berat Badan Ideal (BBI) balita
        * Usia balita berdasarkan tanggal lahir
        * Estimasi tinggi badan balita
        
        Silakan pilih kalkulator yang Anda butuhkan di menu samping.
        """)
        
        # Informasi tambahan
        st.markdown("### Cara Penggunaan")
        st.write("""
        1. Pilih jenis kalkulator yang diinginkan pada menu di sebelah kiri
        2. Ikuti petunjuk dan masukkan data yang diminta
        3. Klik tombol hitung untuk melihat hasil
        """)
        
        # Footer
        st.markdown("---")
        st.markdown("### Catatan")
        st.write("""
        * Perhitungan bersifat estimasi dan dapat berbeda dengan kondisi aktual
        * Konsultasikan dengan dokter untuk hasil yang lebih akurat
        """)
    elif menu == "Kalkulator Usia":
        hitung_usia()
    
        # Halaman Kalkulator BBI
    elif menu == "Kalkulator BBI":
        st.title("Kalkulator Berat Badan Ideal (BBI) Balita")
        
        # Pilih satuan usia
        satuan = st.selectbox("Pilih satuan usia:", ["tahun", "bulan"])

        # Input usia berdasarkan satuan
        if satuan == "tahun":
            usia = st.slider("Masukkan usia balita (dalam tahun):", min_value=1, max_value=5)
        elif satuan == "bulan":
            usia = st.slider("Masukkan usia balita (dalam bulan):", min_value=1, max_value=12)

        # Tombol hitung
        if st.button("Hitung BBI"):
            if usia > 0:
                # Hitung BBI
                bbi = hitung_bbi_balita(usia, satuan)
                st.success(f"Berat Badan Ideal balita anda: {bbi} kg")
            else:
                st.warning("Masukkan usia yang valid!")
    elif menu == "Kalkulator Tinggi Badan":
        hitung_tinggi_badan_balita_ui()

if __name__ == "__main__":
    main()