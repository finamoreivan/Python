from tkinter import *
from speedtest import Speedtest

def speed():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round((download/1000000), 2)
    upload_speed = round((upload/1000000), 2)
    down_label.config(text= "Velocidad de descarga: " + str(download_speed) + " Mbps")
    up_label.config(text= "Velocidad de subida: " + str(upload_speed) + " Mbps")


root = Tk()
root.title("Test de velocidad")
root.geometry('300x200')
Label(root, text="").pack()
Label(root, text="").pack()
button = Button(root, text="Iniciar test", bg="gray", width=30, command=speed)
button.pack()
Label(root, text="").pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()
