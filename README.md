# Sistem-Parkir-Python
Program Python untuk mensimulasikan sistem parkir otomatis yang menghitung tarif berdasarkan jenis kendaraan (mobil/motor), durasi, serta denda jika melebihi batas waktu.


# Sistem Parkir Otomatis (Python)

Program Python sederhana yang dirancang untuk mensimulasikan perhitungan tarif parkir otomatis berdasarkan aturan waktu masuk/keluar, jenis kendaraan, dan durasi menginap. Proyek ini dibuat untuk melatih penerapan logika percabangan bertingkat (`if-elif-else`) serta manipulasi data waktu/angka.

## Aturan & Fitur Sistem
* **Jenis Kendaraan:** Mendukung dua jenis kendaraan, yaitu **Motor** dan **Mobil**.
* **Validasi Waktu:** Jam masuk dan keluar harus berada di rentang format 24 jam (`0-23`). Jika tidak valid, program akan menolak proses.
* **Perhitungan Tarif Progresif:**
  * **Motor:** Rp2.000/jam untuk 2 jam pertama, lalu Rp1.000/jam untuk jam berikutnya.
  * **Mobil:** Rp5.000/jam untuk 2 jam pertama, lalu Rp3.000/jam untuk jam berikutnya.
* **Sistem Denda:** Jika durasi parkir melebihi **12 jam**, maka akan dikenakan denda tambahan sebesar **Rp50.000**.
* **Lintas Hari (Overnight):** Mampu menghitung durasi parkir meskipun melewati pergantian hari (misal jam masuk 22.00, jam keluar 02.00).

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal di komputer Anda.
2. Unduh atau *clone* repositori ini.
3. Buka terminal atau *command prompt*, lalu jalankan perintah berikut:
   ```bash
   python parkir.py
