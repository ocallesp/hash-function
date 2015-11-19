#!/usr/bin/python3

import sys
import string
import random

CANTIDAD_NOMBRES = 200
MAX_TAMANIO_NOMBRE = 20
MAX_TAMANIO_APELLIDOS = 30
MIN_TAMANIO = 10

LETRAS = list(string.ascii_lowercase)
LETRAS.append(' ')

ARCHIVO = "nombres_completos.txt"
semilla = 0

def generar(tamanio_minimo, tamanio_maximo, cantidad):
    nombres = []

    for i in range( cantidad ):
        tamanio_nombre = random.randrange(tamanio_minimo, tamanio_maximo)
        if tamanio_nombre < 2:
            n = len(nombres)
            if n != 0:
                nombres.append( nombres[ random.randrange(0, n-1) ] )
        else:
            tmp_nombre = []
            for j in range( tamanio_nombre ):
                tmp_nombre.append( random.choice( LETRAS ) )
            nombres.append( "".join(tmp_nombre ) )

    return nombres


def generar_nombres_completos(cantidad, lista_nombres, lista_apellidos ):
    lista_nombre_completos = []
    for i in range(cantidad):
        apellido = lista_apellidos[ random.randrange(0, lista_apellidos.__len__()) ]
        nombre = lista_nombres[ random.randrange(0, lista_nombres.__len__())]
        lista_nombre_completos.append("{0},{1}".format(nombre, apellido))

    return lista_nombre_completos


def guardar_nombres(nombre_completo):
    with open(ARCHIVO, 'w') as fd:
        for nombre in nombre_completo:
            fd.write(nombre + '\n')
    


semilla = 33
if len(sys.argv) == 2:
    semilla = int(sys.argv[1:2][0])
print("semilla:{0}".format(semilla))
random.seed(semilla)
lista_nombres = generar(MIN_TAMANIO, MAX_TAMANIO_NOMBRE, 200)
lista_apellidos = generar(MIN_TAMANIO, MAX_TAMANIO_APELLIDOS, 400)

lista_nombres_completos = generar_nombres_completos(200, lista_nombres, lista_apellidos)

guardar_nombres(lista_nombres_completos)


