from tkinter import Tk, Label, Entry, Button, Toplevel, messagebox, StringVar, Spinbox
from PIL import Image, ImageTk
import datetime

class UserService:          # Memakai Modul 5 Class UserService berfungsi untuk membuat Login Page
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "azzam": {
                "username": "azzam",
                "password": "123"
            }
        }

    def checkCredentials(self):
        if self.username in self.data:
            user_data = self.data[self.username]
            if self.password == user_data['password']:
                return user_data
        return False

    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\Selamat Datang di Coklat Tepi Sawah ")
            print("Logged in as user username: ", get_data['username'])
            return True
        else:
            print("\nInvalid Login!\n")
            return False
    
app = Tk()
app.geometry('450x300')
app.title('Program Kasir Angkringan Modern Coklat Tepi Sawah By Azzam Syaiful Islam')
app.resizable(False, False)  # Mencegah perubahan ukuran window

def set_background_image(frame, image_path):
    
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    
    
    background_label = Label(frame, image=photo)
    background_label.image = photo  # Menyimpan referensi ke photo untuk mencegah garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

image_path = "inipo.jpeg"
set_background_image(app, image_path)

# membuat label dan text fields untuk username dan password
username_label = Label(app, text="username:")
username_label.place(x=100, y=100)

username_entry = Entry(app)
username_entry.place(x=190, y=100)

password_label = Label(app, text="Password:")
password_label.place(x=100, y=130)

password_entry = Entry(app, show="*")
password_entry.place(x=190, y=130)

