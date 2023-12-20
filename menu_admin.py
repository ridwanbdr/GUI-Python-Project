import tkinter as tk
from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import ImageTk, Image
import tkinter.messagebox
import os
import sqlite3
import matplotlib.pyplot as plt

list_bulan = []

# Mengambil data bulan di halaman keranjang
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT bulan FROM data_pelanggan''')
result_bulan = cur.fetchone()
all_bulan = result_bulan[0]
list_bulan.append(all_bulan)
conn.commit()
conn.close()

# Mengambil data produk dibeli di halaman keranjang
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT produk_dibeli FROM data_pelanggan''')
result_bykproduk = cur.fetchall()
conn.commit()
conn.close()

total_produk = 0
for row in result_bykproduk:
    total_produk += row[0]


# Mengambil data total belanja di halaman keranjang
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT AVG(total_belanja) FROM data_pelanggan''')
result_totalbelanja = cur.fetchone()
avg_totalbelanja = result_totalbelanja[0]  # Mengambil nilai rata-rata dari hasil query
total_belanja = round(avg_totalbelanja, 2)
conn.commit()
conn.close()


# Mengambil jumlah data akun yang terdaftar dalam database
conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''SELECT COUNT(*) FROM tabel_akun''')
result_totalakun = cur.fetchone()
count_akun = result_totalakun[0]
conn.commit()
conn.close()

total_akun = count_akun
total_terjual = total_produk
rata2pembelian = total_belanja

def button1():
    daftar_bulan = ['Januari','Feburari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
    produk_terjual = [13,20,13,12,39,13,17,9,12,10,8,22]
    lebar_bar = 0.5

    fig,ax=plt.subplots(figsize=(11,6))
    plt.bar(daftar_bulan,produk_terjual,width=lebar_bar,label='Penjualan Per Bulan')

    plt.title('Penjualan Berdasarkan Bulan')
    plt.ylabel('Penjualan')
    plt.xlabel('Bulan')

    plt.legend()
    plt.show()


def button2():
    # Data untuk diagram lingkaran
    labels = ['Jakarta', 'Bandung', 'Bogor', 'Depok','Cimahi','Surabaya','Tanggerang','Bekasi']
    sizes = [30, 38, 25, 19,11,7,21,23]  # Persentase masing-masing bagian
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink','blue','red','green','grey']
    explode = (0.2, 0.1, 0, 0,0,0,0,0)  # Memberikan efek "meledakkan" bagian pertama

    # Membuat diagram lingkaran
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)

    # Menampilkan legenda
    plt.legend(labels, loc='best')

    # Memberikan judul pada diagram lingkaran
    plt.title('Penjualan Berdasarkan Kota')

    # Menampilkan diagram lingkaran
    plt.axis('equal')
    plt.show()

def go_vendor():
    menuadmin.destroy()
    menuadmin.config(os.system('python vendor_list.py'))

def close_window():
    response = tkinter.messagebox.askyesno('Exit', 'Are you sure want to exit?')
    if response:
        menuadmin.destroy()

customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

menuadmin = customtkinter.CTk()  # create custom tkinter window
menuadmin.geometry("700x500")
menuadmin.title('Dashboard Admin')
menuadmin.resizable(False,False)

title = ctk.CTkLabel(menuadmin,text='Dashboard')
title.place(x=230,y=60)

# Frame Kiri (menu)
frame = customtkinter.CTkFrame(menuadmin, width=200, height=530, fg_color='#222873')
frame.place(x=-5, y=-5)

label = ctk.CTkLabel(frame,text='Hello, Welcome Back!',text_color='white',font=('Ink Free',17,'bold'))
label.place(x=20,y=20)

label = ctk.CTkLabel(frame,text='Halo admin :) ',text_color='white',font=('calibri',17,'bold'))
label.place(x=20,y=40)

label = ctk.CTkLabel(frame,text='Toko Furniture Bahagia',text_color='white')
label.place(x=30,y=200)

gambar = Image.open('store.png')
width = 150
height = 90
resize = gambar.resize((width, height))
gambar_jadi1 = ImageTk.PhotoImage(resize)

label_gambar1 = ctk.CTkLabel(frame,text='',image=gambar_jadi1)
label_gambar1.place(x=40,y=100)

menu1 = ctk.CTkButton(frame,width=150,text='Selling by Month',fg_color='#2f369d',command=button1)
menu1.place(x=20,y=260)

menu1 = ctk.CTkButton(frame,width=150,text='Selling by Address',fg_color='#2f369d',command=button2)
menu1.place(x=20,y=320)

