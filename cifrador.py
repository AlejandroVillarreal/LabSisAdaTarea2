import sys
import os

cesar3 = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c',
    ' ' : ' '
}


#Completa esta funcion
def generar_cifrador(offset):
    letras = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]


#Completa esta funcion (quita # para activar)
print(os.getcwd())
try:
    archivo = open("nombre.txt", "r")
    lista = archivo.readline()
    archivo.close()
    print(lista)
except IOError as identifier:
    print("No se pudo leer el archivo")
    sys.exit(1)


def cifrar(palabra, cifrador):
    letras = [item for item in palabra]
    print(letras)
    #print(cifrador.values())
    palabra_cifrada=[]
    for letra in palabra:
        palabra_cifrada.append(cifrador.get(letra))
    print(palabra_cifrada)
    print(' '.join(palabra_cifrada))

def conentenidoCifrador(cifrador):
    for item in cesar3:
        print(f"Letra: {item}  Letra cifrada: {cesar3[item]}")


def curp(palabra):
    palabra.sort(reverse = True)
    print(palabra)


curp(lista)
#cifrar(lista,cesar3)
#conentenidoCifrador(cesar3)
#cifrar(lista, cesar3)
#Completa esta funcion (quita # para activar)
#def mostrar_cifrador(cifrador):

#Completa el resto del codigo