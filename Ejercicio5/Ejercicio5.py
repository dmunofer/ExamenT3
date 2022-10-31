import hashlib

mensaje= input('Introduce el mensaje que quieres encriptar: ')
mensaje_encriptado= hashlib.sha512(mensaje.encode())
print(mensaje_encriptado.hexdigest())