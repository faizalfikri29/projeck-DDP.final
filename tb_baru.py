import streamlit as st

def hitung_tinggi_badan_balita(jenis_kelamin, umur):
    tinggi_laki_laki = {
        0: "Umur harus antara 1 hingga 5 tahun.", 1: 54.7, 2: 58.4, 3: 61.4, 4: 63.9, 5: 65.9
    }
    
    tinggi_perempuan = {
        0: "Umur harus antara 1 hingga 5 tahun.", 1: 53.7, 2: 57.1, 3: 59.8, 4: 62.1, 5: 64.0
    }
    
    # Pilih data sesuai jenis kelamin
    if jenis_kelamin.lower() == "laki-laki":
        data_tinggi = tinggi_laki_laki
    elif jenis_kelamin.lower() == "perempuan":
        data_tinggi = tinggi_perempuan
    else:
        return "Jenis kelamin tidak valid. Gunakan 'laki-laki' atau 'perempuan'."
    
    return data_tinggi.get(umur, None)

def hitung_tinggi_badan_balita_ui():
    st.title("Estimasi Tinggi Badan Balita")

    # Input jenis kelamin dan umur
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["laki-laki", "perempuan"])
    umur = st.number_input("Umur (tahun)", min_value=0, max_value=5, step=1)

    # Hitung tinggi badan jika tombol ditekan
    if st.button("Hitung Tinggi Badan"):
        hasil = hitung_tinggi_badan_balita(jenis_kelamin, umur)
        if isinstance(hasil, float):
            st.success(f"Estimasi tinggi badan balita {jenis_kelamin} umur {umur} tahun: {hasil} cm")
        else:
            st.error(hasil)

if __name__ == "__main__":
    hitung_tinggi_badan_balita_ui()