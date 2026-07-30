import streamlit as st

st.title("Aplikasi Perhitungan Nilai Akhir")
st.write("Silakan masukkan nilai-nilai Anda untuk menghitung Nilai Akhir berdasarkan bobot yang ditentukan.")

# Form Input
with st.form(key="form_nilai"):
    st.subheader("Form Input Nilai")

    # Input kehadiran dengan batas maksimal 16
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

    # Tombol Submit Form
    tombol_hitung = st.form_submit_button(label="Hitung Nilai Akhir")

# Aksi saat tombol 'Hitung Nilai Akhir' ditekan
if tombol_hitung:
    # 1. Perhitungan Nilai Bobot Masing-masing Komponen
    val_kehadiran = (kehadiran / 16 * 100) * 0.05  # Bobot 5%
    val_tugas = nilai_tugas * 0.20                 # Bobot 20%
    val_uts = uts * 0.35                           # Bobot 35%
    val_uas = uas * 0.40                           # Bobot 40%

    # 2. Perhitungan Nilai Akhir Total
    nilai_akhir = val_kehadiran + val_tugas + val_uts + val_uas

    st.divider()
    st.success("Perhitungan Selesai!")

    # Tampilan Nilai Akhir secara Menonjol
    st.metric(
        label="NILAI AKHIR TOTAL",
        value=f"{nilai_akhir:.2f} / 100",
    )

    st.subheader("Rincian Bobot Nilai:")

    # Menampilkan rincian perhitungan per komponen
    col1, col2 = st.columns(2)

    with col1:
        st.write("  **Kehadiran (Bobot 5%)**")
        st.caption(f"Input: {kehadiran}/16 pertemuan")
        st.metric(label="Subtotal Kehadiran", value=f"{val_kehadiran:.2f}")

        st.write("  **Nilai Tugas (Bobot 20%)**")
        st.caption(f"Input: {nilai_tugas:.1f}")
        st.metric(label="Subtotal Tugas", value=f"{val_tugas:.2f}")

    with col2:
        st.write("  **Nilai UTS (Bobot 35%)**")
        st.caption(f"Input: {uts:.1f}")
        st.metric(label="Subtotal UTS", value=f"{val_uts:.2f}")

        st.write("  **Nilai UAS (Bobot 40%)**")
        st.caption(f"Input: {uas:.1f}")
        st.metric(label="Subtotal UAS", value=f"{val_uas:.2f}")
