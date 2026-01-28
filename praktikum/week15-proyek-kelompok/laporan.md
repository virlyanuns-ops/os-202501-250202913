# Laporan Praktikum Minggu [15]
Topik: mini projek sistem operasi
---
 ### 1. PENDAHULUAN
 ---
### A. Latar Belakang
Sistem operasi merupakan komponen perangkat lunak fundamental yang bertugas mengelola sumber daya perangkat keras serta menjembatani interaksi antara pengguna dan komputer. Konsep-konsep inti seperti manajemen memori dan penjadwalan CPU sering kali bersifat abstrak, sehingga diperlukan visualisasi konkret untuk memahami mekanisme kerja internal sistem dalam menangani tugas-tugas komputasi.

Proyek ini, yang bertajuk "Mini projek Sistem Operasi", dikembangkan sebagai tugas praktikum integratif untuk mengimplementasikan teori sistem operasi ke dalam aplikasi berbasis terminal yang fungsional. Sesuai dengan spesifikasi tugas, aplikasi ini menggabungkan dua modul utama yang merepresentasikan aktivitas multitasking pada perangkat komputer sehari-hari:

1. Simulasi Penjadwalan CPU (Simulator Musik)
Modul ini mengimplementasikan algoritma First-Come First-Served (FCFS) untuk mensimulasikan antrean pemutaran musik. Proses diurutkan berdasarkan Waktu Datang, di mana setiap lagu diproses hingga selesai sebelum beralih ke lagu berikutnya.

2. Simulasi Manajemen RAM (Multitasking Laptop)
Modul ini memodelkan kebijakan Page Replacement menggunakan algoritma FIFO (First-In First-Out) untuk mengelola keterbatasan memori. Simulasi ini menggambarkan bagaimana sistem operasi merespons saat kapasitas RAM (yang dibatasi sebanyak 3 slot) telah penuh:

3. Implementasi Docker untuk Reproducibility
Untuk menjamin aplikasi dapat berjalan secara konsisten di berbagai lingkungan (Windows, Linux, atau macOS), proyek ini didistribusikan menggunakan teknologi Docker. Dengan menggunakan base image python:3.11-slim, seluruh dependensi dan kode sumber dibungkus ke dalam container sehingga proses demonstrasi dan penilaian proyek dapat dilakukan tanpa hambatan konfigurasi sistem.

---

### B Tujuan Proyek
1.Mahasiswa mampu menyatukan minimal dua modul teori sistem operasi, yaitu Penjadwalan CPU (menggunakan algoritma FCFS) dan Manajemen Memori (menggunakan algoritma FIFO), ke dalam satu aplikasi praktis.

2. Mahasiswa mampu mengukur performa sistem melalui metrik nyata, seperti menghitung rata-rata Turnaround Time (TAT) dan Waiting Time pada penjadwalan CPU, serta menghitung Skor HIT dan Total MISS pada manajemen RAM.

3. Menjamin aplikasi memiliki reproducible environment dengan menggunakan Docker, sehingga aplikasi dapat dibangun (build) dan dijalankan (run) secara konsisten di berbagai perangkat tanpa kendala dependensi.

4. Melatih kemampuan kerja sama tim dalam pembagian peran (Integrator, Developer, QA) serta menyusun laporan proyek yang sistematis dan mudah dipahami.

5. Mahasiswa mampu menyajikan data kompleks dari aktivitas multitasking laptop dan pemutaran musik ke dalam bentuk tabel ASCII yang informatif dan mudah dibaca oleh pengguna melalui terminal.

---
### 2. ARSITEKTUR APLIKASI
---
### A. Desain Arsitektur Umum
Aplikasi "Mini Simulasi Sistem Operasi" dibangun menggunakan arsitektur modular berbasis Command Line Interface (CLI) dengan bahasa pemrograman Python. Struktur ini memisahkan logika utama program dengan algoritma simulasi agar kode lebih terorganisir dan mudah dikembangkan.

Secara garis besar, arsitektur aplikasi ini terdiri dari dua komponen utama:


- Modul Logika (Logic Modules): Berisi berkas terpisah untuk algoritma spesifik:
    - cpu_scheduling.py: Mengelola simulasi "Simulator Musik" dengan algoritma FCFS untuk menghitung waktu tunggu dan turnaround time.

    - page_replacement.py: Mengelola simulasi "Manajemen RAM" dengan algoritma FIFO untuk menentukan status HIT atau MISS pada slot memori.

- Manajemen Data (Data Layer): Mengatur penyimpanan dataset input (seperti daftar musik atau daftar aplikasi) dalam format file teks (.csv atau .txt) di dalam folder data/.
### B. Deskripsi Modul
Aplikasi ini mengintegrasikan dua modul utama yang mensimulasikan fungsi kritis dalam sistem operasi:

1. Modul Penjadwalan CPU (Simulator Musik)
Modul ini mensimulasikan bagaimana CPU mengelola antrean proses menggunakan analogi daftar putar musik.

    - Algoritma: Menggunakan First-Come First-Served (FCFS).

    - Mekanisme: Setiap lagu (proses) yang masuk pertama kali akan diputar hingga durasinya selesai sebelum beralih ke lagu berikutnya.

    - Output: Tabel yang menampilkan Waktu Datang, Durasi, Waktu Selesai, Turnaround Time (TAT), dan Waktu Tunggu (Waiting Time). Berdasarkan simulasi, diperoleh rata-rata TAT sebesar 8.60 dan rata-rata Waktu Tunggu 5.00.

2. Modul Manajemen Memori (Simulasi RAM Laptop)
Modul ini memvisualisasikan cara sistem operasi mengelola aplikasi di dalam RAM yang memiliki kapasitas terbatas.

    - Algoritma: Menggunakan Page Replacement tipe FIFO (First-In First-Out).

    - Mekanisme: Jika RAM penuh (3 slot terisi), aplikasi yang paling lama berada di memori akan dihapus secara otomatis untuk memberi ruang bagi aplikasi baru.

    - Output: Status HIT (aplikasi sudah ada di RAM) dan MISS (aplikasi harus dimuat ulang). Hasil akhir menunjukkan Total MISS sebanyak 5 kali dan efisiensi Skor HIT sebesar 37.50%.
### C. Alur Data
Alur data dalam aplikasi ini dirancang secara sistematis untuk memastikan transisi dari input pengguna hingga menjadi output tabel metrik berjalan dengan lancar. Proses ini dibagi menjadi empat tahapan utama:

- Input Data:
    - Sistem menerima dataset awal berupa daftar aplikasi untuk RAM dan daftar musik untuk penjadwalan CPU.
    - Data ini dapat berasal dari list internal program atau file eksternal (CSV/TXT) yang disimpan di direktori data/.

- Pemrosesan Modul:
    - Modul Penjadwalan: Data musik (Waktu Datang dan Durasi) diolah menggunakan logika FCFS untuk menentukan urutan eksekusi.
    - Modul Manajemen RAM: Setiap aplikasi yang dipanggil dicek keberadaannya di dalam slot RAM yang terbatas (3 slot) menggunakan logika antrean FIFO.

- Kalkulasi Metrik:
    - Sistem menghitung secara otomatis nilai-nilai statistik berdasarkan hasil pemrosesan.
    - Untuk CPU, dihitung nilai Turnaround Time (TAT) dan Waiting Time.
    - Untuk RAM, dihitung jumlah MISS (kegagalan muat) dan Skor HIT (efisiensi memori).

- Output Visual:
    - Hasil akhir ditampilkan ke terminal dalam bentuk tabel ASCII yang rapi.
    - Pengguna diberikan pilihan untuk mengulangi simulasi (y/n) atau kembali ke menu utama melalui antarmuka CLI.

---
### 3. Demo Langsung Menjalankan Aplikasi
kami menyusun panduan instalasi dan eksekusi lengkap pada berkas code/README.md yang disertakan dalam repositori ini. Demo aplikasi dilakukan menggunakan Docker untuk menjamin konsistensi lingkungan kerja dan hasil yang stabil.

### 3.1 Lingkungan Demo (Environment)
Demo aplikasi ini dijalankan pada lingkungan terisolasi menggunakan Docker Container:

- Base Image: Menggunakan python:3.9-slim (untuk modul Page Replacement) dan python:3.11-slim (untuk modul Simulator Musik).

- Struktur Container: Seluruh kode sumber (Page_Replacement.py dan pemutaran_musik.py) disalin ke dalam direktori kerja /app di dalam container melalui instruksi COPY pada Dockerfile.

### 3.2 Prosedur Demo
Berikut adalah ringkasan prosedur demo yang dilakukan berdasarkan bukti eksekusi terminal:

1. Tahap Build Image:
    - Kami membangun citra Docker untuk manajemen memori dengan perintah: docker build -t page-replacement .

    - Kami membangun citra Docker untuk simulator musik dengan perintah: docker build -t pemutaran_musik .

    - Proses ini memastikan seluruh dependensi dan skrip Python terintegrasi dengan benar dalam image.

2. Tahap Eksekusi (Run):

    - Modul Memori: Container dijalankan menggunakan perintah docker run --rm page-replacement untuk mensimulasikan algoritma FIFO.

    - Modul Musik: Container dijalankan dalam mode interaktif menggunakan perintah docker run -it pemutaran_musik.

    - Penggunaan flag --rm memastikan sistem host tetap bersih setelah aplikasi dihentikan.

