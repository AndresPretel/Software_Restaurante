from tkinter import Tk, Label,Entry,Button,Text,Frame
from tkinter.constants import END, INSERT
from PIL import  Image,ImageTk
import pywhatkit
from datetime import datetime


class Programa_restaurante():             # Creacion y ajustes de la ventana padre
    def __init__(self):
        self.root= Tk()                                  
        self.root.attributes('-fullscreen', True)
        self.state = False
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.create_widgets()
        self.root.mainloop()
 
    def toggle_fullscreen(self, event=None):     #Funcion para abrir en full screen con 'F11'
        self.state = not self.state  
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):      #Funcion para minimizar con 'ESC'
        self.state = False
        self.root.attributes("-fullscreen", False)
        self.root.minsize(800,600)
        return "break"

    def agregar_datos(self):            #Funcion para agregar datos  --> Boton = Agregar registro
        data1 = self.txt_cliente.get()
        data2 = self.txt_tel.get()
        data3 = self.mess_cliente.get(1.0,"end")

        self.nombre_field.insert(0,data1)
        self.tel_field.insert(0,data2)
        self.mess_field.insert(INSERT,data3)

        self.nombre_field.configure(state="disabled")
        self.tel_field.configure(state="disabled")
        self.mess_field.configure(state="disabled")
        self.txt_cliente.delete(0,"end")
        self.txt_tel.delete(0,"end")

    def borrar_datos(self):                             #Funcion para borrar datos --> Boton = Limpiar Registro
        self.nombre_field.configure(state="normal")
        self.tel_field.configure(state="normal")
        self.mess_field.configure(state="normal")
        self.nombre_field.delete(0,"end")
        self.tel_field.delete(0,"end")
        self.mess_field.delete(1.0,END)
    
    def enviar_mensaje(self):            #Funcion para enviar mensaje a whatsapp
        ext = "+57"
        now = datetime.now()
        hora = now.hour
        minuto = now.minute + 1
        numero, mensaje = self.tel_field.get(), self.mess_field.get(1.0, END)
    
        try:
            pywhatkit.sendwhatmsg(ext + numero, mensaje,hora,minuto,8,True,)
            print("Mensaje Enviado")
        except:
            print("Ocurrio Un Error")
   

    def create_widgets(self):  #Creacion de los elementos de la ventana padre

        self.nombre_cliente = Label(text="NOMBRE CLIENTE", bg="azure2",font=("Tahoma",15))
        self.txt_cliente = Entry(bg="white",font=25,justify="center")
        self.tel_cliente = Label(text="NUMERO CLIENTE", bg="azure2",font=("Tahoma",15))
        self.txt_tel = Entry(bg="white",font=25,justify="center")      
        self.mess_text = Label(text="MENSAJE", bg="azure2",font=("Tahoma",15)) 
        self.mess_cliente = Text(font=18)
        self.mess_cliente.insert(0.1,"Su pedido esta listo. Por favor, Dirigete a vaporetto para reclamarlo")
        self.send_txt_mess = Button(text="Agregar Registro",borderwidth=3, relief= "raised",fg="red",font=("Tahoma",12),command=self.agregar_datos)
        self.clear_data = Button(text="Limpiar Registro",borderwidth=3, relief= "raised",fg="red",font=("Tahoma",12),command=self.borrar_datos)
        
        #Posiciones
        self.nombre_cliente.place(relx=0.070,rely=0.1,relwidth=0.30,relheight=0.038)
        self.tel_cliente.place(relx=0.070,rely=0.23,relwidth=0.30,relheight=0.038)
        self.txt_tel.place(relx=0.070,rely=0.28,relwidth=0.30,relheight=0.042)
        self.mess_text.place(relx=0.070,rely=0.34,relwidth=0.30,relheight=0.038)
        self.mess_cliente.place(relx=0.070,rely=0.40,relwidth=0.30,relheight=0.090)
        self.send_txt_mess.place(relx=0.11,rely=0.50,relwidth=0.20,relheight=0.040)
        self.clear_data.place(relx=0.58,rely=0.50,relwidth=0.2,relheight=0.040)


        #Creacion del Frame 1 y sus elementos
        self.frame1 = Frame(self.root,highlightthickness=1,highlightbackground="lightblue1",borderwidth=10,relief="groove",bg="light grey")
        self.check_nombre = Label(self.frame1,text="NOMBRE",font=("Tahoma", 11,"bold"),bg="light grey")
        self.nombre_field = Entry(self.frame1, bg="white", justify= "center",font=("Tahoma",12))
        self.check_tel = Label(self.frame1,text="NUMERO",font=("Tahoma",11,"bold"),bg="light grey")
        self.tel_field = Entry(self.frame1, bg="white", justify= "center",font=("Tahoma",12))
        self.check_mess = Label(self.frame1,text="MENSAJE",font=("Tahoma",11, "bold"),bg="light grey")
        self.mess_field = Text(self.frame1,font=18)
        self.enviar = Button(self.frame1,text="ENVIAR",borderwidth=3, relief= "ridge",fg="red",font=("Arial Black",10),command=self.enviar_mensaje)
        self.enviar.place(relx=0.34,rely=0.85,relwidth=0.3,relheight=0.12)

        #Posiciones
        self.frame1.place(relx=0.49,rely=0.10,relwidth=0.4,relheight=0.39)
        self.check_nombre.place(relx=0.01,rely=0.050,relwidth=0.45,relheight=0.1)
        self.nombre_field.place(relx=0.030,rely=0.2,relwidth=0.4,relheight=0.1)
        self.check_tel.place(relx=0.51,rely=0.050,relwidth=0.45,relheight=0.1)
        self.tel_field.place(relx=0.53,rely=0.2,relwidth=0.4,relheight=0.1)
        self.check_mess.place(relx=0.25,rely=0.38,relwidth=0.45,relheight=0.1)
        self.mess_field.place(relx=0.030,rely=0.50,relwidth=0.90,relheight=0.3)
        self.enviar.place(relx=0.34,rely=0.85,relwidth=0.3,relheight=0.12)

        self.frame2 = Frame(self.root,highlightthickness=1,highlightbackground="lightblue1",borderwidth=10,relief="groove",bg="light grey")
        self.frame2.place(relx=0.050,rely=0.67,relwidth=0.91,relheight=0.25)

       # Imagenes
        img1 = Image.open("images/logowa.png")
        img1 = img1.resize((45,45), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img1)

        img2 = Image.open("images/person.png")
        img2 = img2.resize((45,45), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)

        img3 = Image.open("images/phone.png")
        img3 = img3.resize((45,45), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)

        img4 = Image.open("images/mail.png")
        img4 = img4.resize((55,55), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(img4)
        
        #Ubicaciones
        self.pic1 = Label(self.root, image = self.img1)
        self.pic1.place(relx=0.38,rely=0.40)

        self.pic2 =Label(self.root, image = self.img2)
        self.pic2.place(relx=0.38,rely=0.14)

        self.pic3 = Label(self.root, image = self.img3)
        self.pic3.place(relx=0.38,rely=0.27)

        self.pic4 = Label(self.frame1, image = self.img4,bg="light grey")
        self.pic4.place(relx=0.75,rely=0.81,relwidth=0.2,relheight=0.19)


if __name__ == "__main__":
    app = Programa_restaurante()