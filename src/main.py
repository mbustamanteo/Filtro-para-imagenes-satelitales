#
#
#    Proyecto para filtrar segun radiancia y reflectividad imagenes satelitales
#
#
import pprint
import Image,TiffImagePlugin
from tiff import cargar_config,filtrar_radiancia,filtrar_reflectancia


### CARGAR ARCHIVO DE METADATOS
configuracion = cargar_config()


### DEFINIR ARCHIVOS TIFF
archivosTIFF = (("b1","archivos/b1.tif"),
                ("b2","archivos/b2.tif"),
                ("b3","archivos/b3.tif"),
                ("b4","archivos/b4.tif"),
                ("b5","archivos/b5.tif"),
                ("b7","archivos/b7.tif"))

### FILTRAR Y GUARDAR ARCHIVOS
for tupla in archivosTIFF:
    config_archivo = configuracion[tupla[0]]
    nombre_archivo = tupla[1]
    
    
    imagen = Image.open(nombre_archivo,'r')
    lista = list(imagen.getdata())
    lista_reflectancia = list()
    lista_radiancia = list()
    
    # iterar sobre elementos
    for ND in lista:
        valor = filtrar_reflectancia(ND, config_archivo['LMAX'], config_archivo['LMIN'], config_archivo['QCALMAX'], config_archivo['QCALMIN'])
        lista_reflectancia.append(valor)
        
    imagen.putdata(lista_reflectancia)
    imagen.save("archivos/" + tupla[0] + "-reflectancia.tif")
    
    
    # iterar sobre elementos
    for REFLECTANCIA in lista_reflectancia:
        valor = filtrar_radiancia(REFLECTANCIA, config_archivo['SOLAR'], configuracion['ELEVACION_SOLAR'], configuracion['DIA_JULIANO'])
        lista_radiancia.append(valor)
        
    imagen.putdata(lista_radiancia)
    imagen.save("archivos/" + tupla[0] + "-radiancia.tif")

