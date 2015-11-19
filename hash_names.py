#!/usr/bin/python3

import sys
import string
from math import sqrt

tabla = {}
abecedario = string.ascii_lowercase
primos = [
          2, 3, 5, 7, 11, 13, 17, 
          19, 23, 29, 31, 37, 41, 
          43, 47, 53, 59, 61, 67, 
          71, 73, 79, 83, 89, 97, 
          101
         ] 

db = [None]
tamanio_db = 0
nofilas = 0
nocolumnas = 0
cnt_coliciones = 0
cnt_personas = 0
ARCHIVO = "nombres_completos.txt"
nombres_completos = []


def leer_datos_de_archivo(archivo):
    global nombres_completos
    with open(archivo, 'r') as f:
        nombres_completos = f.readlines()
    

def crear_tabla_de_codigos_de_letras(abecedario, primos):
    global tabla

    if len(abecedario) != len(primos):
        raise NameError("primos y abecedarios deben ser de igual tamanio")
    for letra, primo in zip(abecedario, primos):
        tabla[ letra ] = primo


def obtener_tamanio_matriz(tamanio):

    print("Tamanios de la base de datos disponibles:")
#    for i in range(2,24):
#        print(i*i*2, end=" ")
#    print("")

    if tamanio == 0:
        n = input("Elegir un tamanio: ")
        n = int(n)
    else:
        n = tamanio

    nocolumnas = int(sqrt(int(n/2)))
    
    if nocolumnas * nocolumnas * 2 != n:
        print("redondear al multiplo de 3 mas proximo")
        
    nofilas = 2 * nocolumnas
    return nofilas, nocolumnas
    

def pedir_nombres():
    nombres = input("Introduce nombres: ")
    apellidos = input("Introduce apellidos: ")
    return nombres, apellidos


def obtener_hash(palabra):

    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')

    i = 1
    cont = 0
    for letra in palabra:
        cont += tabla[ letra ] * i
        i += 1
#    print("palabra: {0}\thash: {1}".format(palabra, cont))
    return cont

def obtener_indice(nombre, apellido):
    ind_fila = obtener_hash(nombre) % nofilas
    ind_col = obtener_hash(apellido) % nocolumnas
    return ind_fila, ind_col

def imprimir_db():
#    for fila in db:
#        for columna in fila:
#            print("nombre: {0}".format(columna))
    print("===================================")
    print("Tamanio de la base de datos:{0}".format(tamanio_db))
    print("TOTAL de personas:{0}".format(cnt_personas))
    print("Numero de coliciones: {0}".format(cnt_coliciones))



def ingresar_nombre_a_db(nombre, apellido, buscar):
    global db, cnt_coliciones

    fila, columna = obtener_indice(nombre, apellido)
#    print("hash: fila: {0}\tcolumna: {1}".format(fila, columna))

    flag_contador_coliciones =  False
    # buscar casilla libre
    while True:
        if db[ fila ][ columna ] == None:
            if buscar == True:
               print("No se encontro")
            break
        
        if db[ fila ][ columna ] == [nombre, apellido]:
            if buscar == True:
                print("dato buscado {0}".format( db[ fila ][ columna ]))
            break

        if flag_contador_coliciones == False:
            cnt_coliciones += 1
            flag_contador_coliciones = True

#        print("Se ha encontrado una colicion")
#        print("en la fila:{0} columna:{1}".format(fila, columna))
#        print("que tiene el nombre {0}".format(db[ fila ][ columna ] ))
#        print("ajustar a nueva posicion")
        # resolviendo desbordamientos en la tabla
        if columna == nocolumnas - 1:
            columna = 0
            if fila == nofilas - 1:
                fila = 0
            else:
                fila += 1
        else:
            columna += 1            

    if buscar == False:
        db[ fila ][ columna ] = [nombre, apellido]

#    print("ajuste fila: {0}\tcolumna: {1}".format(fila, columna))
 


def introducir_nombres_a_database(usuario, cantidad_requerida):
    global cnt_personas

    if cantidad_requerida > len(nombres_completos):
        print("faltan mas nombre en el archivo para completar")
        exit(1)

    while True:
        if usuario == True:
            nombre, apellido = pedir_nombres()
        else:
            nombres_completos[ cnt_personas ] = nombres_completos[ cnt_personas ].replace('\n', '')
            nombre = nombres_completos[ cnt_personas ].split(',')[ 0 ]
            apellido = nombres_completos[ cnt_personas ].split(',')[ 1 ]

        ingresar_nombre_a_db(nombre, apellido, False)
        cnt_personas += 1
        if usuario == True:
            res = input("desea continuar? [s/n]:")
            if res == 'n':
                break;
        else:
            if cnt_personas == cantidad_requerida:
                break


def buscar_nombres_en_database():
    print("buscar personas, primero introducir nombres y luego apellidos")
    while True:
        res = input("desea continuar? [s/n]: ")
        if res == 'n':
            break;
        nombre, apellido = pedir_nombres()
        ingresar_nombre_a_db(nombre, apellido, True)
         

#8 18 32 50 72 98 128 162 200 242 288 338 
#392 450 512 578 648 722 800 882 968 1058
def main():
    global db, tamanio_db, nofilas, nocolumnas

    tamanio_db = 98
    if len(sys.argv) == 3:
        tamanio_db = int(sys.argv[1:2][0])
        cantidad_de_nombres = int(sys.argv[2:3][0])

    crear_tabla_de_codigos_de_letras(abecedario, primos)
    nofilas, nocolumnas = obtener_tamanio_matriz(tamanio_db)
    db = [[None for i in range(nocolumnas)] for j in range(nofilas)]
    print("tabla generada de {0} filas y {1} columnas".format(nofilas, nocolumnas))

    leer_datos_de_archivo(ARCHIVO)
    introducir_nombres_a_database(False, cantidad_de_nombres)
    imprimir_db() 
#    buscar_nombres_en_database()


if "__main__" == __name__:
    main()
