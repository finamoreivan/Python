import emoji

# importar tkinter
from tkinter import *

# importar YouTube module
from pytube import YouTube

# iniciar tkinter
root = Tk()

# Geometría de la GUI
root.geometry("400x350")

# Título de la GUI
root.title("Descarar video de Youtube")

# Definir la función para la descarga
def download():
    # usando try y except para ejecutar el programa sin errores
    try:
        myVar.set("Descargando...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video descargado correctamente en la carpeta")
    except Exception as e:
        myVar.set("Error")
        root.update()
        link.set("Ingrese el link correctamente")

# espacios e imagen
Label(root, text="").pack()
canvas = Canvas(root, width=300, height=126)
canvas.pack()
img = PhotoImage(file="YT Logo.png")
canvas.create_image(0,0, anchor=NW, image=img)

# crear el widget Laber para dar la bienvenida al usuario
Label(root, text="Bienvenido a la aplicacion\npara descargar videos de Youtube", font="Consolas 15 bold").pack()
Label(root, text="").pack()
Label(root, text="Ingrese el link abajo", font="Helvetica 11 bold").pack()
Label(root, text=emoji.emojize(":backhand_index_pointing_down::backhand_index_pointing_down::backhand_index_pointing_down:")).pack()
# declarando variable de tipo StringVar
myVar = StringVar()

# declarando variable de tipo StringVar
link = StringVar()

# Widget Entry para obtener el enlace
Entry(root, textvariable=link, width=60).pack(pady=10)

# Crear y llamar a la función download para descargar el video
Button(root, text="Descargar video", command=download).pack()

# Ejecutando el mainloop
root.mainloop()