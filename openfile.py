import tkinter as tk
import datetime
from os import path as os_path
from PIL import Image,ImageFile
from tkinter import filedialog
from tkinter.ttk import *
from PyPDF2 import PdfFileReader, PdfFileWriter



root = tk.Tk()

root.call('wm', 'attributes', '.', '-topmost', True)
today = datetime.datetime.today()
namefile= today.strftime("%Y-%m-%d-%H%M%S")+str('.pdf')
def open_file(): 
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


def merge_pdfs():
    pdf_writer = PdfFileWriter()
    files = filedialog.askopenfilename(multiple=True) 
    var = root.tk.splitlist(files)
    


    filePaths = []
    for path in var:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(namefile, 'wb') as out:
        pdf_writer.write(out)
    

PATH = os_path.abspath(os_path.split(__file__)[0])
print(PATH)

root.title("rock")
root.geometry("1180x850")
root.iconbitmap("logo.ico")
root.config(background='#85B77F')
#frame
frame =tk.Frame(root,bg='white')
#ajouter un label , bg='#85B77F', fg='white'
label_title=Label(root,text="Bienvenue sur mon application",font=("Courrier",40))
label_title.pack()
button1 =tk.Button(root,text="votre fichier image en pdf",command=open_file)
button2 =tk.Button(root,text="votre fichier pfd en pdf",command=merge_pdfs)
button1.pack()
button2.pack()
root.mainloop()