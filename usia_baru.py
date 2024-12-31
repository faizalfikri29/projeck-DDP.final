import streamlit as st
from datetime import datetime, timedelta

def hitung_usia():
    st.title("Kalkulator Usia Balita")

    # Input tanggal lahir dan tanggal perhitungan
    tanggal_lahir = st.date_input("Tanggal Lahir Balita")
    tanggal_perhitungan = st.date_input("Tanggal Perhitungan (Opsional)", value=datetime.now().date())

    # Hitung usia jika tombol ditekan
    if st.button("Hitung Usia"):
        if tanggal_lahir > tanggal_perhitungan:
            st.error("Tanggal lahir tidak boleh lebih besar dari tanggal perhitungan")
        else:
            delta = tanggal_perhitungan - tanggal_lahir
            tahun, bulan, hari, jam, sisa_detik = delta.days // 365, delta.days // 30 % 12, delta.days % 30, *divmod(delta.seconds, 3600)
            st.success(f"Usia balita adalah {tahun} tahun, {bulan} bulan, {hari} hari")

if __name__ == "__main__":
    hitung_usia()