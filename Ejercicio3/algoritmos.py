from clase_nave import *

Nave1=Nave('Halcón Milenario',800, 8,15)
Nave2=Nave('Estrella de la Muerte',1800, 250,900)
Nave3=Nave('X Wing',12,2,2)
Nave4=Nave('AT-AT',44,10,20)
Nave5=Nave('Caza TIE',6,1,1)
Nave6=Nave('Interceptor',4,1,2)
lista_naves=[Nave1, Nave2,Nave3,Nave4,Nave5,Nave6]



#print(Nave1)
#print(Nave2)

def ordenar_nombres(lista):
    lista_nombres=[]
    for nave in lista:
        lista_nombres.append(nave.get_nombre())
    lista_nombres.sort()
    print(lista_nombres)

def ordenar_nombres_reversa(lista):
    lista_nombres=[]
    for nave in lista:
        lista_nombres.append(nave.get_nombre())
    lista_nombres.sort()
    lista_nombres.reverse()
    print(lista_nombres)












def las5navesmaspasajeros(lista,cont=0):
    if len(lista)<=5:
        for nave in lista:
            print(nave.get_nombre())

    else:
        if cont<5:
            for nave in lista:
                max=1
                if nave.get_npasajeros()>max:
                    max=nave.get_npasajeros()
                else:
                    pass
            for nave in lista:
                if nave.get_npasajeros()==max:
                    print(nave.get_nombre())
                    lista_naves.remove(nave)
                else:
                    pass
            return las5navesmaspasajeros(lista_naves,cont+1)

def mayortripulacion(lista):
    max=1
    for nave in lista:

        if nave.get_tripulacion()>max:
            max=nave.get_tripulacion()
        else:
            pass
    for nave in lista:
        if nave.get_tripulacion==max:
            print(nave.get_nombre())

def comienzaconAt(lista):
    for nave in lista:
        if nave.get_nombre()[0]=='A' and nave.get_nombre()[1]=='T':
            print(nave.get_nombre())
        else:
            pass

def mas6pasajeros(lista):
    for nave in lista:
        if nave.get_npasajeros()>6:
            print(nave.get_nombre())

def masgrande(lista):
    lista_largos=[]
    for nave in lista:
        lista_largos.append(nave.get_largo())
    maximo=max(lista_largos)
    for nave in lista:
        if nave.get_largo==maximo:
            print(nave)

def maspequeño(lista):
    lista_largos=[]
    for nave in lista:
        lista_largos.append(nave.get_largo())
    minimo=min(lista_largos)
    for nave in lista:
        if nave.get_largo==minimo:
            print(nave)
        else:
            pass

