#Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000
#  en un archivo llamado numeros_prueba.txt. Luego debe leer desde el archivo 
# esos números y agregarlos a una lista, modifique o cree una nueva lista que 
# contenga solo los nñumeros impares. Finalmente con numpy determinar
# la dimensión de la lista. 
# Imprimir por consola la lista final y su dimensión.
import random
import numpy as np
def main():
    list()
    impar()
def list():
    nombre_fichero="./archivos/numeros_prueba-.tx"
    with open(nombre_fichero,"w", encoding="utf-8") as file:
        for i in range(1,21):
            numero_aleatorio= random.randint(100,1000)
            linea=str(numero_aleatorio)
            file.write(linea)
            file.write("\n")
def impar():
    nombre_fichero="./archivos/numeros_prueba-.tx"
    numeros=[]
    with open(nombre_fichero,"r") as file:
        for linea in file:
            numeros.append(int(linea))
        imp=[]
        for n in numeros:
            if n%2!=0:
                imp.append(n)
        print(imp)
        lista=np.array(imp)
        print(lista)
        print(lista.ndim)

if __name__ == '__main__':
    main()
