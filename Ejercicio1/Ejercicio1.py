#Ejercicio  1
import sys
from threading import Timer



def moverTorre(ndiscos,origen, destino, intermedio):
    if ndiscos >= 1:
        moverTorre(ndiscos-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(ndiscos-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)


tiempo = 180
def timeout():
    print('Tiempo máximo superado')
    sys.exit()

t=Timer(tiempo,timeout)

moverTorre(64,'Aguja1','Aguja2','Aguja3')