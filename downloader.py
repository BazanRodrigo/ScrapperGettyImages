import requests
import os

def download_img(img_url, img_name):
    req = requests.get(img_url)
    req.headers['User-Agent']= 'Mozilla/5.0'
    response = req.content
    with open(img_name, "wb") as f:
       f.write(response)
    print('Descargando '+img_name)

urls = open('url.txt', 'r')
i = 0
listaLinks = []
for link in urls:
    listaLinks.append(link[10:-4])


name = input("Ingresa el nombre de las imagenes\n")
try:
    os.mkdir(name)
    os.chdir(name + '/')
except FileExistsError:
    os.chdir(name+'/')
print('descargando imagenes en '+os.getcwd())

for link in listaLinks:
    if i < 10:
        try:
            download_img(link, name+'000'+str(i)+'.jpg')
        except requests.exceptions.SSLError or requests.exceptions.ConnectionError:
            print("Error de conexión")
    if i >= 10 and i < 100:
        try:
            download_img(link, name + '00' + str(i)+'.jpg')
        except requests.exceptions.SSLError or requests.exceptions.ConnectionError:
            print("Error de conexión")
    if i >= 100 and i < 1000:
        try:
            download_img(link, name + '0' + str(i)+'.jpg')
        except requests.exceptions.SSLError or requests.exceptions.ConnectionError:
            print("Error de conexión")
    if i >= 1000:
        try:
            download_img(link, name + str(i) + '.jpg')
        except requests.exceptions.SSLError or requests.exceptions.ConnectionError:
            print("Error de conexión")
    i += 1