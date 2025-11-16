
# Laporan Praktikum Minggu [6]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb
---

## Tujuan:

1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
3. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
4. Membandingkan performa algoritma RR dan Priority.
5. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
6. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
1. Round Robin Lebih Unggul Algoritma Round Robin (RR) dengan q=3 menunjukkan efisiensi keseluruhan yang lebih baik dibandingkan Priority Scheduling (Non-Preemptive) untuk set data ini.
2. Round Robin (RR)Mendistribusikan Beban Secara Merata dengan menawarkan keadilan yang jauh lebih tinggi.
3. Priority Scheduling Gagal Mengoptimalkan
Meskipun Priority Scheduling seharusnya efisien untuk proses penting, kinerjanya terhambat oleh proses dengan prioritas terendah.
---

## Langkah Praktikum
1. Eksperimen 1   – Round Robin (RR)
- Menggunakan time quantum (q) = 3.
- Menghitung waiting time dan turnaround time untuk tiap proses.
- Mensimulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
`| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...`
- Mencatatat sisa burst time tiap putaran.

2. Eksperimen 2 – Priority Scheduling (Non-Preemptive)
 - Mengurutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
- Melakukan perhitungan manual untuk:
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
- Membuat tabel perbandingan hasil RR dan Priority.

3. Eksperimen 3 
– Analisis Variasi Time Quantum (Opsional)

- mengubah quantum menjadi 2 dan 5.
- mengamati perubahan nilai rata-rata waiting time dan turnaround time.
- membuat tabel perbandingan efek quantum.

4. Eksperimen 4 – Dokumentasi

- Menyimpan semua hasil tabel dan screenshot ke:
`praktikum/week6-scheduling-rr-priority/screenshots/`
- Membuat tabel perbandingan terkait waiting time dan turnaround time untuk algoritma RR dan Priority.

5. Commit & Push

`git add .
git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
git push origin main`

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
`| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...`

`WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]`

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Eksperimen%201.png)
![Screenshot hasil](screenshots/Eksperimen%202.png)
![Screenshot hasil](screenshots/Eksperimen%204.png)

---

## Analisis
 Berdasarkan hasil eksekusi di atas,
  - Diperoleh bahwa kinerja Round Robin quantum 3 menjelaskan Setiap proses, bahkan P3 yang panjang, mendapat akses CPU secara berkala, sehingga tidak ada proses yang mengalami starvation.

- Algoritma Priority Scheduling (Non-Preemptive) menghasilkan kinerja rata-rata yang baik (WT rendah). Namun, mencapai efisiensi dengan mengorbankan keadilan, karena proses berprioritas rendah (P4) menanggung sebagian besar waiting time total.

---

## Kesimpulan
1. Round Robin (q=3) Menawarkan Keseimbangan Terbaik (Efisiensi dan Keadilan).
2. Priority Scheduling Mengorbankan Keadilan Demi Efisiensi Proses Tertentu.


---

## Quiz
1. Apa perbedaan utama antara Round Robin   dan Priority Scheduling?

    Priority Scheduling adalah algoritma paling efisien. Hal ini disebabkan karena proses P1 dan P2 yang tiba awal dan memiliki Burst Time pendek sekaligus prioritas tinggi dapat diselesaikan dengan cepat.

    Round Robin Setiap proses diberi jatah waktu kecil yang disebut Time Quantum. Proses berjalan selama quantum atau sampai selesai. Jika belum selesai dan quantum habis, proses di-preempt dan diletakkan di akhir antrian siap (ready queue) untuk giliran berikutnya.
2. Apa pengaruh besar/kecilnya time quantum  terhadap performa sistem?
    quantum harus dipilih secara seimbang.
    Jika quantum terlalu kecil, sistem membuang waktu untuk peralihan proses.
    Jika quantum terlalu besar, RR kehilangan keunggulannya dan menjadi FCFS, menyebabkan waktu tunggu yang tidak adil.
3. Algoritma Priority Scheduling dapat menyebabkan starvation 
    karena sifat dasarnya yang memprioritaskan proses berdasarkan nilai prioritas daripada waktu tunggu atau waktu kedatangan.

 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
menjalankan perintah 
`| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...`

`WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]`


- Bagaimana cara Anda mengatasinya?  
terus mencoba
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
