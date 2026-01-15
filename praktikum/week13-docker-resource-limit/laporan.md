
# Laporan Praktikum Minggu [13]
Topik:  Docker – Resource Limit (CPU & Memori)
---

## Identitas
- **Nama**  :virli a'inun subroto   
- **NIM**   :250202913    
- **Kelas** :1ikrb

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan CPU dan memori.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
1. Containerization & Isolasi
2. Mekanisme Cgroups (Control Groups)
3. Resource Limit (CPU & Memori)
4. Monitoring Resource

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
---

## Kode / Perintah

```
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
# Membangun image dari folder code
docker build -t week13-resource-limit .
# Menjalankan dengan pembatasan RAM 200MB dan CPU 0.5
docker run --rm --cpus="0.5" --memory="200m" week13-resource-limit
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_limit.png(1).png)
![Screenshot hasil](screenshots/hasil_limit.png(2).png)
---

## Analisis
-Eksekusi Tanpa Limit (Normal):
Saat menjalankan ``docker run --rm week13-resource-limit``, program berjalan hingga tuntas.
Alokasi RAM berhasil mencapai angka target 500 MB dan memunculkan pesan "SEMUA PROSES SELESAI".

- Eksekusi Dengan Limit Memori:
saat menjalankan perintah ```docker run --rm --memory="250m" week13-resource-limit``` program akan terhenti seketika saat mencoba melakukan alokasi memori ke tahap berikutnya (300 MB) karena telah melampaui batas 250 MB yang ditentukan. Hal ini memicu kernel untuk mengirimkan sinyal penghentian paksa guna melindungi stabilitas sistem host.

---

## Kesimpulan

1. Efektivitas Mekanisme Cgroups: Fitur resource limit pada Docker terbukti efektif dalam membatasi penggunaan sumber daya fisik.kontainer tanpa limit dapat mengalokasi RAM hingga 500 MB, sementara kontainer dengan limit --memory="250m" dihentikan paksa oleh sistem saat melampaui ambang batas tersebut.

2. pembatasan sumber daya sangat krusial dalam lingkungan multi-kontainer untuk menjaga stabilitas sistem host, mencegah kebocoran memori dari satu aplikasi memengaruhi aplikasi lainnya (Noisy Neighbor Effect), dan menghindari kegagalan sistem total akibat resource exhaustion.
---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
   - Mencegah Resource Exhaustion agar satu container tidak menghabiskan seluruh sumber daya host yang dapat menyebabkan sistem hang atau mati.

   - Menghindari Noisy Neighbor Effect Memastikan satu container yang sedang bekerja berat tidak mengganggu performa container lain yang berjalan di host yang sama.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

| Fitur | Virtual Machine (VM) | Container |
| :--- | :--- | :--- |
| **Mekanisme** | Menggunakan Hypervisor untuk membagi hardware fisik. | Menggunakan fitur Kernel Linux (Cgroups & Namespaces). |
| **Sifat Isolasi** | Isolasi total hingga level Hardware (Kernel sendiri). | Isolasi level OS (Berbagi kernel dengan host). |
| **Alokasi Resource** | Resource biasanya sudah dipesan (reserved) sejak awal. | Resource bersifat fleksibel namun dibatasi oleh plafon limit.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
   - OOM Killed
   - Performa Melambat (Thrashing)
   - Error Alokasi


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
