
# Laporan Praktikum Minggu [12]
Topik:Virtualisasi Menggunakan Virtual Machine
---

## Identitas
|nama kelompok|nim| kelas|
|------------------|---------------------------|------------------|
|Virli A'inun Subroto| 250202913|1IKRB|
|Syafi'iyah Rahmadani| 250202913|1IKRB|

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
- Virtualisasi dan Hypervisor: Teknik menjalankan OS Guest di atas OS Host menggunakan Hypervisor (seperti VirtualBox) yang berfungsi mengelola dan mengalokasikan sumber daya perangkat keras fisik ke lingkungan virtual.

- Abstraksi Sumber Daya: Setiap Virtual Machine (VM) memiliki alokasi mandiri untuk CPU, RAM, dan storage, sehingga memungkinkan beberapa OS berjalan secara bersamaan tanpa saling mengganggu kinerja satu sama lain.

- Isolasi dan Keamanan: Virtualisasi menciptakan lingkungan terisolasi (sandboxing) yang melindungi OS Host dari kegagalan atau ancaman keamanan yang terjadi di dalam OS Guest.
---

## Langkah Praktikum
1.  **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
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
![Screenshot hasil](screenshots/instalasi_vm.png.jpeg).

![Screenshot hasil](screenshots/konfigurasi_resource.png.jpeg)

![Screenshot hasil](screenshots/os_guest_running.png.jpeg)

![Screenshot hasil](screenshots/konfigurasi_resource.png%20(2).jpeg)

![Screenshot hasil](screenshots )
---

## Analisis
- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
VM bekerja dengan cara memisahkan sumber daya perangkat keras fisik dari sistem operasi guest. Hypervisor bertindak sebagai perantara yang memastikan bahwa OS guest hanya dapat mengakses sumber daya (CPU, RAM, storage) yang telah dialokasikan secara spesifik untuknya. OS guest tidak memiliki akses langsung ke memori atau proses yang sedang berjalan di OS host, sehingga menciptakan batasan yang tegas antara keduanya.

- Kaitkan dengan konsep *sandboxing* dan *hardening* OS. 
  - sandboxing Jika OS guest terkena malware atau mengalami kerusakan sistem, dampak tersebut akan terkurung di dalam VM saja. Karena adanya batasan sandboxing ini, kode berbahaya dari guest tidak dapat "melompat" untuk menginfeksi atau merusak OS host.

   - hardening  
  Dengan menjalankan aplikasi yang berisiko di dalam VM, kita memperkecil luas permukaan serangan (attack surface) pada sistem utama (host). Hardening dilakukan dengan membatasi resource yang tersedia bagi VM, sehingga jika terjadi serangan, penyerang hanya memiliki akses terbatas pada sumber daya yang telah dikonfigurasi sebelumnya.

---

## Kesimpulan
- Efisiensi Pengelolaan Sumber Daya: Virtualisasi memungkinkan satu perangkat keras fisik (Host OS) menjalankan satu atau lebih sistem operasi tambahan (Guest OS) secara bersamaan melalui manajemen sumber daya (CPU, RAM, dan storage) yang fleksibel oleh hypervisor.

- Keamanan dan Isolasi Sistem: Penggunaan Virtual Machine menciptakan lingkungan yang terisolasi (sandboxing), sehingga aktivitas atau kegagalan yang terjadi pada OS Guest tidak akan memengaruhi stabilitas dan keamanan OS Host.

- Pemahaman Arsitektur Virtualisasi: Praktikum ini berhasil membuktikan peran penting hypervisor dalam menjembatani komunikasi antara perangkat keras fisik dengan berbagai sistem operasi guest yang berbeda.
---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?

| Fitur | Host OS (Sistem Operasi Inang) | Guest OS (Sistem Operasi Tamu) |
| :--- | :--- | :--- |
| **Definisi** | OS yang terinstal langsung pada perangkat keras fisik (*bare-metal*). | OS yang berjalan di dalam mesin virtual (VM). |
| **Akses Hardware** | Memiliki akses langsung dan penuh ke CPU, RAM, dan Disk fisik. | Menggunakan sumber daya virtual yang dijembatani oleh Hypervisor. |
| **Instalasi** | Diinstal pada partisi hard disk fisik. | Diinstal pada file disk virtual (seperti format `.vmdk` atau `.vdi`). |
| **Kemandirian** | Dapat berjalan tanpa perlu software virtualisasi. | Membutuhkan Hypervisor (seperti VirtualBox atau VMware) untuk berjalan. |
| **Contoh** | Windows 11 di laptop Anda. | Linux Ubuntu yang berjalan di dalam VirtualBox. |

2. Apa peran hypervisor dalam virtualisasi?
   1. **Abstraksi (Pemisahan)**
   Menyediakan lapisan antara perangkat keras fisik dan sistem operasi. Hypervisor membuat "perangkat keras palsu" (CPU, RAM, Disk virtual) agar bisa digunakan oleh Guest OS.

   2. **Isolasi (Keamanan)**
   Memastikan setiap Mesin Virtual (VM) berjalan secara mandiri. Jika satu VM mengalami error atau terkena virus, hal tersebut tidak akan menular ke VM lain atau ke sistem fisik.

   3. **Alokasi Sumber Daya**
   Bertindak sebagai manajer yang membagi kapasitas hardware. Contoh: Jika Anda punya RAM 16GB, Hypervisor bisa membagi 4GB untuk Linux, 4GB untuk Windows, dan sisanya untuk Host OS.


3. Mengapa virtualisasi meningkatkan keamanan sistem?  
karena virtualisasi menciptakan jarak antara hardware dan aktivitas user, yang secara signifikan mempersempit celah serangan bagi pihak luar.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