### 3.3 Bukti Eksekusi

- Skenario 1 (Scheduling Musik): Menampilkan antrean lagu seperti "Blue - Yung Kai" hingga "Double Take - Dhruv" dengan perhitungan Waiting Time dan Turnaround Time (TAT) yang presisi.
![screenshots](screenshots/Docker_Build_Scheduling.jpeg)

- Skenario 2 (Management RAM): Menjalankan simulasi penggantian halaman (Page Replacement) menggunakan algoritma FIFO dalam lingkungan Docker terisolasi.

![screenshots](screenshots/docker_build_page_replacment.jpeg)

---
### 4. Hasil Pengujian dan Analisis
---
### A. Hasil Pengujian Modul A (CPU Scheduling - FCFS)
Skenario Pengujian: Kami mensimulasikan penjadwalan pemutaran musik menggunakan algoritma First-Come First-Served (FCFS) dengan dataset antrean sebagai berikut:

- Blue – Yung Kai: Waktu Datang 0, Durasi 3
- Untitled – Rex Orange: Waktu Datang 1, Durasi 3
- Peradaban – Feast.: Waktu Datang 2, Durasi 5
- Sial – Mahalini: Waktu Datang 3, Durasi 4
- Double Take – Dhruv: Waktu Datang 4, Durasi 3

Hasil Output Aplikasi: Berikut adalah tabel hasil simulasi pemutaran musik yang dihasilkan oleh sistem:
![screenshots](screenshots/Docker_run_Scheduling.jpeg)

### Tabel Hasil Simulasi Penjadwalan (FCFS)

| Nama Musik | Waktu Datang | Durasi Musik | Waktu Selesai | TAT | Waktu Tunggu |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Blue - Yung Kai | 0 | 3 | 3 | 3 | 0 |
| Untitled - Rex Orange | 1 | 3 | 6 | 5 | 2 |
| Peradaban - Feast. | 2 | 5 | 11 | 9 | 4 |
| Sial - Mahalini | 3 | 4 | 15 | 12 | 8 |
| Double Take - Dhruv | 4 | 3 | 18 | 14 | 11 |

Metrik Akhir:
- Rata-rata Turnaround Time (TAT): 8.60

- Rata-rata Waiting Time (Waktu Tunggu): 5.00

Analisis Kinerja
Berdasarkan hasil simulasi menggunakan algoritma First-Come First-Served (FCFS) pada sistem pemutaran musik:

1. Mekanisme Kerja: Musik diputar secara berurutan berdasarkan waktu kedatangannya. Musik pertama (Blue) langsung diputar tanpa waktu tunggu (0), sementara musik berikutnya harus menunggu musik sebelumnya selesai.

2. Akumulasi Waktu Tunggu: Terlihat adanya peningkatan waktu tunggu yang signifikan seiring bertambahnya antrean. Musik terakhir (Double Take) harus menunggu selama 11 satuan waktu meskipun durasinya hanya 3.

3. Kesimpulan: Meskipun algoritma ini adil secara urutan kedatangan, FCFS mengakibatkan rata-rata waktu tunggu menjadi cukup tinggi (5.00) karena musik yang datang kemudian selalu bergantung pada penyelesaian seluruh durasi musik di depannya.

### B. Laporan Pengujian Modul B (Page Replacement - FIFO)
Skenario Pengujian: Kami mensimulasikan manajemen RAM laptop menggunakan dataset riwayat aplikasi dengan urutan akses: Chrome, Spotify, Word, Chrome, VS Code, Spotify, Zoom, Word. Kapasitas RAM diset menjadi 3 Slot (frames).

Hasil Output Aplikasi:

Berikut adalah screnshoots hasil simulasi yang dihasilkan:

![screenshots](screenshots/docker_run_page_replacment.jpeg)

Berdasarkan eksekusi pada terminal, berikut adalah tabel perubahan isi RAM pada setiap langkah:

| Step | Aplikasi | Isi RAM (Slot) | Status | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Chrome | `[ Chrome ]` |  **FAULT** | Load awal ke slot kosong |
| **2** | Spotify | `[ Chrome, Spotify ]` |  **FAULT** | Load awal ke slot kosong |
| **3** | Word | `[ Chrome, Spotify, Word ]` |  **FAULT** | Load awal ke slot kosong |
| **4** | Chrome | `[ Chrome, Spotify, Word ]` |  **HIT** | Aplikasi tersedia di RAM |
| **5** | VS Code | `[ Spotify, Word, VS Code ]` |  **FAULT** | **RAM Penuh!** Hapus Chrome (Terlama) |
| **6** | Spotify | `[ Spotify, Word, VS Code ]` | **HIT** | Aplikasi tersedia di RAM |
| **7** | Zoom | `[ Word, VS Code, Zoom ]` | **FAULT** | **RAM Penuh!** Hapus Spotify (Terlama) |
| **8** | Word | `[ Word, VS Code, Zoom ]` | **HIT** | Aplikasi tersedia di RAM |



