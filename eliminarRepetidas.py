import cv2
import numpy as np
import os
carpeta = input("Ingresa el nombre de la carpeta\n")
os.chdir(carpeta)
imagenes = os.listdir()
imagenes.sort()
n = len(imagenes)

def comparar(i1, i2):
    try:
        diferencia = cv2.subtract(i1, i2)
        if not np.any(diferencia):
            return True
        else:
            return False
    except cv2.error:
        return False
i = 0
j = 0
comparador = 0
borrar = []

for i in range(0, len(imagenes)):
    imagenUno = cv2.imread(imagenes[i])
    comparador = i+1
    print("Comparando ", imagenes[i])
    while comparador < len(imagenes):
        imagenDos = cv2.imread((imagenes[comparador]))
        if comparar(imagenUno, imagenDos) and imagenes[i] != imagenes[comparador]:
            print("Son iguales las imagenes ", imagenes[i], imagenes[comparador])
            imas = np.hstack((imagenUno, imagenDos))
            #cv2.imshow("Comparaciones", imas)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            borrar.append(imagenes[comparador])
        comparador += 1

print(os.listdir())
for archivo in borrar:
    print(archivo)
    os.remove(archivo)
