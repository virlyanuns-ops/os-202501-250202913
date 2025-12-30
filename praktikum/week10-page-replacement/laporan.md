
# Laporan Praktikum Minggu [10]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)



---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
 - Page Replacement
Manajemen memori virtual menggunakan paging membagi memori menjadi halaman tetap (pages) dan frame. Page fault terjadi saat halaman dibutuhkan tapi tidak ada di memori fisik, sehingga sistem operasi harus mengganti halaman lama dengan halaman baru
- Algoritma FIFO (First-In First-Out)
FIFO mengganti halaman yang paling lama berada di memori (pertama masuk, pertama keluar), seperti antrian. 
- Algoritma LRU (Least Recently Used)
LRU mengganti halaman yang paling lama digunakan berdasarkan waktu akses terakhir. 

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
``reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
print("FIFO Faults:", fifo_page_replacement(reference_string.copy(), 3))
print("LRU Faults:", lru_page_replacement(reference_string.copy(), 3))``


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/FIFO%20dan%20LRU(1).png)
![Screenshot hasil](screenshots/FIFO%20dan%20LRU(2).png)
![Screenshot hasil](screenshots/FIFO%20dan%20LRU(RUN).png)
---

## Analisis
-  tabel perbandingan

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | Mengganti halaman berdasarkan urutan masuk pertama, rentan terhadap Belady's anomaly di mana lebih banyak frame bisa menghasilkan lebih banyak fault |
   | LRU | 9 | Mengganti halaman yang paling lama tidak digunakan, biasanya lebih efisien daripada FIFO dengan fault lebih sedikit |


- mengapa jumlah *page fault* bisa berbeda
karena FIFO mengganti halaman berdasarkan urutan masuk (10 faults), sementara LRU ganti yang paling lama tak dipakai (9 faults).

- algoritma mana yang lebih efisien dan alasannya
LRU lebih efisien daripada FIFO,karena LRU mengganti halaman yang paling lama tidak digunakan dengan memanfaatkan locality of reference, sehingga mempertahankan halaman sering diakses dan mengurangi fault hingga 10%. FIFO hanya ikut urutan masuk, sering mengusir halaman masih relevan (Belady's anomaly).
---

## Kesimpulan
- FIFO suboptimal: Ikut urutan masuk, rentan usir halaman masih dibutuhkan (Belady's anomaly)
- LRU adaptif: Ganti halaman paling lama tak dipakai, manfaatkan locality of reference untuk hemat fault
- LRU unggul karena adaptif terhadap pola akses terkini, hemat 1 fault (10%) dibanding FIFO yang kaku ikut urutan masuk.


---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
- FIFO mengganti halaman berdasarkan urutan masuk pertama (first-in first-out)
- LRU mengganti halaman yang paling lama digunakan (least recently used)

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
- Belady's Anomaly terjadi ketika menambah frame memori justru meningkatkan page fault pada FIFO. Hal ini karena FIFO tidak mempertimbangkan pola akses, sehingga halaman yang masih dibutuhkan bisa terganti lebih awal.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
- LRU memantau waktu terakhir penggunaan halaman, sehingga halaman yang sering diakses baru-baru ini tetap di memori. Pendekatan ini mendekati algoritma Optimal dan menghasilkan page fault lebih sedikit dibanding FIFO yang hanya bergantung urutan masuk.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
