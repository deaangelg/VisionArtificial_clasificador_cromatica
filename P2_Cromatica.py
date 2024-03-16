# -*- coding: utf-8 -*-
"""
Este script procesa una imagen de bacterias para realizar dos tareas:
1. Convertir la imagen a una representación cromática.
2. Clasificar los píxeles de la imagen según ciertos criterios (convertir a blanco y negro la imagen)

Vision artificial Marzo 2024 
Primer parcial Practica II 

@author: Dea Angel
"""

import cv2
import numpy as np

# Se carga la imagen de bacterias
imagen1 = cv2.imread("bacterias.jpg")

# Se crean dos imágenes adicionales modificando el brillo de la imagen original
imagen2 = imagen1 * 0.7
imagen3 = imagen1 * 0.3

# Función para convertir la imagen a una representación cromática
def cromatico(imagen1):
    m, n, c = imagen1.shape
    imagenc = imagen1.copy().astype(np.float32)
    imagen1 = imagen1.astype(np.float32)
    for x in range(m):
        for y in range(n):
            divisor = imagen1[x, y, 0] + imagen1[x, y, 1] + imagen1[x, y, 2]
            if divisor != 0:
                imagenc[x, y, 0] = imagen1[x, y, 0] / divisor
                imagenc[x, y, 1] = imagen1[x, y, 1] / divisor
                imagenc[x, y, 2] = imagen1[x, y, 2] / divisor
            else:
                imagenc[x, y] = [0, 0, 0]  
    # Normalización de la imagen cromática
    result = cv2.normalize(imagenc, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite("imagen_cromatica.jpg", result)
    return result

# Se aplican las funciones a las imágenes originales y modificadas
imagenc1 = cromatico(imagen1)
imagenc2 = cromatico(imagen2)
imagenc3 = cromatico(imagen3)

# Función para clasificar los píxeles de la imagen según ciertos criterios
def clasificador(imagen1):
    m, n, c = imagen1.shape
    imagenb = np.zeros((m, n))
    for x in range(m):
        for y in range(n):
            # Se define una condición para la clasificación de los píxeles
            #cambiar los valores BGR en el caso de otra imagen. 
            if (46 < imagen1[x, y, 0] < 134) and (106 < imagen1[x, y, 1] < 253) and (65 < imagen1[x, y, 2] < 140):
                imagenb[x, y] = 255
    # Se guarda la imagen clasificada
    cv2.imwrite("clasificada.jpg", imagenb)
    return imagenb

# Se aplican las funciones a las imágenes originales y modificadas (clasificador)
imagend1 = clasificador(imagenc1)
imagend2 = clasificador(imagenc2)
imagend3 = clasificador(imagenc3)

# Se concatenan las imágenes para la visualización
im_final1 = np.hstack((imagen1, imagen2, imagen3))
result1 = cv2.normalize(im_final1, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
Originales = cv2.resize(result1, (600, 200))
cv2.imwrite("CAMBIO DE BRILLO ORIGINAL.jpg", Originales)

im_final2 = np.hstack((imagenc1, imagenc2, imagenc3))
result2 = cv2.normalize(im_final2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
Cromatica = cv2.resize(result2, (600, 200))
cv2.imwrite("CROMATICAS.jpg", Cromatica)

im_final3 = np.hstack((imagend1, imagend2, imagend3))
result3 = cv2.normalize(im_final3, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
Clasificada = cv2.resize(result3, (600, 200))
cv2.imwrite("Clasificada.jpg", Clasificada)

# Se muestran las imágenes en ventanas separadas
cv2.imshow("imagen original", Originales)
cv2.imshow("imagen cromatica", Cromatica)
cv2.imshow("imagen clasificada", Clasificada)
cv2.waitKey(0)
cv2.destroyAllWindows()