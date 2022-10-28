#Ejercicio  1

def moverTorre(ndiscos,origen, destino, intermedio):
    if ndiscos >= 1:
        moverTorre(ndiscos-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(ndiscos-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)


moverTorre(64,'Aguja1','Aguja2','Aguja3')