'''
Este código sirve para descargar imagenes de gettyImages en conjunto de la extenxión
'''

#Ingresamos la palabra a buscar para generar los links de imagenes a descargar
searching = input("Ingresa la palabra a buscar en getty Images:\n")
cantidad = int(input("Ingresa la cantidad de páginas a scrappear (se recomienda 10)\n"))

for i in range (1,cantidad):
    print('https://www.gettyimages.com.mx/fotos/'+str(searching)+'?page='+str(i)+'&phrase='+str(searching)+'&sort=mostpopular')

