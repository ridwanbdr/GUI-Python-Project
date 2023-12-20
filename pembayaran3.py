import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import tkinter.messagebox
import os
import sqlite3

customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

mbanking = customtkinter.CTk()  # create custom tkinter window
mbanking.geometry("610x400")
mbanking.title('Cash / Tunai')

frame = customtkinter.CTkFrame(mbanking, width=570, height=360, fg_color='white')
frame.place(x=20, y=20)

gambar = Image.open('pembayaran/cash.jpg')
width = 700
height = 440
resize = gambar.resize((width, height))
gambar_jadi = ImageTk.PhotoImage(resize)

label_gambar = customtkinter.CTkLabel(frame, image=gambar_jadi, bg_color='white',text='')
label_gambar.place(x=5, y=5)

mbanking.mainloop()
