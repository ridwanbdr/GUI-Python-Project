#importing required modules
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import tkinter.messagebox
import os
import sqlite3


def go_signup():
    login_page.destroy()
    login_page.config(os.system('python signup_page.py'))

def close_window():
    response = tkinter.messagebox.askyesno('Exit', 'Are you sure want to exit?')
    if response:
        login_page.destroy()


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

img1=ImageTk.PhotoImage(Image.open("login2.jpg"))
l1=customtkinter.CTkLabel(login_page,image=img1)
l1.pack()

# frame input
frame_kiri = customtkinter.CTkFrame(login_page,width=300,height=300,fg_color='#E8E8E8')
frame_kiri.place(x=165,y=70)
l2=customtkinter.CTkLabel(frame_kiri, text="Welcome To The Store!",font=('Century Gothic',17))
l2.place(x=50,y=40)

username_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Username')
username_entry.place(x=60, y=100)

password_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Password', show="*")
password_entry.place(x=60, y=145)


#Checkbox
check_button = customtkinter.CTkCheckBox(frame_kiri,text='Remember Me')
check_button.place(x=50,y=240)

#Create buttons
login_button = customtkinter.CTkButton(master=frame_kiri, width=170, text="Login", command=select, corner_radius=6)
login_button.place(x=60, y=200)
signup_button = customtkinter.CTkButton(master=frame_kiri, width=60, text="Sign Up", text_color='blue',command=go_signup, corner_radius=6,fg_color='#E8E8E8',hover_color='#E8E8E8')
signup_button.place(x=180, y=240) 


# frame background
frame=customtkinter.CTkFrame(login_page, width=300, height=500,fg_color='white')
frame.place(x=700,y=0)

l3=customtkinter.CTkLabel(frame,image=img1)
l3.place(x=0, y=0)

login_page.protocol('WM_DELETE_WINDOW', close_window)

login_page.mainloop()