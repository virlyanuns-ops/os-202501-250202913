
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : virli a'inun subroto
- **NIM**   : 250202913 
- **Kelas** : 1ikrb

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
fungsi utama sistem operasi
Sistem operasi (OS) berfungsi untuk mengelola sumber daya perangkat keras dan menyediakan layanan umum untuk aplikasi perangkat lunak.
Dan fungsinnya meliputi
1. Manajemen Proses: Membuat,menghapus,dan menjadwalkan proses
2. manajemen sumber daya 
   Mengatur dan mengoptimalkan penggunaan CPU, memori, dan penyimpanan agar aplikasi berjalan lancar.
3. Antarmuka Pengguna:
   Menyediakan cara bagi pengguna untuk berinteraksi dengan komputer.
4. Manajemen File:
   Mengelola file dan folder, termasuk membuat, menghapus, dan mengatur izin akses.
5. Keamanan:
   Melindungi sistem dari akses ilegal dan ancaman keamanan. 


---

## Dasar Teori
1. Sistem operasi (OS) adalah sebuah perangkat lunak yang mengelola sumber daya perangkat keras serata menyediakan layanan umum untuk aplikasi perangkat lunak.
2. Kernel adalah inti dari sistem operasi yang memiliki kontrol penuh atas sistem komputer yang berfungsi untuk menghubungkan hadware dan software
3. System call adalah cara aplikasi untuk meminta layanan dari kernel.
4. Arsitektur Sistem Operasi
Struktur OS berupa monolithic kernel, microkernel, atau layered architecture, yang berfungsi untuk menentukan cara OS berinteraksi satu sama lain serta mempengaruhi efektivitas dan keamanan sistem.


---

## Langkah Praktikum
1. Melakukan fork terhadap repositori yang disediakan.
2. Mengganti nama repositori hasil fork sesuai ketentuan yang sudah tersedia.
3. Melakukan clone repositori tersebut ke komputer lokal.
4. Membuat struktur folder baru di dalam repositori lokal.
5. Di dalam folder tersebut, membuat file laporan.md serta folder screenshot/.
6. Menuliskan ringkasan tentang Perbedaan *monolithic kernel*, *microkernel*, dan *layered architecture*.
   - Contoh OS yang menerapkan tiap model.
   - Analisis: model mana yang paling relevan untuk sistem modern.  
7. Menjawb kuis yang terdapat pada modul.
8. Menambahkan file laporan dan screenshot ke Git, kemudian melakukan commit dengan pesan week1-intro-arsitektur dan pust ke github.
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | headu
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/linux-1.png
)

---

## Analisis
- Jelaskan makna hasil percobaan
Hasil percobaan menunjukkan bagaimana program dan sistem operasi saling berinteraksi ketika sebuah tugas dijalankan.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
1. Kernel yaitu inti dari sistem operasi yang menghubungkan hedware dan software.
2. system call adalah cara bagi ruang pengguna untuk meminta layanan dari kernel.
3. Arsitektur os truktur yang mendasari bagaimana komponen-komponen perangkat lunak berinteraksi satu sama lain.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Linux lebih mudah melihat dan melacak system call, proses lewat terminal.
Windows memiliki alat sendiri tetapi beberapa detail implementasi cenderung lebih tertutup
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
 1. Arsitektur Kernel: monolithic kernel memang juara soal kecepatan karena semuanya terintegrasi rapat, tapi risikonya tinggi satu kesalahan saja bisa bikin sistem rusak,
 
 2. Pelajaran untuk Pengembangan Selanjutnya: Secara keseluruhan, praktikum ini mengajarkan bahwa memahami kernel architecture bukan cuma teori, tapi kunci buat bikin sistem yang tangguh. 
---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.  
   Jawaban:  1.Menjalankan Operasi Dasar  
             2.Mengatur Kinerja Perangkat
             3.Menyimpan Program atau Aplikasi

2. Jelaskan perbedaan antara *kernel mode* dan *user mode*.  
   Jawaban: kernel mode
               memiliki hak akses penuh untuk mengoperasikan ke semua sumber daya sistem tetapi rentan kesalahan/ keamanan rendah
            user mode 
                memiliki hak akses terbatas terhadap sumber daya sistem tetapi untuk sistem keamanan lebih aman karna satu kesalahan tidak akan mempengaruhi seluruh sistem
3. Sebutkan contoh OS dengan arsitektur monolithic dan 
    microkernel.  
   Jawaban :
         arsitektur monolithic:linux, microsoft windows 9x, BSD
         monolithic           : QNX, macOS,minix
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
 adaptasi dengan dunia kampus dibarengi dengan tugas praktikum ini 
- Bagaimana cara Anda mengatasinya? 
1. belajar bersama teman teman yang mau berkembang bersama
2. meminta bantuan teman yang sudah bisa dan kating

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
