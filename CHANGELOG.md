# Changelog

Semua perubahan penting pada script ini akan didokumentasikan di sini.

## 1.0.0 (2025-07-11)


### Bug Fixes

* **log:** correct log message formatting ([4357995](https://github.com/kevlog/ibzg/commit/43579958526f2d2543a8f4bb6efba60a976fcd9e))

## [v1.0.0] - Versi Dasar - Pengumpulan File ATU
### Added
- Menyalin file `002-Invoice-Data-ATU Platform*.txt` dari seluruh subfolder
- Mengumpulkan file ke dalam folder `Invoice ATU {Nama Folder Sumber}`

---

## [v1.1.0] - Kloning dan Ganti File ATU
### Added
- Membuat duplikat folder sumber menjadi `{Nama Folder} Done`
- Mengganti file `002-Invoice-Data-ATU Platform*.txt` dalam `Done` dengan versi terenkripsi dari folder `Invoice ATU`

---

## [v1.2.0] - Pengecualian File ATM dan Folder Masking
### Added
- Mengecualikan file `002-Invoice-Data-ATM Platform*.txt` dari proses kloning
- Menyalin file ATM ke folder `Masking` (tanpa struktur subfolder)
- Menjamin folder `Done` hanya berisi file selain ATM

---

## [v1.3.0] - ZIP Per Subfolder + Output ke BoBo-zip
### Added
- Input bulan dan tahun dari user
- Melakukan zip pada setiap subfolder (`01`, `02`, dst.) dalam folder `Done`
- Nama file zip mengikuti format: `H-002{YY}{MM}{DD}.zip`
- Output zip disimpan di folder `BoBo-zip`

---

Note: v1.3.0 menjadi v.1.0.0