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
def las5navesmaspasajeros(lista,cont=0):
    if len(lista)<=5:
        for nave in lista:
            print(str(nave.get_nombre()))

    else:
        max=1
        if cont<4:
            for nave in lista:
                if nave.get_npasajeros()>max:
                    max=nave.get_npasajeros()
                else:
                    pass
            for nave in lista:
                if nave.get_npasajeros()==max:
                    print(str(nave.get_nombre()))
                    lista_naves.remove(nave)
                    cont+=1
                else:
                    pass
            return las5navesmaspasajeros(lista_naves,cont+1)

        
