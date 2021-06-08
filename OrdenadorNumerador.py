import os


def abrirCarpeta():
    abierto = False
    carpeta = input("Ingresa el nombre de la carpeta para ordenar los archivos\n")
    while(not abierto):
        try:
            os.chdir(carpeta + '/')
            abierto = True
        except FileNotFoundError:
            print("No se encuentra la carpeta\nIngresa el nombre de la carpeta con las imagenes\n")
            carpeta = input()


def numerador(i):
    num = ''
    if i < 10:
        num= ('000' + str(i))
    if i >= 10 and i < 100:
        num= ('00' + str(i))
    if i >= 100 and i < 1000:
        num= ('0' + str(i))
    if i >= 1000 :
        num= (str(i))
    return num


def cargandoImgTxt():
    archivos = os.listdir()
    archivos.sort()
    imagenes = []
    textos = []
    #No olvides revisar que solo esten las imagenes y sus etiquetas
    for archivo in archivos:
        if archivo[-3:] == 'jpg':
            imagenes.append(archivo)
        if archivo[-3:] == 'txt':
            textos.append(archivo)
    for i in range(0,len(imagenes)):
        nombreImgCorrecto = (imagenes[i])[:-8] + str(numerador(i)) + '.jpg'
        nombreTxtCorrecto = (textos[i])[:-8] + str(numerador(i)) + '.txt'
        os.rename(imagenes[i], nombreImgCorrecto)
        os.rename(textos[i], nombreTxtCorrecto)
        print(imagenes[i], textos[i],'renombrando ->', nombreImgCorrecto, nombreTxtCorrecto )



abrirCarpeta()
cargandoImgTxt()
