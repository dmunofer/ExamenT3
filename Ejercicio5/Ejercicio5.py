import hashlib

def encriptar(mensaje):
    encriptado= hashlib.sha512(mensaje.encode())
    return encriptado.hexdigest()