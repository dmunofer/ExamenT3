from Ejercicio1 import Ejercicio1
from Ejercicio2 import Ejercicio2
import Ejercicio3.algoritmos as ej3
import Ejercicio3.nave
from Ejercicio3.nave import Nave
from Ejercicio4 import Ejercicio4
from Ejercicio5 import Ejercicio5

def ejecutar():
    n = int(input('Elige el ejercicio que quieres ejecutar: '))

    if n==1:
        Ejercicio1.moverTorre(4,'Aguja1','Aguja2','Aguja3')

    elif n==2:
        matriz=[[1,5,7],[4,1,2],[0,9,2]]
        Ejercicio2.sarrus_iter(matriz)

    elif n==3:
        Nave1=Nave('Halcón Milenario',800, 8,15)
        Nave2=Nave('Estrella de la Muerte',1800, 250,900)
        Nave3=Nave('X Wing',12,2,2)
        Nave4=Nave('AT-AT',44,10,20)
        Nave5=Nave('Caza TIE',6,1,1)
        Nave6=Nave('Interceptor',4,1,2)
        lista_naves=[Nave1, Nave2,Nave3,Nave4,Nave5,Nave6]

        ej3.ordenar_nombres(lista_naves)
        ej3.ordenar_nombres_reversa(lista_naves)
        ej3.halcon(lista_naves)
        ej3.estrella(lista_naves)
        ej3.las5navesmaspasajeros(lista_naves)
        ej3.mayortripulacion(lista_naves)
        ej3.comienzaconAt(lista_naves)
        ej3.mas6pasajeros(lista_naves)
        ej3.masgrande(lista_naves)
        ej3.maspequeño(lista_naves)

    elif n==4:
        polinomio1=input('Introduce el primer polinomio: ')
        polinomio2=input('Introduce el segundo polinomio: ')

        Ejercicio4.dividir(polinomio1,polinomio2)
        Ejercicio4.restar(polinomio1,polinomio2)


    elif n==5:
        mensaje= input('Introduce el mensaje que quieres encriptar: ')
        encriptado=Ejercicio5.encriptar(mensaje)
        print(encriptado)