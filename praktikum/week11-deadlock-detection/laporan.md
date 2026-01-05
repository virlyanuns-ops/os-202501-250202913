
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock
---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

## Dasar Teori
- Deadlock: Kondisi di mana sekumpulan proses saling menunggu sumber daya yang dipegang oleh proses lain dalam kelompok tersebut, sehingga tidak ada proses yang bisa berjalan.

- Syarat Coffman:

   Mutual Exclusion: Sumber daya hanya bisa digunakan satu proses pada satu waktu.

   Hold and Wait: Proses memegang sumber daya sambil menunggu sumber daya lain.

   No Preemption: Sumber daya tidak bisa diambil paksa; harus dilepas sukarela.

   Circular Wait: Terjadi rantai sirkular di mana proses saling menunggu satu sama lain.
- Strategi :

   Bersifat reaktif: Membiarkan sistem berjalan, lalu memeriksa adanya siklus secara berkala.

   Menggunakan Resource Allocation Graph (RAG) atau algoritma pelacakan request untuk mengidentifikasi proses yang terjebak.

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Perintah untuk mengambil data proses dan sumber daya dari file .csv.
``import pandas as pd
df = pd.read_csv('dataset_deadlock.csv')``

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
Membaca dataset CSV
Membentuk Wait-For Graph
Menampilkan hasil
---

## Analisis
- Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
- Kaitkan hasil dengan teori deadlock (empat kondisi).

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1.  Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
- deadlock prevention:Memastikan salah satu dari 4 syarat deadlock (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait) tidak pernah terpenuhi.
- avoidance:Memeriksa setiap permintaan sumber daya secara dinamis untuk memastikan sistem tetap dalam "Safe State".
- detection:Membiarkan deadlock terjadi, lalu mengidentifikasinya menggunakan algoritma tertentu.

2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
  deadlock Tidak membatasi penggunaan sumber daya, sehingga CPU dan memori bisa bekerja pada kapasitas penuh tanpa aturan yang menghambat.
  hal ini membuat deteksi deadlock dipilih karena lebih praktis dan tidak membebani performa sistem dibandingkan pencegahan yang terlalu kaku.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

| Kelebihan | Kekurangan |
| :--- | :--- |
| **Sumber daya selalu terpakai maksimal.** Sistem tidak membatasi penggunaan sumber daya yang tersedia. | **Risiko kehilangan progres kerja.** Pemulihan seringkali mengharuskan penghentian proses secara paksa. |
| **Cocok untuk sistem dinamis.** Tidak perlu memprediksi kebutuhan sumber daya di masa depan (unpredictable). | **Beban CPU (Overhead).** Menjalankan algoritma pengecekan siklus membutuhkan tenaga komputasi. |
| **Tidak ada batasan kaku.** Proses berjalan lebih bebas tanpa aturan pencegahan yang menghambat kinerja. | **Potensi Starvation.** Proses yang sama bisa terus-menerus dipilih untuk dimatikan saat pemulihan. |

---


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
