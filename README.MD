Manajemen Daftar Tugas (To-Do List Manager)

Program Manajemen Daftar Tugas ini adalah aplikasi berbasis command-line yang memungkinkan pengguna untuk mengorganisir, melacak, dan mengelola berbagai tugas atau aktivitas yang perlu diselesaikan. Program ini dibangun menggunakan Python dan memanfaatkan modul built-in seperti random untuk generate ID unik dan datetime untuk manajemen deadline.

A. Fitur Utama

Manajemen Tugas Komprehensif Program menyediakan sistem penyimpanan tugas dengan: a. ID Unik (4-digit angka acak antara 1000-9999) b. Nama Tugas (deskripsi tugas) c. Deadline (disimpan sebagai objek date) d. Status Penyelesaian (boolean True/False)
Sistem Interaktif Berbasis Menu Antarmuka pengguna yang sederhana dengan 6 opsi menu utama: a. Penambahan Tugas Baru - Validasi format tanggal otomatis - Generate ID otomatis b. Visualisasi Daftar Tugas - Menampilkan dalam format tabel sederhana - Penyortiran berdasarkan status dan deadline c. Update Status Tugas - Penanda penyelesaian tugas d. Penghapusan Tugas - Sistem konfirmasi implisit e. Sistem Rekomendasi - Algoritma acak untuk tugas yang belum selesai f. Keluar Program - Terminasi aplikasi yang terkontrol
B. Persyaratan Sistem

Lingkungan Eksekusi a. Python 3.6 atau versi lebih baru b. Terminal/Command Prompt yang mendukung input/output standar c. Sistem Operasi: Cross-platform (Windows, macOS, Linux)
Dependensi Program ini menggunakan modul Python standar tanpa dependensi eksternal: a. random - Untuk generasi ID tugas b. datetime - Untuk parsing dan manajemen tanggal
C. Batasan Program

Penyimpanan Volatile: a. Data hanya disimpan dalam memori selama program berjalan b. Tidak ada persistensi ke file/database
Validasi Input: a. Format tanggal harus DD-MM-YYYY b. Input ID harus integer
Fitur Tambahan: a. Tidak ada notifikasi deadline b. Tidak ada sistem prioritas tugas
