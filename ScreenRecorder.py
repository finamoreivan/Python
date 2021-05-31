import pyautogui
import cv2
import numpy as np

resolucion = (1280, 720)

codec = cv2.VideoWriter_fourcc(*"XVID")

archivo = "Grabación.avi"
#Cambiar si ya existe el archivo para crear uno nuevo, si no sobreescribe.

fps = 60.0

salida = cv2.VideoWriter(archivo, codec, fps, resolucion)

cv2.namedWindow("Vivo", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Vivo", 480, 270)

while True:
    imagen = pyautogui.screenshot()
    frame = np.array(imagen)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    salida.write(frame)

    cv2.imshow("Vivo", frame)

    if cv2.waitKey(1) == ord("q"):
        break

salida.release()

cv2.destroyAllWindows()
