import streamlit as st

st.title("Aplikasi Perhitungan Nilai")
st.write("Silakan isi form di bawah ini untuk melihat rekap nilai Anda.")

# Membuat Form Input
with st.form(key="form_nilai"):
    st.subheader("Form Input Nilai Mahasiswa/Siswa")

    # Input kehadiran dengan batas maksimal 16
    kehadiran = st.number_input(
        "Jumlah Kehadiran (Maksimal 16 Pertemuan)",
        min_value=0,
        max_value=16,
        value=16,
        step=1,
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

    # Tombol Hitung / Submit Form
    tombol_hitung = st.form_submit_button(label="Hitung")

# Aksi saat tombol 'Hitung' ditekan
if tombol_hitung:
    # Rumus perhitungan nilai kehadiran
    nilai_kehadiran_terhitung = (kehadiran / 16 * 100) * (5 / 100)

    st.divider()
    st.success("Data berhasil diproses!")
    st.subheader("Hasil Perhitungan & Rekap Nilai:")

    # Tampilan Hasil
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Total Kehadiran",
            value=f"{kehadiran} dari 16",
        )
        st.metric(
            label="Nilai Kehadiran Terhitung",
            value=f"{nilai_kehadiran_terhitung:.2f}",
        )
        st.metric(label="Nilai Tugas", value=f"{nilai_tugas:.1f}")

    with col2:
        st.metric(label="Nilai UTS", value=f"{uts:.1f}")
        st.metric(label="Nilai UAS", value=f"{uas:.1f}")
