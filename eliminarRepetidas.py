import cv2
import numpy as np
import os
carpeta = input("Ingresa el nombre de la carpeta\n")
os.chdir(carpeta)
imagenes = os.listdir()


def comparar(i1, i2):
    diferencia = cv2.subtract(i1, i2)
    if not np.any(diferencia):
        return True
    else:
        return False


for imagen in imagenes:
    imagenUno = cv2.imread(imagen, 1)
    for segundaImagen in imagenes:
        imagenDos = cv2.imread(imagen, 1)
        if comparar(imagenUno, imagenDos):
            imas = np.hstack((imagenDos, imagenDos))
            cv2.imshow("Posibles repetciocions",imas)
            print("Son repetidas segun")
            d = input("\n")

