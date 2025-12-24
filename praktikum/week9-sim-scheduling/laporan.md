
# Laporan Praktikum Minggu [X]
# Topik:Simulasi Algoritma Penjadwalan CPU #



---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb
---

## Tujuan
1. Membuat kode program simulasi penjadwalan CPU (FCFS atau SJF).
2. Menjalankan program menggunakan dataset yang telah ditentukan (P1–P4).
3. Menampilkan hasil perhitungan dalam format tabel atau grafik
4. Menyusun penjelasan tertulis mengenai alur dan hasil simulasi.



---

## Dasar Teori
1. Definisi Penjadwalan CPU
Penjadwalan CPU adalah proses yang menentukan proses mana dalam antrean ready yang akan dialokasikan ke CPU untuk dieksekusi. 

2. Kriteria PenjadwalanUntuk mengukur kinerja algoritma penjadwalan, terdapat beberapa parameter utama yang digunakan dalam simulasi:Waiting Time (WT): Total waktu yang dihabiskan suatu proses untuk menunggu di antrean ready.Turnaround Time (TAT): Total waktu dari saat proses tiba hingga proses tersebut selesai dieksekusi (TAT = Completion\ Time - Arrival\ Time).Burst Time: Waktu yang dibutuhkan oleh proses untuk menyelesaikan eksekusinya pada CPU.Arrival Time: Waktu saat proses masuk ke dalam antrean ready.
3. Algoritma FCFS (First-Come, First-Served)
FCFS adalah algoritma penjadwalan CPU yang paling sederhana. Sifat utamanya adalah
Non-preemptive: Sekali CPU dialokasikan ke sebuah proses, proses tersebut akan memegang CPU sampai selesai atau memintanya berhenti.
Prinsip Antrean: Proses yang meminta CPU pertama kali akan dilayani terlebih dahulu (FIFO).
Kelemahan: Berpotensi menyebabkan Convoy Effect, di mana proses-proses pendek harus menunggu sangat lama karena ada proses panjang yang sedang berjalan di depannya.
4. Algoritma SJF (Shortest Job First)
SJF memprioritaskan proses yang memiliki Burst Time terkecil untuk dikerjakan lebih dulu.
SJF Non-preemptive: Jika ada proses baru datang dengan Burst Time lebih pendek saat proses lain sedang berjalan, CPU tidak akan berpindah hingga proses yang sedang berjalan selesai.
Optimalitas: Secara teoritis, SJF memberikan rata-rata Waiting Time minimum untuk sekumpulan proses tertentu.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
1. Alur Kerja Program
Program memproses dataset yang berisi Arrival Time (waktu kedatangan) dan Burst Time (durasi eksekusi) dari setiap proses.
- Program terlebih dahulu mengurutkan data berdasarkan waktu kedatangan terkecil.
- Pada algoritma FCFS, CPU melayani proses pertama (P1) hingga selesai, kemudian melanjutkan ke proses berikutnya tanpa interupsi (non-preemptive).
- Waktu tunggu (Waiting Time) dihitung berdasarkan selisih antara waktu mulai eksekusi dengan waktu kedatangan proses tersebut.

2. Perbandingan dengan Perhitungan Manual
Berdasarkan hasil eksekusi program terhadap dataset uji:

- Hasil perhitungan otomatis menunjukkan rata-rata Waiting Time sebesar 8.75 dan Turnaround Time sebesar 14.75.

- Hasil ini sepenuhnya konsisten dan sesuai dengan perhitungan manual yang dilakukan pada pertemuan sebelumnya.

- Hal ini memvalidasi bahwa logika algoritma yang diimplementasikan ke dalam kode sudah akurat.

3. Kelebihan dan Keterbatasan Simulasi
- Kelebihan: Simulasi ini memungkinkan pengolahan data dalam jumlah besar secara instan dan meminimalkan risiko kesalahan hitung manusia (human error).

- Keterbatasan: Simulasi ini bersifat sederhana dan berbasis terminal, sehingga belum mempertimbangkan overhead sistem operasi yang nyata seperti waktu untuk context switching antar proses.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
karena lingkungan sistem operasi yang asli sangat kompleks. Dengan simulasi, kita bisa memprediksi performa algoritma (seperti efisiensi CPU dan waktu tunggu) dalam berbagai skenario tanpa harus mengganggu operasional sistem yang sebenarnya.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
Pada dataset besar, perhitungan manual sangat rentan terhadap human error (salah hitung) dan memakan waktu sangat lama. Simulasi komputer memberikan akurasi matematis yang konsisten dan kecepatan eksekusi yang stabil terlepas dari jumlah datanya.

3. Algoritma mana yang lebih mudah diimplementasikan? 
FCFS (First-Come, First-Served) adalah yang paling mudah diimplementasikan karena logikanya hanya menggunakan struktur data antrean (Queue) sederhana berdasarkan waktu kedatangan, tanpa perlu melakukan pemilahan ulang (sorting) burst time setiap kali ada proses baru masuk (seperti pada SJF).



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
