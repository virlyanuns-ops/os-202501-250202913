
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  :virlil a'inun susbroto  
- **NIM**   :250202913 
- **Kelas** :1 ikrb

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/week3.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari perintah chmod?
Perintah chmod berfungsi untuk mengubah izin akses  pada (file) atau direktori dalam sistem operasi Linux dan sistem operasi berbasis Unix lainnya. Izin akses 
digunakan untuk mengatur izin untuk tiga kategori pengguna:Pemilik (User/Owner),Grup (Group),Lainnya (Others/World)
2. Apa arti dari kode permission rwxr-xr--?
Rwx :untuk pemilik berkas/user
  w (write): Pemilik berkas memiliki izin untuk mengubah atau menulis ke berkas. 
  x (execute): Pemilik berkas memiliki izin untuk menjalankan berkas (jika berkas tersebut adalah program yang dapat dieksekusi)
  atau masuk ke dalam direktori.
r-x:untuk grup
   	r (read): Anggota grup memiliki izin untuk membaca berkas.
  	- (no write): Anggota grup tidak memiliki izin untuk mengubah atau menulis ke berkas.
   	x (execute): Anggota grup memiliki izin untuk menjalankan berkas.
r-- :untuk lainnya/others
3. Jelaskan perbedaan antara chown dan chmod?

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
