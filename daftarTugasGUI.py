import random
import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

class AplikasiTodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Daftar Tugas")
        self.root.geometry("600x480")
        
        # Struktur data untuk menyimpan tugas
        self.daftar_tugas = {}
        
        # Frame utama
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        # Label judul
        self.label_judul = tk.Label(self.frame, text="Manajemen Daftar Tugas\n", font=("Times New Roman", 24))
        self.label_judul.pack()
        
        # Tombol-tombol menu
        self.btn_tambah = tk.Button(self.frame, text="Tambah Tugas", command=self.tambah_tugas, width=20)
        self.btn_tambah.pack(pady=5)
        
        self.btn_lihat = tk.Button(self.frame, text="Lihat Daftar Tugas", command=self.lihat_tugas, width=20)
        self.btn_lihat.pack(pady=5)
        
        self.btn_selesai = tk.Button(self.frame, text="Tandai Selesai", command=self.tandai_selesai, width=20)
        self.btn_selesai.pack(pady=5)
        
        self.btn_hapus = tk.Button(self.frame, text="Hapus Tugas", command=self.hapus_tugas, width=20)
        self.btn_hapus.pack(pady=5)
        
        self.btn_rekomendasi = tk.Button(self.frame, text="Rekomendasi Tugas", command=self.rekomendasi_tugas, width=20)
        self.btn_rekomendasi.pack(pady=5)
        
        self.btn_keluar = tk.Button(self.frame, text="Keluar", command=self.keluar, width=20)
        self.btn_keluar.pack(pady=5)
        
        # Text area untuk menampilkan daftar tugas
        self.text_area = tk.Text(self.root, height=10, width=70)
        self.text_area.pack(pady=10)
    
    def tambah_tugas(self):
        nama_tugas = simpledialog.askstring("Tambah Tugas", "Masukkan nama tugas:")
        if not nama_tugas:
            return
            
        deadline = simpledialog.askstring("Tambah Tugas", "Masukkan deadline (DD-MM-YYYY):")
        if not deadline:
            return
            
        try:
            tanggal_deadline = datetime.datetime.strptime(deadline, "%d-%m-%Y").date()
            id_tugas = random.randint(1000, 9999)
            
            self.daftar_tugas[id_tugas] = {
                'nama': nama_tugas,
                'deadline': tanggal_deadline,
                'selesai': False
            }
            messagebox.showinfo("Sukses", f"Tugas '{nama_tugas}' berhasil ditambahkan dengan ID {id_tugas}!")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal tidak valid! Gunakan DD-MM-YYYY")
    
    def lihat_tugas(self):
        self.text_area.delete(1.0, tk.END)
        
        if not self.daftar_tugas:
            self.text_area.insert(tk.END, "Daftar tugas kosong!")
            return
            
        self.text_area.insert(tk.END, "DAFTAR TUGAS:\n")
        for id_tugas, detail in self.daftar_tugas.items():
            status = "✓" if detail['selesai'] else "✗"
            self.text_area.insert(tk.END, 
                f"ID: {id_tugas} | Tugas: {detail['nama']}\n"
                f"Deadline: {detail['deadline']} | Status: {status}\n")
    
    def tandai_selesai(self):
        id_tugas = simpledialog.askinteger("Tandai Selesai", "Masukkan ID tugas yang selesai:")
        if id_tugas is None:
            return
            
        if id_tugas in self.daftar_tugas:
            self.daftar_tugas[id_tugas]['selesai'] = True
            messagebox.showinfo("Sukses", f"Tugas '{self.daftar_tugas[id_tugas]['nama']}' ditandai selesai!")
            self.lihat_tugas()
        else:
            messagebox.showerror("Error", "ID tugas tidak ditemukan!")
    
    def hapus_tugas(self):
        id_tugas = simpledialog.askinteger("Hapus Tugas", "Masukkan ID tugas yang akan dihapus:")
        if id_tugas is None:
            return
            
        if id_tugas in self.daftar_tugas:
            del self.daftar_tugas[id_tugas]
            messagebox.showinfo("Sukses", "Tugas berhasil dihapus!")
            self.lihat_tugas()
        else:
            messagebox.showerror("Error", "ID tugas tidak ditemukan!")
    
    def rekomendasi_tugas(self):
        if not self.daftar_tugas:
            messagebox.showinfo("Info", "Daftar tugas kosong!")
            return
            
        tugas_belum_selesai = [t for t in self.daftar_tugas.values() if not t['selesai']]
        if tugas_belum_selesai:
            rekomendasi = random.choice(tugas_belum_selesai)
            messagebox.showinfo("Rekomendasi", 
                f"Rekomendasi tugas untuk dikerjakan:\n\n"
                f"Nama: {rekomendasi['nama']}\n"
                f"Deadline: {rekomendasi['deadline']}")
        else:
            messagebox.showinfo("Info", "Semua tugas sudah selesai!")
    
    def keluar(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTodoList(root)
    root.mainloop()