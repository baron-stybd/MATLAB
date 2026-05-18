# MATLAB Sinusoidal Data Plotter 📈

Repositori ini berisi *script* MATLAB untuk membaca, memproses, dan memvisualisasikan data gelombang sinusoidal tidak murni (*unpure sinusoidal*) langsung dari *spreadsheet* Excel. *Script* ini sangat berguna untuk keperluan analisis data teknik, pemrosesan sinyal, dan penyusunan laporan akademik.

## Fitur Utama
- **Import Otomatis:** Membaca data spesifik pada rentang sel tertentu dari file `.xlsx` menggunakan fungsi `readmatrix`.
- **Data Filtering:** Pembersihan otomatis untuk baris data yang kosong atau bernilai `NaN`.
- **Visualisasi Akurat:** Menghasilkan grafik 2D yang dilengkapi dengan *grid*, label sumbu, dan garis referensi titik nol (0,0) untuk mempermudah analisis visual.

## Prasyarat
Sebelum menjalankan *script* ini, pastikan sistem kamu memiliki:
- **MATLAB** (R2019a atau lebih baru direkomendasikan untuk dukungan penuh `readmatrix`).
- **GNU Octave** (Sebagai alternatif *open-source*, pastikan *package* `io` terinstal).
- File data Excel (`.xlsx`) yang berisi kolom waktu dan nilai amplitudo.

## Instalasi & Persiapan

1. Clone repositori ini ke dalam direktori lokal kamu:
   ```bash
   git clone [https://github.com/baron-stybd/matlab-sinusoidal-plot.git](https://github.com/baron-stybd/matlab-sinusoidal-plot.git)
