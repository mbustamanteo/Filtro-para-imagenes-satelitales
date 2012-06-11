'''
Created on 10-06-2012

@author: micho
'''

import pprint
import Image,TiffImagePlugin
import math

#
#    Dado el valor de un pixel, devolver el valor de reflectancia espectral
#    NIVEL DIGITAL = valor del pixel
#    LMAX, LMIN, QMAX, QMIN = constantes definidas por el fabricante
#
def filtrar_reflectancia(NIVEL_DIGITAL,LMAX, LMIN, QMAX, QMIN):   
    #sensor ETM+/Landsat
    divi = ((LMAX - LMIN) / (QMAX - QMIN))
    multi = (NIVEL_DIGITAL - QMIN)
    resultado = divi*multi + LMIN
    
    return resultado
    

#
#    Dado el valor de un pixel, devolver el valor de radiancia
#

def filtrar_radiancia(REFLECTANCIA,IRRADIANCIA_SOLAR,ELEVACION_SOLAR,DIA_JULIANO):

    DISTANCIA = 1- 0.01673 * ( math.cos(0.9856 * (DIA_JULIANO - 4)))
    
    numerador = math.pi * REFLECTANCIA * (DISTANCIA*DISTANCIA)
    denominador = IRRADIANCIA_SOLAR * math.cos(90 - ELEVACION_SOLAR)    # angulo cenital es el opuesto a la elevacion solar
    resultado = numerador / denominador
    
    return resultado
    
#
#    Devuelve un diccionario con los metadatos
#
def cargar_config():
    configuracion = {
        'b1' : { 'LMAX' : 191.600, 'LMIN' : -6.200, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 1997.0 },
        'b2' : { 'LMAX' : 196.500, 'LMIN' : -6.400, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 1812.0 },
        'b3' : { 'LMAX' : 152.900, 'LMIN' : -5.000, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 1533.0 },
        'b4' : { 'LMAX' : 241.100, 'LMIN' : -5.100, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 1039.0 },
        'b5' : { 'LMAX' : 31.060,  'LMIN' : -1.000, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 230.8 },
        'b7' : { 'LMAX' : 10.800,  'LMIN' : -0.350, 'QCALMIN' : 1.0 , 'QCALMAX' : 255.0, 'SOLAR' : 84.9 },
        'DIA_JULIANO' : 2455026.191609,
        'ELEVACION_SOLAR' : 52.1847478        
    }
    return configuracion
