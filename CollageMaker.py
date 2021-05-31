# SIRVE CON IMAGENES .JPG

from PIL import Image
import numpy as np

# Abrimos las imágenes pegando la dirección donde se encuentran en el ordenador.
imagen1 = Image.open("C:/Users/PC/Downloads/123.jpg")
imagen2 = Image.open("C:/Users/PC/Downloads/123.jpg")

# Array de las imágenes
imagen1_array = np.array(imagen1)
imagen2_array = np.array(imagen2)

# Collage
imagen = np.hstack([imagen1_array , imagen2_array])

# Crear imagen final

imagenFinal = Image.fromarray(imagen)

# Guardar imagen
imagenFinal.save("C:/Users/PC/Downloads/Collage.jpg")

print("La imagen ha sido guardada")
