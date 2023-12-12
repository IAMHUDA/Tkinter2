#menambahkan library
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Pegawai")
        self.root.geometry("490x670")
        self.root.resizable(True, True)

        self.image_path = "umybg.jpg"
        self.bg_image = Image.open(self.image_path)
        self.bg_image = ImageTk.PhotoImage(self.bg_image) 
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)
        bg_label.pack()

        self.image_path = "logo.png"
        self.logo_image = Image.open(self.image_path)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)

        # Create a container (Frame) for entry widgets
        self.entry_container = tk.Frame(root, bg="#F5F5F5")
        self.entry_container.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Create logo label
        logo_label = tk.Label(self.entry_container, image=self.logo_image, bg="#F5F5F5")
        logo_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.EW)

        entry_font = ("Helvetica", 10)
        entry_width = 50

    
        # Create entry widgets inside the container
        login_label = tk.Label(self.entry_container, text="Login", font=("Helvetica", 14), bg="#F5F5F5")
        login_label.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.EW)

        # Create a line under the Login label using Canvas
        line_canvas = tk.Canvas(self.entry_container, bg="#F5F5F5", height=2, highlightthickness=0)
        line_canvas.create_line(0, 2, 400, 2, width=2, fill="#808080")  # Adjust the length and color as needed
        line_canvas.grid(row=2, column=0, columnspan=2, pady=(5, 10), sticky=tk.EW)

        self.nama_pegawai = tk.Label(self.entry_container, text="nama Pegawai", font=entry_font, bg="#FFFFFF")
        self.nama_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,
                                       highlightthickness=0, highlightbackground="white", bg="azure")

        self.alamat = tk.Label(self.entry_container, text="Alamat", font=entry_font, bg="#FFFFFF")
        self.alamat_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,
                                       highlightbackground="white", highlightthickness=0, bg="azure")

        self.posisi_label = tk.Label(self.entry_container, text="Posisi", font=entry_font, bg="#FFFFFF")
        self.posisi_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,
                                       highlightbackground="white", highlightthickness=0, bg="azure")

        self.TahunMasuk_label = tk.Label(self.entry_container, text="Tahun Masuk", font=entry_font, bg="#FFFFFF")
        self.TahunMasuk_entry = tk.Entry(self.entry_container, font=entry_font, width=entry_width,
                                       highlightbackground="white", highlightthickness=0, bg="azure")
        # Place entry widgets inside the container
        label_y = 3
        entry_y = 4
        for label, entry in zip([self.nama_pegawai, self.alamat,self.posisi_label,self.TahunMasuk_label],
                                [self.nama_entry, self.alamat_entry,self.posisi_entry,self.TahunMasuk_entry],):
            label.grid(row=label_y, column=0, pady=5, sticky=tk.W)
            entry.grid(row=entry_y, column=0, pady=5, sticky=tk.E)
            label_y += 2
            entry_y += 2

        # Create Submit button with shadow inside the container
        button_font = ("Helvetica", 10)
        self.submit_button = tk.Button(self.entry_container, text="submit", command=self.Submit_login,
                                       font=button_font, bg="#00FFFF", fg="black", bd=0, padx=20, pady=3,
                                       relief=tk.GROOVE, cursor="hand2",highlightthickness=7)
        self.submit_button.grid(row=entry_y, column=0, columnspan=2, pady=10, sticky=tk.EW)

#membuat fungsi untuk meginput data
    def Submit_login(self):
        nama_pegawai = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        posisi = self.posisi_entry.get()
        TahunMasuk = self.TahunMasuk_entry.get()




#membuat koneksi ke database SQLite dengan nama InputNilaiDB
        conn =sqlite3.connect('InputPegawaiDB.db')
        cursor = conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS Input_Pegawai(
                    nama_pegawai TEXT,
                    alamat TEXT,
                    posisi TEXT,
                    TahunMasuk INTEGER)''')

#membuat insert into untuk menambahkan data yang ingin kita input ke databse
        cursor.execute(''' INSERT INTO Input_Pegawai(nama_pegawai, alamat, posisi, TahunMasuk) VALUES (?, ?, ?, ?)''',
                        (nama_pegawai, alamat, posisi, TahunMasuk))
    
#digunakan untuk menyimpan perubahan yang telah dilakukan ke database
        conn.commit()
#digunakan untuk menutup koneksi ke database SQLite
        conn.close() 

#membuat popup yang akan tampil jika data disubmit atau disimpan
        messagebox.showinfo("Successful", f"Data berhasil disimpan sebagai:{nama_pegawai}")


#digunakan untuk memulai loop utama
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()