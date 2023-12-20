import tkinter
from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import ImageTk,Image
from PIL import *
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

    rtamu_page = customtkinter.CTk()  # membuat cutstom tkinter window
    rtamu_page.geometry("1100x750")
    rtamu_page.title('Menu')

    def pilih_produk():
        tkinter.messagebox.askyesno('Confirmation','Tambahkan ke keranjang?')
        if answer:
            messagebox.showinfo("Informasi", "Anda memilih Ya.")
        else:
            messagebox.showinfo("Informasi", "Anda memilih Tidak.")


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
        rtamu_page.config(os.system('python main_menu.py'))

    customtkinter.set_appearance_mode("light")  # Pilihan Mode: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Tema: blue (default), dark-blue, green

    
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

    label1=customtkinter.CTkLabel(rtamu_page, text="Ruang Tamu dan Kamar Tidur",font=('Swis721 Blk BT',17),text_color='#222873')
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
    produk = 'ruangtamu/sofa1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    sofa1 = 'Oakland sofa tidur fabric (abu-abu)'
    harga_sofa1 = 1099000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(sofa1,harga_sofa1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'ruangtamu/sofa2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    sofa2 = 'Informa windsor sofa tidur fabric (merah)'
    harga_sofa2 = 1599600

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command=lambda : pilih_produk(sofa2,harga_sofa2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)
   

    # produk 3  
    produk = 'ruangtamu/sofa3.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    sofa3 = 'Oakland sofa tidur fabric (coklat)'
    harga_sofa3 = 1099000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(sofa3,harga_sofa3),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)


    # produk 4
    produk = 'ruangtamu/meja0.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    meja1 = 'Neo helios meja sisi (biru muda)'
    harga_meja1 = 179000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(meja1,harga_meja1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)


    # Tab 2
    frame_atas2 = customtkinter.CTkFrame(master=tabview.tab('katalog 2'),width=1100,height=270,fg_color='#fff',corner_radius=20)
    frame_atas2.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas2, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'ruangtamu/meja1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    meja2 = 'Informa nordika meja tamu (cokelat)'
    harga_meja2 = 899000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(meja2,harga_meja2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)


    # produk 2
    produk = 'ruangtamu/meja2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    meja3 = 'Newmark meja tamu (cokelat)'
    harga_meja3 = 1899000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(meja3,harga_meja3),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)


    # produk 3
    produk = 'ruangtamu/lemaritv1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    lemaritv1 = 'Informa hampshire set lemari tv'
    harga_lemaritv1 = 2399000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(lemaritv1,harga_lemaritv1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)

    

    # produk 4
    produk = 'ruangtamu/lemaritv2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    lemaritv2 = 'Ricola rak tv (putih)'
    harga_lemaritv2 = 1199000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(lemaritv2,harga_lemaritv2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)

    
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
    produk = 'ruangtidur/kasur1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    kasur1 = 'Informa oberyn set'
    harga_kasur1 = 8600000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(kasur1,harga_kasur1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)

    # produk 2
    produk = 'ruangtidur/kasur2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    kasur2 = 'Informa elena set'
    harga_kasur2 = 8050000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(kasur2,harga_kasur2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    # produk 3
    produk = 'ruangtidur/laci1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    laci1 = 'Informa maxy laci pakaian'
    harga_laci1 = '1999500'

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(laci1,harga_laci1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)


    # produk 4
    produk = 'ruangtidur/laci2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    laci2 = 'Informa pexio laci penyimpanan'
    harga_laci2 = 599000

    button1 = customtkinter.CTkButton(frame_atas, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(laci2,harga_laci2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)


    # Tab 2
    frame_atas2 = customtkinter.CTkFrame(master=tabview2.tab('katalog 2'),width=1100,height=270,fg_color='#fff',corner_radius=20)
    frame_atas2.place(x=20,y=-20)

    my_label=customtkinter.CTkLabel(master=frame_atas2, text="",fg_color='#e6f2ff',width=1000,height=100)
    my_label.place(x=0,y=50)

    # produk 1
    produk = 'ruangtidur/laci3.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    laci3 = 'Informa hiro laci pakaian'
    harga_laci3 = 3299500

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(laci3,harga_laci3),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=20, y=25)


    # produk 2
    produk = 'ruangtidur/lemari1.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    lemari1 = 'Informa brino lemari pakaian'
    harga_lemari1 = 8999400

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(lemari1,harga_lemari1),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=270, y=25)

    # produk 3
    produk = 'ruangtidur/lemari2.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)
    
    lemari2 = 'Informa noella lemari pakaian'
    harga_lemari2 = 9379300

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(lemari2,harga_lemari2),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=545, y=25)

    # produk 4
    produk = 'ruangtidur/lemari3.png'
    aturgambar(gambar=produk)
    produk = aturgambar(gambar=produk)

    lemari3 = 'Informa maxy 2 lemari pakaian'
    harga_lemari3 = 1596000

    button1 = customtkinter.CTkButton(frame_atas2, width=170, text="",font=('Segoe UI Semibold',15), corner_radius=6,command= lambda : pilih_produk(lemari3,harga_lemari3),image=produk,fg_color='#e6e6e6',hover_color='#bfbfbf')
    button1.place(x=800, y=25)

    rtamu_page.config()
    rtamu_page.mainloop()
ruang_tamu()