import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
canvas1.pack()

label1 = tk.Label(root, text="Herramienta de conversión", bg="azure3")
label1.config(font=("helvetica", 16))
canvas1.create_window(150, 60, window=label1)


def getPNG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_PNG = tk.Button(text="Importe la imagen PNG",
                             command=getPNG, bg="royalblue", fg="white", font=("hervetica", 12, "bold"))
canvas1.create_window(150, 130, window=browseButton_PNG)


def convertToPNG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    im1.save(export_file_path)


saveAsButton_JPG = tk.Button(text="Convertir de PNG a JPG",
                             command=getPNG, bg="royalblue", fg="white", font=("hervetica", 12, "bold"))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()
