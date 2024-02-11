import random
numero = random.randint(1,50)
respuesta = ...
print("Adivina el numero que estoy pensando ahora mismo")

while numero != respuesta:
    respuesta = int(input("Indroduce un numero entre 1 y 50:"))
    if respuesta > numero:
        print("Introduce un numero menor:")
    elif respuesta < numero:
        print("Introduce un numero mayor:")
    else:
        print("Has acertado!")
