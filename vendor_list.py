import sqlite3
import customtkinter
import customtkinter as ctk
import tkinter
from tkinter import ttk
from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

class pelajar:
    database = 'menu_transaksi.db'

    def __init__(self, root):
        self.root = root
        self.root.title('Keranjang Belanja')
        self.root.config()

        # frame label toko
        self.top_frame = customtkinter.CTkFrame(master=self.root,width=985,height=80,fg_color='#222873')
        self.top_frame.pack(side='top',fill='x')

        self.label1 = ctk.CTkLabel(self.top_frame,text="Hello, Welcome To The Store!",font=('Ink Free',17,'bold'),text_color='white')
        self.label1.place(x=20,y=7)

        self.label1=customtkinter.CTkLabel(master=self.top_frame, text="Toko Furniture Bahagia",font=('Swis721 Blk BT',21),text_color='white')
        self.label1.place(x=20,y=35)

        self.tagline=customtkinter.CTkLabel(self.top_frame, text="Kemitraan Berkualitas, Inovasi Tanpa Batas",font=('Ink Free',16,'bold'),text_color='white')
        self.tagline.place(x=900,y=40)

        self.top_frame2 = customtkinter.CTkFrame(master=self.root,width=985,height=80,fg_color='white')
        self.top_frame2.pack(side='top',fill='x')

        self.label1 = ctk.CTkLabel(self.top_frame,text="Vendor List Company",font=('Swis721 Blk BT',21),text_color='#fff')
        self.label1.place(x=500,y=30)

        self.gambar = Image.open('supplier.png')
        self.width = 150
        self.height = 90
        self.resize = self.gambar.resize((self.width, self.height))
        self.gambar_jadi1 = ImageTk.PhotoImage(self.resize)

        self.label_gambar1 = ctk.CTkLabel(self.root,text='',image=self.gambar_jadi1)
        self.label_gambar1.place(x=40,y=81)

        self.gambar = Image.open('pt1.png')
        self.width = 600
        self.height = 90
        self.resize = self.gambar.resize((self.width, self.height))
        self.gambar_jadi1 = ImageTk.PhotoImage(self.resize)

        self.label_gambar1 = ctk.CTkLabel(self.root,text='',image=self.gambar_jadi1)
        self.label_gambar1.place(x=400,y=81)

        # Button back menu
        def go_menu():
            self.root.destroy()
            self.root.config(os.system('python menu_admin.py'))

        self.button_back_menu = customtkinter.CTkButton(self.top_frame2, width=150, text="Dashboard",font=('Segoe UI Semibold',15), corner_radius=6,command=go_menu)
        self.button_back_menu.place(x=1100,y=20)

        # frame untuk input data vendor
        self.frame_input = ctk.CTkFrame(self.root)
        self.frame_input.pack(side='left', padx=30)

        # widget input nama.
        self.nama = ctk.CTkLabel(self.frame_input, text='Nama : ')
        self.nama.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_nama = ctk.CTkEntry(self.frame_input)
        self.entry_nama.grid(row=0, column=1)

        # widget input alamat
        self.alamat = ctk.CTkLabel(self.frame_input, text='Alamat : ')
        self.alamat.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_alamat = ctk.CTkEntry(self.frame_input)
        self.entry_alamat.grid(row=1, column=1)

        # widget input produk
        self.produk = ctk.CTkLabel(self.frame_input, text='Produk : ')
        self.produk.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_produk = ctk.CTkEntry(self.frame_input)
        self.entry_produk.grid(row=2, column=1)

        # widget input jumlah
        self.jumlah = ctk.CTkLabel(self.frame_input, text='Jumlah : ')
        self.jumlah.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.entry_jumlah = ctk.CTkEntry(self.frame_input)
        self.entry_jumlah.grid(row=3, column=1)

        # widget input status
        self.status = ctk.CTkLabel(self.frame_input, text='Status : ')
        self.status.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.entry_status = ctk.CTkEntry(self.frame_input)
        self.entry_status.grid(row=4, column=1)

        # frame tombol-tombol
        self.frame_tombol = ctk.CTkFrame(self.root)
        self.frame_tombol.pack(side='left', padx=20)

        # tombol add
        self.add = ctk.CTkButton(self.frame_tombol, text='Add', command=self.add_data)
        self.add.pack(fill='y', padx=10, pady=10)

        # tombol edit
        self.edit = ctk.CTkButton(self.frame_tombol, text='Edit', command=self.edit_data)
        self.edit.pack(fill='y', padx=10, pady=10)

        # tombol delete
        self.delete = ctk.CTkButton(self.frame_tombol, text='Delete', command=self.delete_data)
        self.delete.pack(fill='y', padx=10, pady=10)

        # frame tabel data
        self.frame_tabel = ctk.CTkFrame(self.root)
        self.frame_tabel.pack(fill='both', padx=10, pady=5)

        self.tree = ttk.Treeview(
            self.frame_tabel, columns=('Nama', 'Alamat', 'Produk', 'Jumlah','Status'), show='headings'
        )
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Alamat", text="Alamat")
        self.tree.heading("Produk", text="Produk")
        self.tree.heading("Jumlah", text="Jumlah")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill='both', expand=True)

        self.buat_tabel()
        self.tampilkan_data()

        def close_window():
            response = messagebox.askyesno('Exit', 'Are you sure want to exit?')
            if response:
                self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', close_window)

    def run(self):
        self.root.mainloop()

    def run_perintah(self, perintah, parameter=()):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        result = cursor.execute(perintah, parameter)
        conn.commit()
        return result

    def buat_tabel(self):
        perintah = '''create table if not exists data_pembelian (
            nama text not null,
            alamat text not null,
            produk int not null,
            jumlah int not null,
            status text not null
        )'''
        self.run_perintah(perintah=perintah)

    def tampilkan_data(self):
        records = self.tree.get_children()
        for i in records:
            self.tree.delete(i)

        # Ambil data dari database dan tampilkan pada tabel
        perintah = 'select nama, alamat, produk, jumlah, status from data_pembelian'
        data = self.run_perintah(perintah).fetchall()
        for row in data:
            self.tree.insert('', 'end', values=row)

    def add_data(self):
        try:
            # ambil data dari input user
            nama = self.entry_nama.get()
            alamat = self.entry_alamat.get()
            produk = self.entry_produk.get()
            jumlah = self.entry_jumlah.get()
            status = self.entry_status.get()

            # cek apakah ada input yg kosong
            if nama == '' or alamat == '' or produk == '' or jumlah == '' or status == '' :
                messagebox.showerror('Error', 'Isi semua data yang kosong!')
                return

            # insert data ke database
            perintah = 'insert into data_pembelian (nama,alamat,produk,jumlah,status) values (?,?,?,?,?)'
            parameter = (nama, alamat, produk, jumlah,status)
            self.run_perintah(perintah, parameter)

        except ValueError:
            messagebox.showerror('Error', 'nama harus berupa angka!')
            return

        except sqlite3.IntegrityError:
            messagebox.showerror('Error', 'nama sudah ada dalam database!')
            return

        self.entry_nama.delete(0, 'end')
        self.entry_alamat.delete(0, 'end')
        self.entry_produk.delete(0, 'end')
        self.entry_jumlah.delete(0, 'end')
        self.entry_status.delete(0, 'end')

        # tampilkan data terbaru pada tabel
        self.tampilkan_data()

    def edit_data(self):
        try:
            nama = self.entry_nama.get()
            alamat = self.entry_alamat.get()
            produk = self.entry_produk.get()
            jumlah = self.entry_jumlah.get()
            status = self.entry_status.get()

            # ambil data yg akan di update
            selected_item = self.tree.focus()
            values = self.tree.item(selected_item, 'values')
            id = values[0]

            # cek apakah ada input yg kosong
            if nama == '' or alamat == '' or produk == '' or jumlah == '' or status == '':
                messagebox.showerror('Error', 'Isi semua data yang kosong!')
                return

            # update data di database
            perintah = 'update data_pembelian set nama=?,alamat=?,produk=?,jumlah=?,status=? where nama=?'
            parameter = (nama, alamat, produk, jumlah, status, id)
            self.run_perintah(perintah, parameter)

        except ValueError:
            messagebox.showerror('Error', 'nama harus berupa angka')
            return

        except IndexError:
            messagebox.showwarning('Warning', 'Pilih data yang akan diedit!')
            return

        self.tampilkan_data()
        self.rapihkan_entries()

    def delete_data(self):
        # ambil data yg akan di update
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, 'values')
        id = values[0]

        # hapus data yang dipilih
        perintah = 'delete from data_pembelian where nama=?'
        parameter = (id,)
        self.run_perintah(perintah, parameter)

        self.tampilkan_data()

    def rapihkan_entries(self):
        self.entry_nama.delete(0, 'end')
        self.entry_nama.delete(0, 'end')
        self.entry_produk.delete(0, 'end')
        self.entry_jumlah.delete(0, 'end')
        self.entry_status.delete(0, 'end')
        self.tampilkan_data()

    def delete_data(self):
        if not self.tree.focus():
            messagebox.showwarning('Warning', 'Pilih data untuk dihapus!')
            return
        result = messagebox.askquestion('Delete Confirmation', 'Apakah anda yakin ingin menghapus data ini?')
        if result == 'yes':
            selected_item = self.tree.focus()
            nama = self.tree.item(selected_item)["values"][0]
            perintah = f"DELETE FROM data_pembelian WHERE nama = '{nama}'"
            self.run_perintah(perintah=perintah)
            self.tampilkan_data()


if __name__ == "__main__":
    app = pelajar(root=ctk.CTk())
    app.root.mainloop()