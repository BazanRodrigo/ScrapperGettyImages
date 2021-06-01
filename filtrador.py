import pygame
import os
import shutil
from pygame.locals import *

img = 1
listaImg = []


def save(img):
    destino = 'ImagenesFiltradas' + str(img[4:])
    shutil.copy(img, destino)


def ordenador(listaArchivos, name):
    i = 0   
    for archivo in listaArchivos:
        if i < 10:
            os.rename(archivo, name + '000' + str(i) + '.jpg')
        if i >= 10 and i < 100:
            os.rename(archivo, name + '00' + str(i) + '.jpg')
        if i >= 100 and i < 1000:
            os.rename(archivo, name + '0' + str(i) + '.jpg')
        if i >= 1000 :
            os.rename(archivo, name + str(i) + '.jpg')
        i += 1

def main():
    name = input("Ingresa el nombre de la carpeta con las imagenes\n")
    os.chdir(name + '/')
    os.listdir().sort()
    listaImg = (os.listdir()).copy()
    os.chdir('../')
    try:
        os.mkdir('ImagenesFiltradas')
    except FileExistsError:
        print("\n")
    i = 0
    for imagen in listaImg:
        listaImg[i] = name + '/' + str(listaImg[i])
        i += 1
    wp = pygame.image.load('DataProgram/wallpaperPrincipal.jpg')
    correctimg = pygame.image.load('Icons/correct.png')
    incorrectimg = pygame.image.load('Icons/incorrect.png')
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode([1000, 720])
    window.blit(wp, (0, 0))
    window.blit(correctimg, (800, 100))
    window.blit(incorrectimg, (800, 250))
    pygame.display.flip()
    window.blit(pygame.image.load(listaImg[0]), (50, 50))
    pygame.display.flip()
    running = True
    listaImg.sort()
    imagen = 0
    i = 0
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 800 and x < 928 and y > 100 and y < 225:
                    save(listaImg[i])
                    i += 1
                    print("Se guardo " + str(listaImg[i]))
                if x > 800 and x < 928 and y > 250 and y < 375:
                    print("No se guardo " + str(listaImg[i]))
                    i += 1
                window.blit(wp, (0, 0))
                window.blit(correctimg, (800, 100))
                window.blit(incorrectimg, (800, 250))
                try:
                    window.blit(pygame.image.load(listaImg[i]), (50, 50))
                except:
                    imagen += 1
                    window.blit(pygame.image.load(listaImg[i]), (50, 50))
                pygame.display.flip()
                if i == len(listaImg):
                    running = False
    os.chdir('ImagenesFiltradas/')
    ordenador(os.listdir(), name)


if __name__ == '__main__':
    main()
