import tkinter
from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import ImageTk,Image
from PIL import *
import tkinter.messagebox
import tkinter.messagebox as messagebox
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


def ruang_tamu():
    
    def pilih_produk():
        rtamu_page.config(os.system('python buat_tes.py'))
    
    def pilih_produk (nama,harga):
        confirm = messagebox.askyesno('Confirmation','Tambahkan ke keranjang?')
        if confirm == True:
            input_jumlah = customtkinter.CTkInputDialog(text="Masukkan jumlah produk :", title="Input Jumlah")
            try :
                jumlah = input_jumlah.get_input()
                jumlah = int(jumlah)
                harga_total = jumlah*harga
                conn = sqlite3.connect('daftar_akun.db')
                cur = conn.cursor()
                cur.execute('''insert into keranjang (name,harga,jumlah,harga_total) values (?,?,?,?)''',(nama,harga,jumlah,harga_total))
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Informasi", "Produk ditambahkan ke keranjang!")
            except ValueError:
                messagebox.showerror('Error','Masukkan jumlah dalam angka!')
                return
        else:
            messagebox.showinfo("Informasi", "Anda memilih tidak.")

    def buttonclick():
        def backmenu():
            new_window.destroy()
            menu_utama()

        menu_page.destroy()
        new_window = customtkinter.CTk()
        new_window.geometry('600x300')
        new_window.title('New Window')
        back_button = customtkinter.CTkButton(new_window, width=40, text="Menu", font=('Segoe UI Semibold',15), corner_radius=6,command=backmenu)
        back_button.pack()
        new_window.mainloop()

    
    def go_menu():
        rtamu_page.destroy()
        button1.config(os.system('python main_menu.py'))

    customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

    rtamu_page = customtkinter.CTk()  # membuat cutstom tkinter window
    rtamu_page.geometry("1100x750")
    rtamu_page.title('Menu')
    
    # # Frame & label atas
    top_frame = customtkinter.CTkFrame(master=rtamu_page,width=1500,height=80,fg_color='#222873')
    top_frame.place(x=-10,y=0)

    label1=customtkinter.CTkLabel(master=top_frame, text="Hello, Welcome To The Store!",font=('Ink Free',17,'bold'),text_color='white')
    label1.place(x=20,y=7)
    label1=customtkinter.CTkLabel(master=top_frame, text="Toko Furniture Bahagia",font=('Swis721 Blk BT',21),text_color='white')
    label1.place(x=20,y=35)
    tagline=customtkinter.CTkLabel(top_frame, text="Discover the Art of Stylish Living",font=('Monotype Corsiva',22),text_color='white')
    tagline.place(x=820,y=35)

    tabview = customtkinter.CTkTabview(master=rtamu_page,width=1060,height=310,corner_radius=10,fg_color='white')
    tabview.place(x=20,y=100)

    tabview.add("katalog 1")  # add tab at the end
    tabview.add("katalog 2")  # add tab at the end
    tabview.set("katalog 1")  # set currently visible tab

    label1=customtkinter.CTkLabel(rtamu_page, text="Ruang Makan & Kantor",font=('Swis721 Blk BT',17),text_color='#222873')
    label1.place(x=60,y=85)

    # Button back menu
    button_back_menu = customtkinter.CTkButton(rtamu_page, width=150, text="Home Menu",font=('Segoe UI Semibold',15), corner_radius=6,command=go_menu)
    button_back_menu.place(x=900, y=85)
    
    # Fungsi atur komposisi gambar
    def aturgambar(gambar):
        produk = Image.open(gambar)
        width = 200
        height = 280
        resize = produk.resize((width,height))
        resize_image = ImageTk.PhotoImage(resize)
        produk_image = resize_image
        return produk_image


    # Frame atas
    # Tab 1
    frame_atas = customtkinter.CTkFrame(master=tabview.tab('katalog 1'),width=1100,height=270,fg_color='white',corner_radius=20)
    frame_atas.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'dapur/kursi1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    produk1 = 'Milagro Kursi Makan (abu-abu)'    
    harga_produk1 = 1099000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk1,harga_produk1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'dapur/kursi2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    produk2 = 'Medform Kursi Makan (krem)'
    harga_produk2 = 699000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk2,harga_produk2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    # produk 3
    produk = 'dapur/meja1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    produk3 = 'Lexi Set Meja Makan Lipat 2 Bangku'
    harga_produk3 = 559000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk3,harga_produk3),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)

    # produk 4
    produk = 'dapur/meja2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk4 = 'Lexon Set Meja Makan 4 Kursi'
    harga_produk4 = 1299000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk4,harga_produk4),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)

    # Tab 2
    frame_atas2 = customtkinter.CTkFrame(master=tabview.tab('katalog 2'),width=1100,height=270,fg_color='#fff',corner_radius=20)
    frame_atas2.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas2, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'dapur/meja3.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    produk5 = 'Informa Zeus Set Meja Makan'
    harga_produk5 = 1499000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk5,harga_produk5),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'dapur/kabinet1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk6 = 'Ivy Kitchen Set (abu-abu)'
    harga_produk6 = 5099400

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk6,harga_produk6),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    # produk 3
    produk = 'dapur/kabinet2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk7 = 'Sky Kabinet Dapur Metal (putih)'
    harga_produk7 = 4799000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk7,harga_produk7),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)




    # Frame bawah
    tabview2 = customtkinter.CTkTabview(master=rtamu_page,width=1060,height=300,corner_radius=10,fg_color='white')
    tabview2.place(x=20,y=420)

    tabview2.add("katalog 1")  # add tab at the end
    tabview2.add("katalog 2")  # add tab at the end
    tabview2.set("katalog 1")  # set currently visible tab
    # Tab 1
    frame_atas = customtkinter.CTkFrame(master=tabview2.tab('katalog 1'),width=1100,height=270,fg_color='white',corner_radius=20)
    frame_atas.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'dapur/mejakantor1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk8 = 'Maine Meja Kantor 1'
    harga_produk8 = 1999000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk8,harga_produk8),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'dapur/mejakantor2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk9 = 'Maine Meja Kantor 2'
    harga_produk9 = 2199000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk9,harga_produk9),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    # produk 3
    produk = 'dapur/mejakantor3.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk10 = 'Montana Meja Kantor (cokelat)'
    harga_produk10 = 5199000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk10,harga_produk10),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)

    # produk 4
    produk = 'dapur/mejakantor4.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk11 = 'Mont Meja Kantor Ekstensi (hijau)'
    harga_produk11 = 4799000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk11,harga_produk11),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)

    # Tab 2
    frame_atas2 = customtkinter.CTkFrame(master=tabview2.tab('katalog 2'),width=1100,height=270,fg_color='#fff',corner_radius=20)
    frame_atas2.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas2, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'dapur/lemarikantor1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk12 = 'Kiev Lemari Arsip 2 Pintu'
    harga_produk12 = 1899000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk12,harga_produk12),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'dapur/lemarikantor2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    produk13 = 'Informa Rhein Lemari Arsip'
    harga_produk13 = 3899000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(produk13,harga_produk13),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    rtamu_page.config()
    rtamu_page.mainloop()
ruang_tamu()