import pygame
import os
import shutil
from pygame.locals import *
img = 1
listaImg = []
def save(img):
    destino = 'ImagenesFiltradas' + str(img[4:])
    shutil.copy(img, destino)

def main():
   name = input("Ingresa el nombre de la carpeta con las imagenes\n")
   os.chdir(name + '/')
   listaImg = os.listdir().copy()
   os.chdir('../')
   os.mkdir('ImagenesFiltradas')
   i = 0
   for imagen in listaImg:
       listaImg[i] = name + '/' + str(listaImg[i])
       i += 1
   wp = pygame.image.load('DataProgram/wallpaperPrincipal.jpg')
   correctimg = pygame.image.load('Icons/correct.png')
   incorrectimg = pygame.image.load('Icons/incorrect.png')
   pygame.init()
   pygame.display.init()
   window = pygame.display.set_mode()
   window.blit(wp, (0, 0))
   window.blit(correctimg, (100, 800))
   window.blit(incorrectimg, (400, 800))
   pygame.display.flip()
   print(imagen)
   window.blit(pygame.image.load(listaImg[0]), (200, 200))
   pygame.display.flip()
   running = True
   while running:
       for imagen in range(1, len(listaImg)):
           # Did the user click the window close button?
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               if event.type == pygame.MOUSEBUTTONDOWN:
                   x = pygame.mouse.get_pos()[0]
                   y = pygame.mouse.get_pos()[1]
                   if x > 100 and x < 225 and y > 800 and y < 928:
                       save(listaImg[imagen])
                       window.blit(wp, (0, 0))

                   if x > 400 and x < 525 and y > 800 and y < 928:
                       print("No se guardo " + str(listaImg[imagen]))
                       window.blit(wp, (0, 0))

                   window.blit(pygame.image.load(listaImg[imagen]), (200, 200))
                   pygame.display.flip()



if __name__  == '__main__':
    main()