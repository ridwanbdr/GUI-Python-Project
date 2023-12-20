import sqlite3
import tkinter
import tkinter as ttk
from tkinter import ttk
from tkinter import *
import customtkinter
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk,Image
from PIL import *
import tkinter.messagebox
import datetime
import os


# Menghapus data total harga yang sebelumnya
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''drop table if exists harga_total''')
result = cur.fetchall()
conn.commit()
conn.close()

# Mengambil data seluruh harga produk yang terpilih
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT harga_total FROM keranjang''')
result = cur.fetchall()
conn.commit()
conn.close()

result1 = [item[0] for item in result]
total_harga = sum(result1)
total = int(total_harga)

# Memasukkan data yang terpilih kedalam database total harga
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''create table if not exists harga_total (
    total_harga int
)''')
cur.execute('insert into harga_total (total_harga) values (?)',(total,))
conn.commit()
conn.close()

# Mengambil data produk yang terpilih
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT name FROM keranjang''')
result_name = cur.fetchall()
# Membuat database untuk produk terpilih
cur.execute('''CREATE TABLE IF NOT EXISTS all_product (
    produk_terpilih TEXT
)''')
# Memasukkan data nama produk terpilih ke database
for name in result_name:
    cur.execute('INSERT INTO all_product (produk_terpilih) VALUES (?)', (name[0],))
conn.commit()
conn.close()

# Mengambil data harga per produk yang terpilih
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT harga FROM keranjang''')
result_harga = cur.fetchall()
# Membuat database untuk produk terpilih
cur.execute('''CREATE TABLE IF NOT EXISTS harga_satuan (
    harga_satuan TEXT
)''')
# Memasukkan data produk terpilih ke database
for harga in result_harga:
    cur.execute('INSERT INTO harga_satuan (harga_satuan) VALUES (?)', (harga[0],))

# Mengambil jumlah produk yang terpilih
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT jumlah FROM keranjang''')
result_jumlah = cur.fetchall()
# Membuat database untuk produk terpilih
cur.execute('''CREATE TABLE IF NOT EXISTS jumlah_dipilih (
    jumlah_dipilih int
)''')
# Memasukkan data produk terpilih ke database
for jumlah in result_jumlah:
    cur.execute('INSERT INTO jumlah_dipilih (jumlah_dipilih) VALUES (?)', (jumlah[0],))
conn.commit()
conn.close()

produk_jumlah = [item[0] for item in result_jumlah]
total_jumlah_produk = sum(produk_jumlah)
jumlah_produk_dipilih = int(total_jumlah_produk)


# Mengambil seluruh data produk yang terpilih
# Mengambil data seluruh harga produk yang terpilih
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM keranjang''')
result_seluruh = cur.fetchall()
conn.commit()
conn.close()

print(result_seluruh)


# Membuat tabel data pelanggan
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''create table if not exists data_pelanggan (
    nama text not null,
    alamat text not null,
    tanggal int not null,
    bulan text not null, 
    produk_dibeli int,
    total_belanja int
)''')
conn.commit()
conn.close()

