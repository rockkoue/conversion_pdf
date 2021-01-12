from tkinter import *
import tkinter as tk
import datetime
from os import path as os_path
from PIL import Image,ImageFile
from tkinter import filedialog



class MyApp:

    def __init__(self):
        self.window = Tk()
        self.root = tk.Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("logo.ico")
        self.window.config(background='#41B77F')
        
        today = datetime.datetime.today()
        namefile= today.strftime("%Y-%m-%d-%H%M%S")+str('.pdf')
        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)



    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_pdfpdf_button()
        self.create_imagepdf_button()


    def open_file(self): 
        files = filedialog.askopenfilename(multiple=True) 
        var = root.tk.splitlist(files)
        filePaths = []
        for f in var:
            filePaths.append(f)
        filePaths
        Table=[]
        for i in range(len( filePaths)):
            #.resize((1000,1050))
            Table.append(Image.open(filePaths[i]))
        Table[0].save(namefile,'PDF',resolution=100.0,save_all=1,append_images=Table[1:])

    def create_title(self):
        label_title = Label(self.frame, text="Apllication Pdf", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Petite aplication de generation de PDF", font=("Courrier", 25), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def create_pdfpdf_button(self):
        yt_button = Button(self.frame, text="Image Pdf", font=("Courrier", 25), bg='white',command=self.open_file)
        yt_button.pack(pady=25,fill=X )
    def create_imagepdf_button(self):
        yt_button = Button(self.frame, text="Pdf Pdf", font=("Courrier", 25), bg='white')
        yt_button.pack(pady=25,fill=X)


# afficher
app = MyApp()
app.window.mainloop()