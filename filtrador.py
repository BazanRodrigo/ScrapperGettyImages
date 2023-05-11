import os
import shutil
import pygame
import glob

def save(carpeta,img):
    """Guarda la imagen en una carpeta llamada ImagenesFiltradas."""    
    destino = carpeta+'/'+'ImagenesFiltradas/' + os.path.basename(img)
    shutil.copy(img, destino)

def ordenador(lista_archivos, name):
    """Ordena los archivos en una carpeta."""
    os.chdir('ImagenesFiltradas/')
    i = 0
    lista_archivos.sort()
    for archivo in lista_archivos:
        nombre, extension = os.path.splitext(archivo)
        nombre = name + f'{i:04d}'
        os.rename(archivo, nombre + extension)
        i += 1

def lastImage():
    # Obtener la lista de imágenes con cualquier extensión en la carpeta ImagenesFiltradas    
    imagenes = glob.glob(os.path.join("ImagenesFiltradas", "*.*"))
    if not imagenes:        
        return -1
    # Ordenar la lista según el número que se encuentra antes de la extensión
    imagenes_ordenadas = sorted(imagenes, key=lambda x: int(os.path.splitext(x)[0][-4:]))
    # Obtener la imagen con la terminación más grande
    imagen_mas_grande = imagenes_ordenadas[-1]
    # Cargar la imagen y devolverla
    return imagen_mas_grande[18:]


def main():
    """Función principal que ejecuta el programa."""
    # Se pide al usuario el nombre de la carpeta con las imágenes.
    while True:
        nombre_carpeta = input("Ingresa el nombre de la carpeta con las imágenes: ")
        if os.path.isdir(nombre_carpeta):
            break
        print("No se encuentra la carpeta.")
    os.chdir(nombre_carpeta)
    if not os.path.isdir('ImagenesFiltradas'):
        os.mkdir('ImagenesFiltradas')
    # Se cargan las imágenes y se muestran en la pantalla.
    lista_img = [os.path.join(nombre_carpeta, f) for f in os.listdir() if f.endswith(('.jpg', '.jpeg', '.png'))]
    lista_img.sort()
    li = lastImage()
    print(li,'*'*500)
    print(lista_img)
    if li != -1:
        imgg = nombre_carpeta + '\\' + li        
        lista_img = lista_img[lista_img.index(imgg):]
    pygame.init()
    pygame.display.set_caption('Filtrar imágenes')
    pantalla = pygame.display.set_mode([1000, 720])
    os.chdir('../')
    wp = pygame.image.load('wallpaperPrincipal.jpg')
    correct_img = pygame.image.load('Icons/correct.png')
    incorrect_img = pygame.image.load('Icons/incorrect.png')
    i = 0
    while i < len(lista_img):
        pantalla.blit(wp, (0, 0))
        pantalla.blit(correct_img, (800, 100))
        pantalla.blit(incorrect_img, (800, 250))
        imagen = pygame.image.load(lista_img[i])
        pantalla.blit(imagen, (50, 50))
        pygame.display.flip()

        # Se esperan eventos del usuario.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    save(nombre_carpeta ,lista_img[i])
                    print(f"Se guardó {lista_img[i]}")
                elif event.key == pygame.K_DOWN:
                    print(f"No se guardó {lista_img[i]}")
                i += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 800 < x < 928 and 100 < y < 225:
                    save(nombre_carpeta ,lista_img[i])
                    print(f"Se guardó {lista_img[i]}")
                    i += 1
                elif 800 < x < 928 and 250 < y < 375:
                    print(f"No se guardó {lista_img[i]}")
                    i += 1

    # Se ordenan las imágenes guardadas.
    os.chdir('..')
    os.makedirs('ImagenesFiltradas', exist_ok=True)
    ordenador(os.listdir(nombre_carpeta), nombre_carpeta)

if __name__ == '__main__':
    main()