def keranjang():

    def go_menu():
        keranjang.destroy()
        keranjang.config(os.system('python main_menu.py'))

    def go_ruangtamu():
        menu_page.destroy()
        menu_page.config(os.system('python ruang_tamu.py'))

    def go_dapur_kantor():
        menu_page.destroy()
        menu_page.config(os.system('python dapur_kantor.py'))

    def go_cetakInv():
        nama = nama_cust.get()
        alamat = alamat_cust.get()
        tanggal = tgl_beli.get()   
        bulan = bln_belii.get()
        kotaasal = kota.get()
        no_kontak = kontak.get()

        if nama == '' or alamat == '' or tanggal == '' or bulan == '' :
            tkinter.messagebox.showwarning('Information','Isi data customer terlebih dahulu!')
            return

        cetak_inv = customtkinter.CTk()  # membuat cutstom tkinter window
        cetak_inv.geometry("320x470")
        cetak_inv.title('Invoice')

        # frame
        frame = customtkinter.CTkFrame(cetak_inv,width=280,height=430,fg_color='#ffffb3')
        frame.place(x=20,y=20)

        label = customtkinter.CTkLabel(frame,text='Toko Furniture Bahagia',font=('Swis721 Blk BT',13),text_color='#222873')
        label.place(x=60,y=5)

        label1 = customtkinter.CTkLabel(frame,text='Jl. Achmad Dahlan no 23, Bandung',font=('Cascadia Code SemiLight',10),text_color='black')
        label1.place(x=50,y=25)

        label_garis0 = customtkinter.CTkLabel(frame,text='--------------------------------------',font=('Cascadia Code SemiLight',12),text_color='black')
        label_garis0.place(x=5,y=45)
        
        label2 = customtkinter.CTkLabel(frame,text='Invoice',font=('Cascadia Code SemiLight',29,'bold'),text_color='black')
        label2.place(x=20,y=85)

        label3 = customtkinter.CTkLabel(frame,text='#Invoice',font=('Cascadia Code SemiLight',8),text_color='black')
        label3.place(x=180,y=80)

        tgl_skrg = datetime.datetime.now().strftime("%Y-%m-%d")
        tanggal = f'Date : {tgl_skrg}'
        label4 = customtkinter.CTkLabel(frame,text=tanggal,font=('Cascadia Code SemiLight',8),text_color='black')
        label4.place(x=180,y=100)

        label_garis = customtkinter.CTkLabel(frame,text='--------------------------------------',font=('Cascadia Code SemiLight',12),text_color='black')
        label_garis.place(x=5,y=120)

        label5 = customtkinter.CTkLabel(frame,text=f'Total Item  : {jumlah_produk_dipilih}',font=('Cascadia Mono',12),text_color='black')
        label5.place(x=50,y=165)
        
        label6 = customtkinter.CTkLabel(frame,text=f'Harga Total : Rp. {total}',font=('Cascadia Mono',12),text_color='black')
        label6.place(x=50,y=195)

        label_garis2 = customtkinter.CTkLabel(frame,text='--------------------------------------',font=('Cascadia Code SemiLight',12),text_color='black')
        label_garis2.place(x=5,y=240)

        label7 = customtkinter.CTkLabel(frame,text='SEND PAYMENT TO :',font=('Lucida Console',10,'bold'),text_color='black')
        label7.place(x=20,y=270)

        nama = nama_cust.get()
        alamat = alamat_cust.get()
        tanggal = tgl_beli.get()   
        bulan = bln_belii.get()
        kotaasal = kota.get()
        no_kontak = kontak.get()

        label_nama = customtkinter.CTkLabel(frame,text=F'NAME       : {nama}',font=('Lucida Console',10),text_color='black')
        label_nama.place(x=20,y=290)
        
        label_alamat = customtkinter.CTkLabel(frame,text=f'ADDRESS    : {alamat}, {kotaasal}',font=('Lucida Console',10),text_color='black')
        label_alamat.place(x=20,y=310)

        label_waktu = customtkinter.CTkLabel(frame,text=F'PAYMENT ON : {tanggal} - {bulan} - 2023',font=('Lucida Console',10),text_color='black')
        label_waktu.place(x=20,y=330)

        label_kontak = customtkinter.CTkLabel(frame,text=F'CONTACT    : {no_kontak}',font=('Lucida Console',10),text_color='black')
        label_kontak.place(x=20,y=350)

        label_ucapan = customtkinter.CTkLabel(frame,text='''Terimakasih telah berbelanja di toko kami!
--- Selamat Datang Kembali ---''',font=('Cascadia Code SemiLight',8),text_color='black')
        label_ucapan.place(x=35,y=390)
        
        cetak_inv.mainloop()

    def go_bayar():

        nama = nama_cust.get()
        alamat = alamat_cust.get()
        tanggal = tgl_beli.get()   
        bulan = bln_belii.get()
        kotaasal = kota.get()
        no_kontak = kontak.get()

        if nama == '' or alamat == '' or tanggal == '' or bulan == '' :
            tkinter.messagebox.showwarning('Information','Isi data customer terlebih dahulu!')
            return

        def go_atm():
            menu_pembayaran.destroy()
            keranjang.config(os.system('python pembayaran2.py'))

        def go_mbanking():
            menu_pembayaran.destroy()
            keranjang.config(os.system('python pembayaran.py'))
            

        def go_cash():
            menu_pembayaran.destroy()
            keranjang.config(os.system('python pembayaran3.py'))

        customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

        menu_pembayaran = customtkinter.CTk()  # membuat cutstom tkinter window
        menu_pembayaran.geometry("300x200")
        menu_pembayaran.title('Metode Pembayaran')

        # Frame
        frame1 = customtkinter.CTkFrame(menu_pembayaran,width=400,height=40,fg_color='#222873')
        frame1.place(x=-10,y=0)
        label1= customtkinter.CTkLabel(frame1,text='Pilih pembayaran!',font=('Segoe Print',19),text_color='white')
        label1.place(x=70,y=5)

        button1 = customtkinter.CTkButton(menu_pembayaran,text='Transfer ATM',command=go_atm)
        button1.place(x=80,y=60)

        button2 = customtkinter.CTkButton(menu_pembayaran,text='Mobile Banking',command=go_mbanking)
        button2.place(x=80,y=110)
        
        button3 = customtkinter.CTkButton(menu_pembayaran,text='Cash (ditempat)',command=go_cash)
        button3.place(x=80,y=160)

        menu_pembayaran.mainloop()


    def keluar():
        tkinter.messagebox.showinfo('Information','Terima Kasih Atas Kunjungan Anda!')
        keranjang.destroy()
        keranjang.config(os.system('python login_page.py'))


        customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

        menu_pembayaran = customtkinter.CTk()  # membuat cutstom tkinter window
        menu_pembayaran.geometry("300x200")
        menu_pembayaran.title('Metode Pembayaran')

        # Frame
        frame1 = customtkinter.CTkFrame(menu_pembayaran,width=400,height=40,fg_color='#222873')
        frame1.place(x=-10,y=0)
        label1= customtkinter.CTkLabel(frame1,text='Pilih pembayaran!',font=('Segoe Print',19),text_color='white')
        label1.place(x=70,y=5)

        button1 = customtkinter.CTkButton(menu_pembayaran,text='Transfer ATM',command=go_atm)
        button1.place(x=80,y=60)

        button2 = customtkinter.CTkButton(menu_pembayaran,text='Mobile Banking',command=go_mbanking)
        button2.place(x=80,y=110)
        
        button3 = customtkinter.CTkButton(menu_pembayaran,text='Cash (ditempat)',command=go_cash)
        button3.place(x=80,y=160)

        menu_pembayaran.mainloop()



    
    def enter_data():
        nama = nama_cust.get()
        alamat = alamat_cust.get()
        tanggal = tgl_beli.get()   
        bulan = bln_belii.get()

        if nama == '' or alamat == '' or tanggal == '' or bulan == '' :
            tkinter.messagebox.showerror('Information','Terdapat data yang kosong!')
            return
        
        else :
            try :
                conn = sqlite3.connect('daftar_akun.db')
                cur = conn.cursor()
                cur.execute('''insert into data_pelanggan (nama,alamat,tanggal,bulan,produk_dibeli,total_belanja) values (?,?,?,?,?,?)''',(nama,alamat,tanggal,bulan,jumlah_produk_dipilih,total))
                conn.commit()
                conn.close()
            
            except ValueError:
                tkinter.messagebox.showerror('Error','Format input salah!')
                nama_cust.delete(0,END)
                alamat_cust.delete(0,END)
                tgl_beli.delete(0,END)
                bln_belii.delete(0,END)
            
            else :
                tkinter.messagebox.showinfo('Information','Data berhasil ditambahkan!')
                # keranjang.destroy()
                # keranjang.config(os.system('python login_page.py'))

    customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

    keranjang = customtkinter.CTk()  # membuat cutstom tkinter window
    keranjang.geometry("1100x700")
    keranjang.title('Keranjang Belanja')

    label1=customtkinter.CTkLabel(keranjang, text="Data Pembelian Konsumen",font=('Swis721 Blk BT',17),text_color='#222873')
    label1.place(x=60,y=170)

    
    # # Frame & label atas
    top_frame = customtkinter.CTkFrame(master=keranjang,width=1500,height=80,fg_color='#222873')
    top_frame.place(x=-10,y=0)

    label1=customtkinter.CTkLabel(master=top_frame, text="Hello, Welcome To The Store!",font=('Ink Free',17,'bold'),text_color='white')
    label1.place(x=20,y=7)
    label1=customtkinter.CTkLabel(master=top_frame, text="Toko Furniture Bahagia",font=('Swis721 Blk BT',21),text_color='white')
    label1.place(x=20,y=35)
    tagline=customtkinter.CTkLabel(top_frame, text="Discover the Art of Stylish Living",font=('Monotype Corsiva',22),text_color='white')
    tagline.place(x=820,y=35)
    frame_judul=customtkinter.CTkFrame(keranjang,fg_color='white',width=1200,height=70)
    frame_judul.place(x=0,y=80)

    judul_halaman = customtkinter.CTkLabel(frame_judul,text='Keranjang Belanja',font=('Segoe Print',19,'bold'),text_color='#222873')
    judul_halaman.place(x=450,y=20)

    # Button back menu
    button_back_menu = customtkinter.CTkButton(keranjang, width=150, text="Home Menu",font=('Segoe UI Semibold',15), corner_radius=6,command=go_menu)
    button_back_menu.place(x=900, y=95)

    # Frame data customer
    middle_frame = customtkinter.CTkFrame(master=keranjang,width=620,height=160,fg_color='#fff',corner_radius=-10)
    middle_frame.place(x=25,y=215)

    label1 = customtkinter.CTkLabel(middle_frame,text='Nama Customer')
    label1.place(x=30,y=15)

    label2 = customtkinter.CTkLabel(middle_frame,text='Alamat Lengkap')
    label2.place(x=30,y=80)

    label3 = customtkinter.CTkLabel(middle_frame,text='Tanggal')
    label3.place(x=230,y=15)

    label4 = customtkinter.CTkLabel(middle_frame,text='Bulan')
    label4.place(x=330,y=15)

    label5 = customtkinter.CTkLabel(middle_frame,text='Kontak',width=100)
    label5.place(x=430,y=15)

    label6 = customtkinter.CTkLabel(middle_frame,text='Asal Kota',width=100)
    label6.place(x=310,y=80)

    nama_cust = customtkinter.CTkEntry(middle_frame,width=170,placeholder_text='......')
    nama_cust.place(x=30,y=45)
    alamat_cust = customtkinter.CTkEntry(middle_frame,width=265,placeholder_text='......')
    alamat_cust.place(x=30,y=110)
    tgl_beli = customtkinter.CTkEntry(middle_frame,width=50,placeholder_text='...')
    tgl_beli.place(x=230,y=45)
    bln_belii = customtkinter.StringVar(value='...')
    bln_option = customtkinter.CTkComboBox(middle_frame,values=['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],variable=bln_belii)
    bln_option.place(x=290,y=45)
    kontak = customtkinter.CTkEntry(middle_frame,width=150,placeholder_text='number')
    kontak.place(x=450,y=45)
    kota = customtkinter.StringVar(value='...')
    kota_option = customtkinter.CTkComboBox(middle_frame,values=['Jakarta', 'Bandung', 'Bogor', 'Depok','Cimahi','Surabaya','Tanggerang','Bekasi'],variable=kota)
    kota_option.place(x=310,y=110)

    # Frame info harga total
    frame_info = customtkinter.CTkFrame(keranjang,width=350,height=200,fg_color='#fff',corner_radius=-10,border_width=2,border_color='#222873')
    frame_info.place(x=680,y=175)

    label1 = customtkinter.CTkLabel(frame_info,text='Total belanja :',font=('Cascadia Code ExtraLight',17,'bold'))
    label1.place(x=20,y=15)

    label2 = customtkinter.CTkLabel(frame_info,text='Total produk  :',font=('Cascadia Code ExtraLight',17,'bold'))
    label2.place(x=20,y=65)

    display_harga = customtkinter.CTkLabel(frame_info,text=f'Rp. {total}',font=('Microsoft JhengHei',17),text_color='blue')
    display_harga.place(x=200,y=15)

    display_jumlah = customtkinter.CTkLabel(frame_info,text=f'{jumlah_produk_dipilih}',font=('Microsoft JhengHei',17),text_color='blue')
    display_jumlah.place(x=270,y=65)

    # Button
    enter_button = customtkinter.CTkButton(middle_frame,text='Enter',width=120,command=enter_data)
    enter_button.place(x=470,y=110)

    label1=customtkinter.CTkLabel(keranjang, text="Keranjang",font=('Swis721 Blk BT',17),text_color='#222873')
    label1.place(x=210,y=390)

    invoice_button = customtkinter.CTkButton(frame_info,text='Cetak Invoice',width=310,font=('Segoe UI Semibold',15),command=go_cetakInv)
    invoice_button.place(x=20,y=120)

    bayar_button = customtkinter.CTkButton(frame_info,text='Informasi Pembayaran',width=310,font=('Segoe UI Semibold',15),command=go_bayar)
    bayar_button.place(x=20,y=160)
    

    # Frame keranjang
    frame_keranjang = customtkinter.CTkFrame(master=keranjang,width=700,height=240,fg_color='#fff',corner_radius=20,border_width=2,border_color='#222873')
    frame_keranjang.place(x=210,y=430)

    label_bg = customtkinter.CTkLabel(frame_keranjang,width=695,height=130,fg_color='#e6f2ff')
    label_bg.place(x=2,y=60)

    # Membuat treeview
    tree = ttk.Treeview(
        frame_keranjang,columns=('Produk', 'Harga satuan (Rp)', 'Jumlah','Total (Rp)'), show='headings'
    )
    tree.heading("Produk", text="Produk")
    tree.heading("Harga satuan (Rp)", text="Harga satuan (Rp)")
    tree.heading("Jumlah", text="Jumlah")
    tree.heading("Total (Rp)", text="Total (Rp)")
    tree.place(x=40,y=40)

    # Memasukkan data ke dalam kolom-kolom Treeview
    for row in result_seluruh:
        tree.insert("", "end", values=row)

    exit_button = ctk.CTkButton(keranjang,width=100,text='Keluar',command=keluar)
    exit_button.place(x=930,y=600)
        
    keranjang.config()
    keranjang.mainloop()
keranjang()