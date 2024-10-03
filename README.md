# Instalasi

Berikut adalah langkah-langkah untuk menginstal proyek ini:

1. Pastikan Python sudah terinstal di sistem Anda.

2. Clone repositori ini ke komputer Anda:
   ```
   git clone https://github.com/username/nama-proyek.git
   cd nama-proyek
   ```

3. Buat dan aktifkan virtual environment (opsional tapi disarankan):
   ```
   python -m venv venv
   source venv/bin/activate  # Untuk Unix atau MacOS
   venv\Scripts\activate  # Untuk Windows
   ```

4. Jalankan skrip instalasi dependensi:
   ```
   python install_dependencies.py
   ```
   Skrip ini akan menginstal semua dependensi yang diperlukan, termasuk `web3` dan `eth-utils`.

5. Proyek Anda sekarang siap digunakan!

Catatan: Jika Anda mengalami masalah saat menjalankan `install_dependencies.py`, Anda dapat menginstal dependensi secara manual dengan menjalankan:
