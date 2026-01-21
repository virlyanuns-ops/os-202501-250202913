
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb

---

### Judul

#### Analisis Perbandingan Performa Algoritma Page Replacement First-In, First-Out (FIFO) dan Least Recently Used (LRU) pada Sistem Memori Virtual
---

## 1. Introduction (Pendahuluan)
### 1.1 Latar Belakang

Dalam arsitektur sistem operasi modern, memori virtual memungkinkan eksekusi proses yang melampaui kapasitas fisik RAM dengan menggunakan media penyimpanan sekunder sebagai perluasan. Namun, keterbatasan jumlah frame pada RAM sering menyebabkan page fault, yaitu kondisi di mana halaman yang dibutuhkan tidak tersedia di memori utama. Untuk itu, diperlukan algoritma page replacement untuk menentukan halaman mana yang harus dikeluarkan dari memori.

Dua algoritma yang paling umum dipelajari adalah FIFO dan LRU. FIFO mengganti halaman berdasarkan urutan waktu masuknya, sedangkan LRU mengganti halaman yang sudah paling lama tidak diakses oleh sistem. Praktikum ini bertujuan untuk mensimulasikan kedua algoritma tersebut menggunakan Python guna menganalisis algoritma mana yang paling efisien dalam meminimalkan jumlah page fault.

---

## 1.2 Rumusan Masalah
1. Bagaimana perbedaan urutan penggantian halaman antara algoritma FIFO dan LRU pada reference string yang sama?

2. Apakah algoritma LRU selalu memberikan hasil page fault yang lebih rendah dibandingkan FIFO pada skenario pengujian ini?

3. Bagaimana pengaruh jumlah frame yang terbatas terhadap efisiensi manajemen memori pada laptop Axioo Hype 5?

## 1.3 Tujuan

1. Mensimulasikan logika kerja algoritma FIFO dan LRU menggunakan bahasa pemrograman Python.

2. Membandingkan metrik jumlah Page Fault dan Hit Rate antara kedua algoritma secara objektif.

3. Menganalisis keunggulan LRU dalam mengoptimalkan memori berdasarkan riwayat penggunaan akses terakhir.

---

## 2. Methods (Metode)
## 2.1 Lingkungan Pengujian

 Pengujian dilakukan pada perangkat keras dengan spesifikasi sebagai berikut untuk menjamin validitas data:

- Model Laptop: Axioo Hype 5 -2

- Processor (CPU): AMD Ryzen 5 7430U

- RAM: 8 GB

- Software: Visual Studio Code & Python 3.14.2

## 2.2 Prosedur Pengujian

1. Membuat skrip Python yang mengimplementasikan logika struktur data antrean (untuk FIFO) dan stack/timestamp (untuk LRU).

2. Menggunakan input reference string: [7, 0, 1, 2, 0, 3, 0, 4, 2, 3] dengan kapasitas 3 Frame.

3. Menjalankan skrip melalui terminal VS Code dan mencatat setiap perubahan isi memori.

Mendokumentasikan hasil akhir berupa total page fault untuk dianalisis.

## 2.3 Variabel Pengukuran

1. Page Fault: Kegagalan menemukan halaman di RAM (indikator inefisiensi).

2. Page Hit: Halaman ditemukan di RAM (indikator efisiensi).

3. Frame: Slot memori fisik yang tersedia.


---

## 3. Results (Hasil)

## 3.1 Tabel Perbandingan Output Terminal
Berdasarkan hasil simulasi Python, didapatkan data sebagai berikut:

| Hasil | Keterangan |
| :--- | :--- |
| ![screenshots](screenshots/FIFO%20Replacement%20Result.png) | fifo	Total Page Faults 9	Keterangan Lebih banyak interaksi I/O          |
| ![screenshots](screenshots/LRU%20Replacement%20Result.png) | LRU	Total Page Faults 8	Keterangan Lebih optimal

## 3.2 Analisis Hasil Pengujian

Analisis Uji Coba: Terlihat dari data di atas bahwa LRU hanya menghasilkan 7 page fault, sedangkan FIFO mencapai 9. Hal ini membuktikan bahwa pada laptop Axioo Hype 5, algoritma yang memperhatikan aktivitas terkini (LRU) jauh lebih responsif terhadap pola data yang berulang dibandingkan algoritma yang hanya berdasarkan urutan waktu (FIFO).

## 4. Discussion (Pembahasan)

## 4.1 Analisis Perbandingan Algoritma

algoritma LRU menunjukkan performa yang lebih baik dengan total 8 page faults (80.00%), sementara algoritma FIFO menghasilkan 9 page faults (90.00%). Selisih satu fault ini membuktikan bahwa LRU lebih efektif karena memanfaatkan prinsip Temporal Locality, di mana halaman yang baru saja digunakan tetap dipertahankan di memori. Sebaliknya, FIFO mengganti halaman hanya berdasarkan urutan waktu masuk tanpa mempedulikan frekuensi atau kemutakhiran akses, sehingga kurang responsif terhadap pola data yang berulang.

## 4.2 Kelebihan dan Kekurangan Algoritma
- FIFO: Mudah dikoding dan ringan, namun sering mengalami Belady's Anomaly (meningkatnya fault saat frame ditambah).

- LRU: Sangat efisien dalam menekan page fault, namun memerlukan manajemen memori yang lebih kompleks dan beban CPU sedikit lebih tinggi untuk melacak riwayat penggunaan.


## 5. Closing (Penutup)

## 5.1 Kesimpulan
simulasi menunjukkan bahwa algoritma LRU memiliki efisiensi yang lebih tinggi dengan jumlah page fault yang lebih sedikit dibandingkan FIFO. Strategi LRU dalam menyimpan halaman yang paling baru diakses terbukti efektif meningkatkan hit rate pada sistem memori virtual.

## 5.2 Saran

Untuk praktikum mendatang, disarankan mencoba algoritma Optimal Page Replacement sebagai pembanding standar tertinggi, serta menguji dengan jumlah frame yang berbeda (misal 4 atau 5) untuk melihat perubahannya secara signifikan.

---

## Daftar Pustaka

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2021). Operating System Concepts (Enhanced 10th Ed.). Wiley. (Buku standar internasional terbaru untuk teori manajemen memori).

2. Stallings, W. (2023). Operating Systems: Internals and Design Principles (10th Ed.). Pearson Education. (Membahas analisis algoritma LRU dan optimasi memori virtual modern).

3. Python Software Foundation. (2026). Official Documentation Python 3.14.2.

---

## Quiz

1. Mengapa format IMRAD membantu? Format IMRAD menyediakan struktur standar yang memisahkan data objektif (Hasil) dari analisis subjektif (Pembahasan), sehingga alur logika laporan menjadi sistematis dan transparan untuk dievaluasi secara akademik.

2. Perbedaan Hasil dan Pembahasan? Bagian Hasil menyajikan fakta mentah sesuai bukti eksekusi (seperti data 9 faults pada FIFO dan 8 faults pada LRU), sedangkan Pembahasan menjelaskan alasan teknis mengapa perbedaan tersebut terjadi dan kaitannya dengan teori sistem operasi.

3. Mengapa sitasi penting? Sitasi penting untuk menjaga integritas akademik, menghindari plagiarisme, dan membuktikan bahwa analisis yang dibuat didukung oleh literatur sah dari pakar seperti Silberschatz atau Tanenbaum.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_