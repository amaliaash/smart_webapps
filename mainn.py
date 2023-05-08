import streamlit as st

def hitung_kadar(concentration, volume, dilution_factor, weight, unit):
    if dilution_factor:
        kadar = (concentration * volume * dilution_factor) / weight
    else:
        kadar = (concentration * volume) / weight
    
    if unit == "mg/L":
        kadar = kadar * 1000
    elif unit == "mg/Kg":
        kadar = kadar
    
    return kadar

st.title ("Aplikasi Menghitung Kadar Sampel")

concentration = st.number_input("Masukkan konsentrasi (dalam ppm): ", min_value=0.0, step=0.1)
volume = st.number_input("Masukkan volume labu takar (dalam L): ", min_value=0.0, step=0.1)
dilution_factor = st.number_input("Masukkan faktor pengenceran (dalam angka): ", min_value=0.0, step=0.1, value=1.0)
weight = st.number_input("Masukkan bobot sampel (dalam gram): ", min_value=0.0, step=0.0001, format="%.4f")

unit = st.selectbox("Pilih satuan:", ("mg/L", "mg/Kg"))

if st.button("Hitung Kadar"):
    kadar = hitung_kadar(concentration, volume, dilution_factor, weight, unit)
    st.write("Kadar sampel adalah {:.2f} {}".format(kadar, unit))
