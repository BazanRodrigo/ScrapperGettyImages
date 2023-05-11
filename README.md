# Scrapper para gettyImages
Este código funciona en complemento de la extensión:
> Fatkun Batch Descargar imagen.  
  
La extensíon se puede descargar en la tienda de extensiones de chrome, para poder descargar las imagenes es necesario seguir estos pasos:  

1.- Instalar extensión _Fatkun Batch Descargar imagen_  
2.- Ejecutar el código **_Scrapper_**  
3.- Abrir los links que te indica el código  
4.- Una vez abiertos todos los links, ejecutar la extensión y seleccionar la opción _**`Download「All Tabs」`**_  
5.- Seleccionar la opción  **_`Export links`_**  
![img.png](img.png)  
6.- Copiar todos los links y pegarlos en el archivo **_url.txt_**  
7.- Ejecutar el archivo **_downloader.py_**

El script filtrador.py es para filtrar las imagenes funcionales y las no funcionales, si te sirve la imagen, selecciona la paloma de color verde, si no, selecciona la equis de color rojo; funciona igual con teclas hacia arriba y hacia abajo respectivamente.
Al final el script te devuelve una carpeta llamada Imagenes filtradas, las cuales están listas para proceder a etiquetar las imagenes usando LabelImg.py

Una vez hayas etiquetado las imagenes, puedes ejecutar el script  OrdenadorNumerador.py, para que todas las imagenes tengan una numeración cotinua sin perder las etiquetas generadas para entrenar YOLO


# Etiquetación de imagenes
https://github.com/heartexlabs/labelImg
1. Corre el código 
**pip install pyinstaller**
**conda install pyqt=5**
**conda install -c anaconda lxml**
**pyrcc5 -o libs/resources.py resources.qrc**
**python labelImg.py**

