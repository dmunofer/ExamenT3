#Ejercicio 2

def sarrus_iter(matriz):
    det = (matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0])-((matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[2][1]*matriz[1][2]*matriz[0][0])))
    return det


def sarrus_rec