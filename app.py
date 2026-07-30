import streamlit as st

st.title("Aplikasi Perhitungan Nilai")
st.write("Silakan isi form di bawah ini untuk melihat rekap nilai Anda.")


with st.form(key="form_nilai"):
    st.subheader("Form Input Nilai Mahasiswa/Siswa")

    # Input angka dengan batasan 0 - 100
    kehadiran = st.number_input(
        "Kehadiran (%)", min_value=0, max_value=100, value=100, step=1
    )
    nilai_tugas = st.number_input(
        "Nilai Tugas", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )
    uts = st.number_input(
        "Nilai UTS", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )
    uas = st.number_input(
        "Nilai UAS", min_value=0.0, max_value=100.0, value=0.0, step=0.5
    )

   
    tombol_hitung = st.form_submit_button(label="Hitung")


if tombol_hitung:
    st.divider()
    st.success("Data berhasil diproses!")
    st.subheader("Hasil Nilai yang Diisikan:")

    
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Kehadiran", value=f"{kehadiran}%")
        st.metric(label="Nilai Tugas", value=f"{nilai_tugas:.1f}")

    with col2:
        st.metric(label="Nilai UTS", value=f"{uts:.1f}")
        st.metric(label="Nilai UAS", value=f"{uas:.1f}")
