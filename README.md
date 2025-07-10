
# IBZG

IBGZ (Invoice Backdate Zip Generator)

Script Python ini digunakan untuk membantu pengelolaan file invoice `.txt` dalam folder bulanan, terutama untuk kasus ATU dan ATM platform. Script ini terdiri dari beberapa versi bertahap.

## 📦 Kebutuhan Sistem

- Python 3.7+
- Modul standar: `os`, `shutil`, `zipfile`

## 🚀 Cara Penggunaan

1. Jalankan script dengan Python.
2. Masukkan path folder sumber, contoh:
   ```
   C:\Users\PC-Username\Documents\Maret 2025
   ```
3. File ATU akan disalin ke folder:
   ```
   Invoice ATU Maret 2025
   ```
4. Setelah enkripsi manual selesai, tekan ENTER.
5. Script akan:
   - Membuat folder `Maret 2025 Done`
   - Memindahkan file ATM ke folder `Masking`
   - Mengganti file ATU dengan versi terenkripsi
   - Meminta input bulan dan tahun
   - Membuat ZIP untuk setiap subfolder ke dalam folder `BoBo-zip`

## 📁 Struktur Folder Hasil

```
Maret 2025
├─ 01
│  └─ 002-Invoice-Data-ATU Platform-*.txt
├─ 02
│  └─ ...
Invoice ATU Maret 2025
└─ 002-Invoice-Data-ATU Platform-*.txt
Masking
└─ 002-Invoice-Data-ATM Platform-*.txt
Maret 2025 Done
├─ 01
│  └─ (file terenkripsi)
BoBo-zip
├─ H-002250301.zip
└─ H-002250302.zip
```

## 📌 Catatan

- Script **tidak melakukan enkripsi otomatis** — proses enkripsi dilakukan manual oleh user.
- Nama file `.zip` mengikuti format: `H-002YYMMDD.zip`
- Jika ada file ATM duplikat, otomatis akan diberi suffix (`_1`, `_2`, dst.)

## 📘 Lihat Juga

- [CHANGELOG.md](CHANGELOG.md) untuk riwayat perubahan versi.
