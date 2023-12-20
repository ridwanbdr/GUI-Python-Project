#importing required modules
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import tkinter.messagebox
import os
import sqlite3


def select():
    username = username_entry.get()
    password = password_entry.get()

    if password != 'admin' :
        tkinter.messagebox.showinfo('Information','Log in gagal!')
        return
    else :
        tkinter.messagebox.showinfo('Information','Log in berhasil!')
        login_page.destroy()
        login_page.config(os.system('python menu_admin.py'))

def go_back():
    login_page.destroy()
    login_page.config(os.system('python login_option.py'))


customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

login_page = customtkinter.CTk()  # membuat cutstom tkinter window
login_page.geometry("600x440")
login_page.title('Login')


gambar = Image.open('bg_login.png')
width = 1000
height = 700
resize = gambar.resize((width, height))
gambar_jadi1 = ImageTk.PhotoImage(resize)

img1=ImageTk.PhotoImage(Image.open("bg_login.png"))
l1=customtkinter.CTkLabel(login_page,image=gambar_jadi1,text='')
l1.place(x=0,y=0)

# frame input
frame_kiri = customtkinter.CTkFrame(login_page,width=250,height=280,fg_color='#E8E8E8',corner_radius=10)
frame_kiri.place(x=50,y=40)

l2=customtkinter.CTkLabel(frame_kiri, text="Hello, Admin!",font=('Century Gothic',18))
l2.place(x=70,y=20)

l2=customtkinter.CTkLabel(frame_kiri, text="Welcome To The Store!",font=('Century Gothic',14))
l2.place(x=45,y=50)

username_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Username')
username_entry.place(x=40, y=100)

password_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Password : admin', show="*")
password_entry.place(x=40, y=145)


#Create buttons
login_button = customtkinter.CTkButton(master=frame_kiri, width=170, text="Login", command=select, corner_radius=6)
login_button.place(x=40, y=200)

back_button = customtkinter.CTkButton(frame_kiri,text='Back',width=130,command=go_back)
back_button.place(x=60,y=235)


# frame background
frame=customtkinter.CTkFrame(login_page, width=300, height=500,fg_color='white')
frame.place(x=700,y=0)

l3=customtkinter.CTkLabel(frame,image=img1)
l3.place(x=0, y=0)


login_page.mainloop()