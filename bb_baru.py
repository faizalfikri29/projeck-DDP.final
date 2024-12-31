import streamlit as st

def hitung_bbi_balita(usia, satuan='tahun'):
    # Konversi ke tahun jika input dalam bulan
    if satuan == 'bulan':
        usia_tahun = usia / 12
    else:
        usia_tahun = usia
    
    # Perhitungan BBI berdasarkan usia
    if usia_tahun < 1:
        usia_bulan = usia_tahun * 12
        bbi = (usia_bulan / 2) + 4
    else:
        bbi = (usia_tahun * 2) + 8
    
    return round(bbi, 2)

# Aplikasi Streamlit
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