def window_Kasir():
    username = username_entry.get()            # Memakai Modul 6 Getter OOP yang mengambil nilai dari objek StringVar
    password = password_entry.get()
    user = UserService(username, password)
    if user.login():

        # variabel Mencakup Modul 1 Variabel Tipe data Array
        BaksoAci = StringVar()
        Cireng = StringVar()
        Kentang = StringVar()
        Steakayam = StringVar()
        ChickenToast = StringVar()
        Coklatroti = StringVar()
        Kopisusugulaaren = StringVar()
        Tehleci = StringVar()
        UangUser = StringVar()
        teksuang = StringVar ()
        total = 0

        # beberapa function seperti di bawah ini, Mencakup Modul 4 Function and Method
        def totalbeli():
            global total
            hSteakayam = int(Steakayam.get()) * 16000
            hCireng = int(Cireng.get()) * 8000
            hKentang = int(Kentang.get()) * 10000
            hChickenToast = int(ChickenToast.get()) * 15000
            hBaksoAci = int(BaksoAci.get()) *10000
            hCoklatroti = int(Coklatroti.get()) * 10000
            hKopi_Susugula_Aren = int(Kopisusugulaaren.get()) * 10000
            hTeh_Leci = int(Tehleci.get()) * 6000
            total = hSteakayam + hCireng + hKentang + hChickenToast + hBaksoAci + hCoklatroti + hKopi_Susugula_Aren + hTeh_Leci
            UangUser.set(str(total)) 

        def kembalian():
            global total
            uang_str = teksuang.get()
            
            if uang_str:
                try:
                    uang = int(uang_str)
                    kembalian = uang - total
                    details = {
                        "Steak Ayam": Steakayam.get(),
                        "Cireng": Cireng.get(),
                        "Kentang": Kentang.get(),
                        "Chicken Toast": ChickenToast.get(),
                        "Bakso Aci": BaksoAci.get(),
                        "Coklat Roti": Coklatroti.get(),
                        "Kopi Susu Gula Aren": Kopisusugulaaren.get(),
                        "Teh Leci": Tehleci.get()
                    }
                    window_Struk(uang, total, details)
                except ValueError:
                    messagebox.showerror(message='Masukkan jumlah uang yang valid')
            else:
                messagebox.showerror(message='Masukkan jumlah uang yang valid')

        def clear():
                Steakayam.set('0')
                Cireng.set('0')
                Kentang.set('0')
                ChickenToast.set('0')
                BaksoAci.set('0')
                Coklatroti.set('0')
                Kopisusugulaaren.set('0')
                Tehleci.set('0')

        def set_background_image(frame, image_path):
 
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            
            # Mengatur background dengan label
            background_label = Label(frame, image=photo)
            background_label.photo = photo  
            background_label.place(x=0, y=0, relwidth=1, relheight=1)


        app.geometry('910x600') 
        app.resizable(False, False)  # agar tidak ada perubahan ukuran window secara manual

        image_path = "inipo.jpeg"
        set_background_image(app, image_path)

        Label(app, text="Program Kasir Angkringan Modern Coklat Tepi Sawah:", font='Times 16 bold').place(x=200,y=30)
        
        # membuat label nama menu
        Label(app, text="1. Steakayam:", font='Times 12 bold').place(x=100,y=100)
        Label(app, text="2. Cireng:", font='Times 12 bold').place(x=100,y=140)
        Label(app, text="3. Kentang:", font='Times 12 bold').place(x=100,y=180)
        Label(app, text="4. Chicken Toast:", font='Times 12 bold').place(x=100,y=220)
        Label(app, text="5. Bakso Aci:", font='Times 12 bold').place(x=100,y=260)
        Label(app, text="6. Coklat Roti:", font='Times 12 bold').place(x=100,y=300)
        Label(app, text="7. Kopi Susu Gula Aren:", font='Times 12 bold').place(x=100,y=340)
        Label(app, text="8. Teh Leci:", font='Times 12 bold').place(x=100,y=380)

        Label(app, text='Rp. 16000', font='Times 12 bold').place(x=350,y=100)
        Label(app, text='Rp. 8000', font='Times 12 bold').place(x=350,y=140)
        Label(app, text='Rp. 10000', font='Times 12 bold').place(x=350,y=180)
        Label(app, text='Rp. 15000', font='Times 12 bold').place(x=350,y=220)
        Label(app, text='Rp. 10000', font='Times 12 bold').place(x=350,y=260)
        Label(app, text='Rp. 10000', font='Times 12 bold').place(x=350,y=300)
        Label(app, text='Rp. 10000', font='Times 12 bold').place(x=350,y=340)
        Label(app, text='Rp. 6000', font='Times 12 bold').place(x=350,y=380)

        # membuat spinbox agar Customer dapat memilih lebih dari 1
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Steakayam, command=totalbeli).place(x=550,y=100)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Cireng, command=totalbeli).place(x=550,y=140)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Kentang, command=totalbeli).place(x=550,y=180)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=ChickenToast, command=totalbeli).place(x=550,y=220)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=BaksoAci, command=totalbeli).place(x=550,y=260)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Coklatroti, command=totalbeli).place(x=550,y=300)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Kopisusugulaaren, command=totalbeli).place(x=550,y=340)
        Spinbox(app, from_=0, to=100, width=4, font='Times 10', textvariable=Tehleci, command=totalbeli).place(x=550,y=380)

        Label(app, text='Masukan uang anda', font='Times 12 ').place(x=100,y=440)

        Entry(app, textvariable=teksuang).place(x=100,y=460)

        Label(app, text='Rp. ', font='Times 12 bold').place(x=350,y=460)
        Label(app, textvariable=UangUser, font='Times 12 bold').place(x=380,y=460)

        Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=560)
        Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=560)

        Label(app, text='Created by Azzam Syaful Islam', font='Times 10 ').place(x=700,y=580)

        app.mainloop() 

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def window_Struk(uang, total, details):
    kembalian = uang - total

    window_Struk = Toplevel()
    window_Struk.title("Struk Pembelian")
    window_Struk.geometry("600x400")
    window_Struk.resizable(False, False)  # Mencegah perubahan ukuran window Struk

    # Membuat teks struk dengan detail pembelian
    struk_text = (
        "-------------------------------------------------------------------\n"
        "                      COKLAT TEPI SAWAH              \n"
        " kapling weru, Kec. Bandongan, Kabupaten Magelang, Jawa Tengah\n"
        "-------------------------------------------------------------------\n"
        f"{get_current_time()}\n"       
        "-------------------------------------------------------------------\n"
        "Pembelian:\n"
    )
    
    # Menambahkan detail makanan dan minuman yang dibeli oleh Customer
    for item, qty in details.items():
        if int(qty) > 0:
            struk_text += f"{item}: {qty} pcs\n"
    
    struk_text += (
        "-------------------------------------------------------------------\n"
        f"Total : Rp {total}\n"
        f"Tunai : Rp {uang}\n"
        f"Kembalian : Rp {kembalian}\n"
        "Terimakasih Telah Berkunjung di Coklat Tepi Sawah,\n"
        "Kunjungan anda sangat berarti bagi kami :D\n"
        "-------------------------------------------------------------------\n"
    )

    label = Label(window_Struk, text=struk_text, justify='left', font=("Times", 12))
    label.pack(padx=0, pady=0) 

    window_Struk.mainloop()

login_button = Button(app, text="Login", command=window_Kasir)  
login_button.place(x=190, y=170)

exit_button = Button(app, text="Exit", command=app.destroy)
exit_button.place(x=250, y=170)

app.mainloop()
