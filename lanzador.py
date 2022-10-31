from Ejercicio1 import Ejercicio1
from Ejercicio2 import Ejercicio2
from Ejercicio3 import *
from Ejercicio5 import Ejercicio5

def ejecutar():
    n = int(input('Elige el ejercicio que quieres ejecutar: '))

    if n==1:
        Ejercicio1.moverTorre(4,'Aguja1','Aguja2','Aguja3')