import tkinter
from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import ImageTk,Image
from PIL import *
import tkinter.messagebox
import os
import sqlite3

conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''create table if not exists keranjang (
    name text not null,
    harga int not null,
    jumlah int,
    harga_total int
)''')
conn.commit()
conn.close()

def menu_utama():

    def go_ruangtamu():
        menu_page.destroy()
        menu_page.config(os.system('python ruang_tamu.py'))

    def go_dapur_kantor():
        menu_page.destroy()
        menu_page.config(os.system('python dapur_kantor.py'))

    def go_keranjang():
        menu_page.destroy()
        menu_page.config(os.system('python keranjang.py'))

    

    customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

    menu_page = customtkinter.CTk()  # membuat cutstom tkinter window
    menu_page.geometry("1100x750")
    menu_page.title('Menu')

    label1=customtkinter.CTkLabel(menu_page, text="Home Menu",font=('Swis721 Blk BT',17),text_color='#222873')
    label1.place(x=60,y=88)

    label1=customtkinter.CTkLabel(menu_page, text="Kategori",font=('Swis721 Blk BT',17),text_color='#222873')
    label1.place(x=60,y=405)
    
    # # Frame & label atas
    top_frame = customtkinter.CTkFrame(master=menu_page,width=1500,height=80,fg_color='#222873')
    top_frame.pack(side='top',fill='x')

    label1=customtkinter.CTkLabel(master=top_frame, text="Hello, Welcome To The Store!",font=('Ink Free',17,'bold'),text_color='white')
    label1.place(x=20,y=7)
    
    label1=customtkinter.CTkLabel(master=top_frame, text="Toko Furniture Bahagia",font=('Swis721 Blk BT',21),text_color='white',justify='left')
    label1.place(x=20,y=35)

    tagline=customtkinter.CTkLabel(top_frame, text="Discover the Art of Stylish Living",font=('Monotype Corsiva',22),text_color='white')
    tagline.place(x=820,y=35)

    # Frame dan label tengah
    middle_frame = customtkinter.CTkFrame(master=menu_page,width=985,height=265,fg_color='#fff',corner_radius=20)
    middle_frame.place(x=55,y=125)


    # Membaca gambar
    banner_image = Image.open('banner.webp')

    # Mengubah ukuran gambar
    width = 1200  # Lebar yang diinginkan
    height = 300  # Tinggi yang diinginkan
    banner_image = banner_image.resize((width, height))

    # Membuat objek PhotoImage dari gambar yang telah diubah ukurannya
    banner = ImageTk.PhotoImage(banner_image)

    # Membuat label dengan gambar
    banner_label = ctk.CTkLabel(middle_frame, image=banner, bg_color="#fff")
    banner_label.place(x=10, y=14)


    # Frame Kategori Produk
    kategori_frame = customtkinter.CTkFrame(master=menu_page,width=985,height=255,fg_color='#fff',corner_radius=20)
    kategori_frame.place(x=55,y=450)

    # label background kategori
    my_label=customtkinter.CTkLabel(master=kategori_frame, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=33)

    # Ruang Tamu
    kategori1 = Image.open('ruangtamu.jpg')
    width = 200
    height = 150
    kategori1 =  kategori1.resize((width,height))
    kategori1_image = ImageTk.PhotoImage(kategori1)

    button1 = customtkinter.CTkButton(kategori_frame, width=120, text="", font=('Segoe UI Semibold',15), corner_radius=6,command=go_ruangtamu,image=kategori1_image,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=35, y=20)

    # Ruang Tidur
    kategori2 = Image.open('ruangtidur.jpg')
    width = 200
    height = 150
    kategori2 =  kategori2.resize((width,height))
    kategori2_image = ImageTk.PhotoImage(kategori2)

    button1 = customtkinter.CTkButton(kategori_frame, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command=go_ruangtamu,image=kategori2_image,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=280, y=20)

    # Ruang Dapur
    kategori3 = Image.open('kitchen.jpg')
    width = 200
    height = 150
    kategori3 =  kategori3.resize((width,height))
    kategori3_image = ImageTk.PhotoImage(kategori3)

    button2 = customtkinter.CTkButton(kategori_frame, width=170, text="", font=('Segoe UI Semibold',15),corner_radius=6,command=go_dapur_kantor,image=kategori3_image,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button2.place(x=540, y=20)

    # Ruang kerja
    kategori4 = Image.open('office.jpg')
    width = 200
    height = 150
    kategori4 =  kategori4.resize((width,height))
    kategori4_image = ImageTk.PhotoImage(kategori4)

    button2 = customtkinter.CTkButton(kategori_frame, width=170, text="", font=('Segoe UI Semibold',15),corner_radius=6,command=go_dapur_kantor,image=kategori4_image,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button2.place(x=780, y=20)

    # Deskripsi Kategori
    desc11=customtkinter.CTkLabel(master=kategori_frame, text="Sofa, Kursi",font=('Futura Md BT',14),text_color='#222873')
    desc11.place(x=81,y=150)
    desc12=customtkinter.CTkLabel(master=kategori_frame, text="Meja, Lemari TV",font=('Futura Md BT',14),text_color='#222873')
    desc12.place(x=68,y=170)

    desc21=customtkinter.CTkLabel(master=kategori_frame, text="Tempat tidur, Laci,",font=('Futura Md BT',14),text_color='#222873')
    desc21.place(x=304,y=150)
    desc22=customtkinter.CTkLabel(master=kategori_frame, text="Lemari pakaian",font=('Futura Md BT',14),text_color='#222873')
    desc22.place(x=313,y=170)

    desc31=customtkinter.CTkLabel(master=kategori_frame, text="Meja, Kursi,",font=('Futura Md BT',14),text_color='#222873')
    desc31.place(x=584,y=150)
    desc32=customtkinter.CTkLabel(master=kategori_frame, text="Kabinet",font=('Futura Md BT',14),text_color='#222873')
    desc32.place(x=594,y=170)

    desc41=customtkinter.CTkLabel(master=kategori_frame, text="Meja kantor, Kursi",font=('Futura Md BT',14),text_color='#222873')
    desc41.place(x=806,y=150)
    desc42=customtkinter.CTkLabel(master=kategori_frame, text=" kantor, Sofa",font=('Futura Md BT',14),text_color='#222873')
    desc42.place(x=816,y=170)


   
    # Buttons
    button1 = customtkinter.CTkButton(kategori_frame, width=170, text="Ruang Tamu", font=('Segoe UI Semibold',15), corner_radius=6,command=go_ruangtamu)
    button1.place(x=40, y=204)
    button1 = customtkinter.CTkButton(kategori_frame, width=170, text="Kamar Tidur",font=('Segoe UI Semibold',15), corner_radius=6,command=go_ruangtamu)
    button1.place(x=285, y=204)
    button2 = customtkinter.CTkButton(kategori_frame, width=170, text="Ruang Makan & Dapur", font=('Segoe UI Semibold',15),corner_radius=6,command=go_dapur_kantor)
    button2.place(x=545, y=204)
    button2 = customtkinter.CTkButton(kategori_frame, width=170, text="Ruang Kantor", font=('Segoe UI Semibold',15),corner_radius=6,command=go_dapur_kantor)
    button2.place(x=785, y=204)

    button_keranjang = customtkinter.CTkButton(menu_page,width=120, text='Keranjang',font=('Segoe UI Semibold',15),command=go_keranjang)
    button_keranjang.place(x=900,y=405)

    menu_page.config()
    menu_page.mainloop()
menu_utama()