Metrik Akhir:

- Total Referensi Aplikasi: 8

- Total Page FAULT: 5 kali

- HIT Ratio: 37.50%

Analisis :

- algoritma FIFO (First-In First-Out) bekerja dengan prinsip menghapus data yang pertama kali masuk ketika kapasitas RAM sudah penuh.

-  Dari 8 percobaan akses, sistem berhasil melakukan HIT sebanyak 3 kali (Chrome, Spotify, dan Word). Ini terjadi karena aplikasi tersebut masih tersimpan di RAM saat dipanggil kembali.

- Kelemahan FIFO: Pada langkah ke-5, Chrome dihapus karena merupakan aplikasi tertua (masuk di Step 1), padahal Chrome baru saja diakses di Step 4. Jika setelah Step 8 Chrome dipanggil lagi, maka akan terjadi Fault kembali.

- Kesimpulan: Meskipun sederhana dan ringan secara komputasi, FIFO kurang responsif terhadap aplikasi yang sering digunakan kembali jika aplikasi tersebut sudah "tua" di dalam antrean. Untuk meningkatkan Hit Ratio, algoritma seperti LRU (Least Recently Used) mungkin akan memberikan hasil yang lebih baik pada pola penggunaan ini.

### 5. Pembagian Peran dan Kontribusi
kolaboratif bembagian tugas

![screenshots](screenshots/comit.png)

Identitas  rincian peran dan kontribusi setiap anggota tim:



|         Nama         | Kelas  |    NIM    |           Peran            |
| :------------------: | :----: | :-------: | :------------------------: |
|    Muhamad Juhan     | 1 IKRB | 250202953 | Projejct Lead & Integrator |
|       Safrudin       | 1 IKRB | 250202966 |        Developer 1         |
| Ahmad Wildan Asrovi  | 1 IKRB | 250202927 |        Developer 2         |
| Virli A'inun Subroto | 1 IKRB | 250202913 |     Documentation & QA     |



---

## Quiz

1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya? 
jawaban: Tantangan terbesar adalah menyatukan dua logika yang berbeda (penjadwalan CPU dan manajemen memori) agar bisa berjalan dalam satu menu CLI yang konsisten tanpa terjadi error saat input data. Solusinya adalah menggunakan arsitektur modular, di mana setiap logika fungsi dipisahkan ke dalam file berbeda agar kode lebih rapi dan mudah diperbaiki jika ada kesalahan.

2. Mengapa Docker membantu proses demo dan penilaian proyek? 
jawaban: Docker sangat membantu karena membungkus aplikasi dan semua dependensinya ke dalam satu container, sehingga aplikasi pasti berjalan sama di komputer mana pun tanpa kendala perbedaan versi sistem operasi atau pustaka. Hal ini memastikan tidak ada masalah "jalan di komputer saya tapi tidak di komputer orang lain" saat demo atau penilaian dilakukan.

3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? 
jawaban: Modul Manajemen RAM (Page Replacement) akan paling terdampak karena dengan dataset yang 10x lebih besar namun kapasitas slot RAM tetap terbatas (hanya 3 slot), sistem akan jauh lebih sering melakukan penghapusan dan penggantian aplikasi. Hal ini mengakibatkan jumlah Total MISS meningkat drastis, sehingga performa simulasi akan melambat karena sistem terus-menerus memuat ulang data.

---
## Kesimpulan
Proyek "Mini projek Sistem Operasi" ini berhasil membuktikan bahwa konsep rumit dalam sistem operasi bisa dipelajari dengan lebih mudah melalui simulasi sederhana berbasis baris perintah (CLI). Kami berhasil mengintegrasikan konsep penjadwalan CPU dan manajemen memori ke dalam satu aplikasi simulasi berbasis terminal yang berjalan lancar menggunakan Docker. Dari hasil uji coba, algoritma FCFS pada simulator musik menghasilkan rata-rata waktu tunggu 5.00, sementara algoritma FIFO pada RAM laptop menunjukkan skor efisiensi (HIT) sebesar 37.50% dengan 5 kali kegagalan muat data (MISS) karena keterbatasan slot memori. Proyek ini membuktikan bahwa meskipun memori terbatas, sistem operasi tetap bisa mengatur jalannya banyak aplikasi secara bergantian, dan penggunaan Docker sangat memudahkan kami untuk memastikan aplikasi bisa langsung dijalankan di komputer mana pun tanpa pusing memikirkan instalasi tambahan.

 
---
