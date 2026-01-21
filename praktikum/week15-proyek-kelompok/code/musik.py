import os
import time
import sys

# =================================================================
# MINI SIMULASI - TEMA: PEMUTAR MUSIK (V4)
# Fitur: Re-playable Queue & Sequential Scheduling (FCFS)
# Deskripsi: Simulasi antrean musik yang bisa diulang setelah selesai.
# =================================================================
class MusicSimulator:
    def __init__(self):
        # Dataset Lagu (Proses dalam Sistem Operasi)
        self.playlist = [
            {"id": 101, "judul": "Sial - Mahalini", "durasi": 4},
            {"id": 102, "judul": "Blue - Yung Kai", "durasi": 3},
            {"id": 103, "judul": "Gajah - Tulus", "durasi": 5},
            {"id": 104, "judul": "Untitled - Rex Orange", "durasi": 3},
            {"id": 105, "judul": "Satu-Satu - Idgitaf", "durasi": 4},
            {"id": 106, "judul": "Double Take - Dhruv", "durasi": 3},
            {"id": 107, "judul": "Tak Ingin Usai - Keisya", "durasi": 5},
        ]
        # Kecepatan loading bar (dalam detik)
        self.kecepatan_simulasi = 2 

    def clear(self):
        """Fungsi untuk membersihkan layar terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def gambar_tabel(self, daftar_selesai, lagu_aktif=None):
        """Menampilkan tabel monitoring antrean secara real-time"""
        self.clear()
        print("="*75)
        print(f"{'ANTREAN PEMUTARAN MUSIK (SIMULASI OS)':^75}")
        print("="*75)
        # Header kolom menggunakan istilah non-teknis agar mudah dipahami
        print(f"{'No':<4} | {'Judul Lagu':<25} | {'Durasi':<10} | {'Tunggu':<10} | {'Total'}")
        print("-" * 75)

        # 1. Menampilkan baris lagu yang sudah selesai diproses
        for task in daftar_selesai:
            print(f"{task['no']:<4} | {task['judul']:<25} | {task['durasi']:>2} Menit  | "
                  f"{task['wt']:>2} Menit  | {task['tat']:>2} Menit  ✅")

        # 2. Menampilkan baris lagu yang saat ini sedang aktif (CPU Execution)
        if lagu_aktif:
            print(f"{lagu_aktif['no']:<4} | {lagu_aktif['judul']:<25} | {lagu_aktif['durasi']:>2} Menit  | "
                  f"{lagu_aktif['wt']:>2} Menit  | {'...':<7} ⏳ Memutar")
            
            # Animasi Progress Bar di dalam tabel
            self.animasi_putar(lagu_aktif['judul'])
        
        print("-" * 75)

    def animasi_putar(self, judul):
        """Visualisasi progress pemutaran (Simulasi Gantt Chart)"""
        lebar = 35
        for i in range(lebar + 1):
            persen = int((i / lebar) * 100)
            bar = '█' * i + '-' * (lebar - i)
            sys.stdout.write(f'\r   Progress: [{bar}] {persen}% ')
            sys.stdout.flush()
            time.sleep(self.kecepatan_simulasi / lebar)
        print()

    def jalankan_simulasi(self):
        """Logika inti penjadwalan antrean musik"""
        while True: # Loop Utama agar bisa memutar lagi
            self.clear()
            print("🎵 SELAMAT DATANG DI SIMULATOR MUSIK 🎵")
            print("="*40)
            print("Silakan pilih lagu awal untuk memulai antrean:")
            
            # Tampilkan daftar pilihan dataset
            for i, l in enumerate(self.playlist, 1):
                print(f"{i}. {l['judul']} ({l['durasi']} Menit)")
            
            try:
                pilihan = int(input("\nMulai dari nomor (1-7): ")) - 1
                if pilihan < 0 or pilihan >= len(self.playlist):
                    print("\n⚠️ Nomor tidak valid, coba lagi...")
                    time.sleep(1.5)
                    continue
            except ValueError:
                print("\n⚠️ Harap masukkan angka saja!")
                time.sleep(1.5)
                continue

            # Inisialisasi variabel statistik OS
            antrean = self.playlist[pilihan:]
            selesai = []
            waktu_tunggu_skrg = 0
            total_waiting_time = 0

            # Proses pemutaran sequential (FCFS)
            for i, lagu in enumerate(antrean, 1):
                data_lagu = {
                    "no": i,
                    "judul": lagu['judul'],
                    "durasi": lagu['durasi'],
                    "wt": waktu_tunggu_skrg
                }

                # Tampilkan status 'Sedang Memutar'
                self.gambar_tabel(selesai, data_lagu)

                # Hitung Turnaround Time (TAT)
                tat = waktu_tunggu_skrg + lagu['durasi']
                data_lagu['tat'] = tat
                
                # Masukkan ke history selesai
                selesai.append(data_lagu)
                total_waiting_time += waktu_tunggu_skrg
                waktu_tunggu_skrg += lagu['durasi']
                
                # Context switching delay (Jeda antar proses)
                if lagu != antrean[-1]:
                    time.sleep(1)

            # Tampilkan hasil akhir semua lagu
            self.gambar_tabel(selesai)
            avg_wt = total_waiting_time / len(selesai)
            
            print(f"\n[RINGKASAN SISTEM]")
            print(f"Rata-rata Waktu Tunggu: {avg_wt:.2f} Menit")
            print("Semua antrean telah selesai diputar.")
            
            # --- FITUR PUTAR LAGI ---
            ulang = input("\nApakah ingin memutar antrean lagi? (y/n): ").lower()
            if ulang != 'y':
                print("\nMematikan simulator... Sampai jumpa!")
                time.sleep(1)
                break

if __name__ == "__main__":  
    app = MusicSimulator()
    try:
        app.jalankan_simulasi()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program dihentikan paksa.")