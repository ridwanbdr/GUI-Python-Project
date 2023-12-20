#importing required modules
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import tkinter.messagebox
import os
import sqlite3

conn = sqlite3.connect('daftar_akun.db')
cur = conn.cursor()
cur.execute('''create table if not exists tabel_akun (
    name text not null,
    age int not null,
    username text not null primary key,
    password text not null
)''')
conn.commit()
conn.close()

def insert():
    name = name_entry.get()
    age = age_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if name == '' or age == '' or username == '' or password == '' :
        tkinter.messagebox.showerror('Information','Pendaftaran akun tidak berhasil!')
        return
    else :
        try :
            age = int(age)

            conn = sqlite3.connect('daftar_akun.db')
            cur = conn.cursor()
            cur.execute('''insert into tabel_akun (name,age,username,password) values (?,?,?,?)''',(name,age,username,password))
            conn.commit()
            conn.close()
            
        except sqlite3.IntegrityError:
            tkinter.messagebox.showerror('Error','Username telah terdaftar!')
            name_entry.delete(0,END)
            age_entry.delete(0,END)
            username_entry.delete(0,END)
            password_entry.delete(0,END)

        except ValueError:
            tkinter.messagebox.showerror('Error','Format input salah!')
            name_entry.delete(0,END)
            age_entry.delete(0,END)
            username_entry.delete(0,END)
            password_entry.delete(0,END)

        else :
            tkinter.messagebox.showinfo('Information','Sign up berhasil!')
            signup_page.destroy()
            signup_page.config(os.system('python login_page.py'))



customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

signup_page = customtkinter.CTk()  # membuat cutstom tkinter window
signup_page.geometry("600x440")
signup_page.title('Sign Up Account')


bg_signup = Image.open('ruangtamu.jpg')
width = 1000
height = 600
bg_signup =  bg_signup.resize((width,height))
signup_image = ImageTk.PhotoImage(bg_signup)

l1=customtkinter.CTkLabel(signup_page,image=signup_image)
l1.pack()


top_tagline =customtkinter.CTkLabel(signup_page, text="Hai, Welcome to the store!",font=('Century Gothic',17))
# top_tagline.place(x=200,y=25)

# frame input
frame_kiri = customtkinter.CTkFrame(signup_page,width=300,height=500)
frame_kiri.place(x=0,y=0)

label=customtkinter.CTkFrame(frame_kiri,width=320,height=60,fg_color='#222873')
label.place(x=-10,y=0)

nama_toko = customtkinter.CTkLabel(label,text='Toko Furniture Bahagia',font=('Swis721 Blk BT',14),text_color='white')
nama_toko.place(x=60,y=15)

l2=customtkinter.CTkLabel(frame_kiri, text="Create your account!",font=('Century Gothic',17))
l2.place(x=55,y=90)

name_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Name')
name_entry.place(x=60, y=130)

age_entry =customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Age')
age_entry.place(x=60, y=170)

username_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Username')
username_entry.place(x=60, y=210)

password_entry=customtkinter.CTkEntry(master=frame_kiri, width=170, placeholder_text='Password')
password_entry.place(x=60, y=250)


#Checkbox
check_button = customtkinter.CTkCheckBox(frame_kiri,text='Remember Me')
check_button.place(x=60,y=340)

#Create custom button
login_button = customtkinter.CTkButton(master=frame_kiri, width=170, text="Sign Up", command=insert, corner_radius=6)
login_button.place(x=60, y=300)


# frame background
frame=customtkinter.CTkFrame(signup_page, width=300, height=500,fg_color='white')
frame.place(x=700,y=0)

l3=customtkinter.CTkLabel(frame,image=signup_image)
l3.place(x=0, y=0)

signup_page.mainloop()