menu1 = ctk.CTkButton(frame,width=150,text='Product Stocks',fg_color='#2f369d')
menu1.place(x=20,y=380)

menu1 = ctk.CTkButton(frame,width=150,text='Vendor Lists',fg_color='#2f369d',command=go_vendor)
menu1.place(x=20,y=440)

# Frame Atas
frame2= customtkinter.CTkFrame(menuadmin, width=485, height=50, fg_color='white',corner_radius=10,border_width=3,border_color='#cccccc')
frame2.place(x=205, y=3)

gambar = Image.open('burgermenu.png')
width = 30
height = 30
resize = gambar.resize((width, height))
gambar_jadi1 = ImageTk.PhotoImage(resize)

label_gambar1 = ctk.CTkButton(frame2,text='',image=gambar_jadi1,width=30,fg_color='white',hover_color='grey')
label_gambar1.place(x=15,y=9)

search_box = ctk.CTkEntry(frame2,width=250,placeholder_text='Search')
search_box.place(x=100,y=10)

# Frame informasi (1)
frame2= customtkinter.CTkFrame(menuadmin, width=485, height=150, fg_color='white',corner_radius=10)
frame2.place(x=205, y=100)

gambar = Image.open('statistik.png')
width = 150
height = 100
resize = gambar.resize((width, height))
gambar_jadi1 = ImageTk.PhotoImage(resize)

label_gambar1 = ctk.CTkLabel(frame2,text='',image=gambar_jadi1)
label_gambar1.place(x=20,y=5)
label_desc = ctk.CTkLabel(frame2,text=f'Rp.{rata2pembelian}',text_color='red')
label_desc.place(x=25,y=95)
label_desc = ctk.CTkLabel(frame2,text='Average Buying',text_color='blue')
label_desc.place(x=30,y=120)

gambar2 = Image.open('statistik2.png')
width = 150
height = 100
resize = gambar2.resize((width, height))
gambar_jadi2 = ImageTk.PhotoImage(resize)

label_gambar2 = ctk.CTkLabel(frame2,text='',image=gambar_jadi2)
label_gambar2.place(x=135,y=10)
label_desc = ctk.CTkLabel(frame2,text=f'{total_terjual} items',text_color='red')
label_desc.place(x=160,y=95)
label_desc = ctk.CTkLabel(frame2,text='Products',text_color='blue')
label_desc.place(x=165,y=120)


gambar3 = Image.open('akun.jpeg')
width = 100
height = 100
resize = gambar3.resize((width, height))
gambar_jadi3 = ImageTk.PhotoImage(resize)

label_gambar3 = ctk.CTkLabel(frame2,text='',image=gambar_jadi3)
label_gambar3.place(x=280,y=10)
label_desc = ctk.CTkLabel(frame2,text=f'{total_akun}',text_color='red')
label_desc.place(x=310,y=95)
label_desc = ctk.CTkLabel(frame2,text='Account Registered',text_color='blue')
label_desc.place(x=270,y=120)

gambar4 = Image.open('statistik3.png')
width = 110
height = 110
resize = gambar4.resize((width, height))
gambar_jadi4 = ImageTk.PhotoImage(resize)

label_gambar4 = ctk.CTkLabel(frame2,text='',image=gambar_jadi4)
label_gambar4.place(x=390,y=10)

# Frame informasi (2)
frame3= customtkinter.CTkFrame(menuadmin, width=150, height=150, fg_color='white',corner_radius=10)
frame3.place(x=240, y=300)

gambar_stok = Image.open('stok.png')
width = 150
height = 160
resize = gambar_stok.resize((width, height))
gambar_stok1 = ImageTk.PhotoImage(resize)

button_stok = ctk.CTkButton(frame3,image=gambar_stok1,width=120,height=120,text='',fg_color='white',hover_color='grey')
button_stok.place(x=5,y=5)

# Frame informasi (3)
frame4= customtkinter.CTkFrame(menuadmin, width=150, height=150, fg_color='white',corner_radius=10)
frame4.place(x=410, y=300)

gambar_supplier = Image.open('supplier.png')
width = 150
height = 160
resize = gambar_supplier.resize((width, height))
gambar_supplier1 = ImageTk.PhotoImage(resize)

button_stok = ctk.CTkButton(frame4,image=gambar_supplier1,width=120,height=120,text='',fg_color='white',hover_color='grey',command=go_vendor)
button_stok.place(x=5,y=5)

menuadmin.protocol('WM_DELETE_WINDOW', close_window)

menuadmin.mainloop()