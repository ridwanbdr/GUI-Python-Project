#importing required modules
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import tkinter.messagebox
import os
import sqlite3


def go_admin():
    login_page.destroy()
    login_page.config(os.system('python login_admin.py'))

def go_customer():
    login_page.destroy()
    login_page.config(os.system('python login_page.py'))

def select():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('daftar_akun.db')
    cur = conn.cursor()
    cur.execute('''select * from tabel_akun where username=? and password = ?''',(username,password))
    result = cur.fetchall()
    if len(result) == 0 :
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        tkinter.messagebox.showinfo('Information','Log in belum berhasil!')
    else :
        tkinter.messagebox.showinfo('Information','Log in berhasil!')
        cur.execute('drop table if exists keranjang')
        cur.execute('drop table if exists all_product')
        cur.execute('drop table if exists jumlah_dipilih')
        cur.execute('drop table if exists harga_satuan')
        cur.execute('drop table if exists harga_total')
        login_page.destroy()
        login_page.config(os.system('python main_menu.py'))


customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

login_page = customtkinter.CTk()  # membuat cutstom tkinter window
login_page.geometry("600x440")
login_page.title('Login')

img1=ImageTk.PhotoImage(Image.open("login_option.png"))

l3=customtkinter.CTkLabel(login_page,image=img1,text='')
l3.place(x=0, y=0)

l3=customtkinter.CTkLabel(login_page,fg_color='#222873',text='',width=700,height=10)
# l3.place(x=0, y=120)

welcome = Image.open('welcome.png')
width = 615
height = 150
resize = welcome.resize((width, height))
welcome1 = ImageTk.PhotoImage(resize)

l3=customtkinter.CTkLabel(login_page,image=welcome1,text='')
l3.place(x=110, y=0)

# Button gambar
gambar_supplier = Image.open('as_customer.png')
width = 130
height = 130
resize = gambar_supplier.resize((width, height))
gambar_supplier1 = ImageTk.PhotoImage(resize)

button_stok = customtkinter.CTkLabel(login_page,image=gambar_supplier1,width=120,height=120,text='',fg_color='white')
button_stok.place(x=0,y=0)

gambar_supplier = Image.open('as_customer2.png')
width = 160
height = 160
resize = gambar_supplier.resize((width, height))
gambar_supplier1 = ImageTk.PhotoImage(resize)

button_stok = customtkinter.CTkButton(login_page,image=gambar_supplier1,width=120,height=120,text='',fg_color='white',hover_color='grey',command=go_customer)
button_stok.place(x=120,y=180)

gambar_supplier = Image.open('as_admin.png')
width = 160
height = 160
resize = gambar_supplier.resize((width, height))
gambar_supplier1 = ImageTk.PhotoImage(resize)

button_stok = customtkinter.CTkButton(login_page,image=gambar_supplier1,width=120,height=120,text='',fg_color='white',hover_color='grey',command=go_admin)
button_stok.place(x=320,y=180)

login_page.mainloop()