#Ejercicio  1
from logging import raiseExceptions
import sys
from threading import Timer



def moverTorre(ndiscos,origen, destino, intermedio):
    if ndiscos >= 1 and ndiscos<21:
        moverTorre(ndiscos-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(ndiscos-1,intermedio,destino,origen)
    else:
        raise Exception('Número de discos incorrecto')

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)


tiempo = 180
def timeout():
    print('Tiempo máximo superado')
    sys.exit()

t=Timer(tiempo,timeout)

moverTorre(14,'Aguja1','Aguja2','Aguja3')