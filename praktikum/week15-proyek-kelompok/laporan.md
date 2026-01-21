
### README.md
---
### Mini Simulasi 
---
Sistem Operasi
Aplikasi berbasis terminal (CLI) ini dibuat untuk mensimulasikan dua konsep inti Sistem Operasi: CPU Scheduling dan Memory Management. Proyek ini dikembangkan sebagai Tugas Praktikum Minggu 15.


### Fitur Utama
---
1. Simulasi Pemutaran Musik (CPU Scheduling)

    - Algoritma: First-Come First-Served (FCFS).
    - Analogi: Antrean pemutaran lagu (Playlist). Lagu yang masuk ke antrean lebih awal akan diputar hingga selesai sebelum lagu berikutnya dimulai.
    - Output: Tabel detail yang mencakup Waktu Datang, Durasi Musik, Waktu Selesai, Turnaround Time (TAT), dan Waktu Tunggu.

2. Simulasi Multitasking Laptop (Memory Management)

    - Algoritma: First-In First-Out (FIFO) Page Replacement.

    - Analogi: Manajemen RAM pada laptop dengan kapasitas terbatas (3 Slot). Jika RAM penuh dan aplikasi baru dibuka, aplikasi yang paling lama berada di RAM akan dihapus.

    - Output: Visualisasi status HIT (aplikasi sudah ada di RAM) atau MISS (aplikasi harus dimuat ke RAM/menggantikan yang lama).
---

### Struktur Folder
---

``` Plaintext
code/
├── main.py              # Entry point aplikasi (Menu Utama)
├── cpu_scheduling.py    # Modul logika FCFS (Simulasi Musik)
├── page_replacement.py  # Modul logika FIFO (Simulasi RAM)
├── Dockerfile           # Konfigurasi container Docker
├── README.md            # Dokumentasi ini
└── data/                # Dataset simulasi
    ├── processes.csv    # Data untuk antrean musik
    └── pages.txt        # Data riwayat penggunaan aplikasi 

```
---
### Cara Menjalankan
---
aplikasi telah berhasil di-build dan dijalankan menggunakan Docker dengan nama image pemutaran_musik.

### Cara 1: Menggunakan Docker (Disarankan)
Pastikan Docker Desktop / Docker Engine sudah terinstal dan berjalan.
1. Build Image Buka terminal di dalam folder code/, lalu jalankan:

```docker build -t pemutaran_musik .```

2. Jalankan Container Gunakan run -it agar bisa berinteraksi dengan menu aplikasi:


```docker run -it pemutaran_musik```


### Cara 2: Menjalankan Secara Manual (Local Host)


```python main.py```


### Analisis Hasil Simulasi 
1. Hasil CPU Scheduling (Simulasi Musik)
Berdasarkan data lagu seperti Blue - Yung Kai dan Untitled - Rex Orange, diperoleh performa sistem sebagai berikut:

- Rata-rata Turnaround Time (TAT): 8.60

- Rata-rata Waiting Time: 5.00

2. Hasil simulasi  Multitasking leptop (Management RAM)
Simulasi dilakukan dengan kapasitas 3 Slot RAM:
- Total MISS: 5 (Terjadi saat aplikasi baru harus dimuat ke slot kosong atau mengganti aplikasi lama).
- Skor HIT: 37.50% (Terjadi saat aplikasi yang diminta sudah tersedia di RAM, seperti pada langkah ke-4, 6, dan 8).
- Aplikasi yang disimulasikan: Chrome, Spotify, Word, VS Code, dan Zoom.

---
### Konfigurasi Dataset
---
Anda dapat mengubah data simulasi di folder data/:
1. data/processes.csv 
    - Format: NamaMusik,WaktuDatang,Durasi

contoh:
``` 
Nama Musik, Waktu Datang, Durasi Musik
Blue - Yung Kai, 0, 3
Untitled - Rex Orange, 1, 3
Peradaban - Feast., 2, 5
Sial - Mahalini, 3, 4
Double Take - Dhruv, 4, 3
```
2. data/pages.txt 
    - Format: Nama aplikasi

contoh:
```Chrome,Spotify,Word,Chrome,VS Code,Spotify,Zoom,Word```