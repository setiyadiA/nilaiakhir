import streamlit as st

st.title("Aplikasi Perhitungan Nilai Akhir")



with st.form(key="form_nilai"):
    st.subheader("Form Input Nilai")

   
    kehadiran = st.number_input(
        "Jumlah Kehadiran (Maksimal 16 Pertemuan)",
        min_value=0,
        max_value=16,
        value=16,
        step=1,
    )
    nilai_tugas = st.number_input(
        "Nilai Tugas (0 - 100)", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )
    uts = st.number_input(
        "Nilai UTS (0 - 100)", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )
    uas = st.number_input(
        "Nilai UAS (0 - 100)", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )


    tombol_hitung = st.form_submit_button(label="Hitung Nilai Akhir")


if tombol_hitung:
    
    val_kehadiran = (kehadiran / 16 * 100) * 0.05  # Bobot 5%
    val_tugas = nilai_tugas * 0.20                 # Bobot 20%
    val_uts = uts * 0.35                           # Bobot 35%
    val_uas = uas * 0.40                           # Bobot 40%

    
    nilai_akhir = val_kehadiran + val_tugas + val_uts + val_uas

    
    if nilai_akhir >= 80:
        indeks = "A"
    elif nilai_akhir >= 68:
        indeks = "B"
    elif nilai_akhir >= 56:
        indeks = "C"
    elif nilai_akhir >= 45:
        indeks = "D"
    else:
        indeks = "E"

    st.divider()
    st.success("Perhitungan Selesai!")
    
   
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(
            label="NILAI AKHIR TOTAL",
            value=f"{nilai_akhir:.2f} / 100",
        )
    with col_res2:
        st.metric(
            label="INDEKS NILAI",
            value=indeks,
        )





