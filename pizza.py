print("BIENVENIDO A TU PIZZERÍA FAVORITA")

tamaño= input("De qué tamaño quieres la pizza? 'p' ,'m' o 'g':  ")

queso = input("Desee extra de queso en tu maravillosa pizza? 's' o 'n':  ")

pepperoni = input("Desee extra de queso en tu maravillosa pizza? 's' o 'n':  ")

cuenta=0

if tamaño == "p":
    cuenta = 5

elif tamaño == "m":
    cuenta = 8

elif tamaño == "g":
    cuenta = 11

else:
    print("No te entiendo mi pana")

if queso == "s":
    cuenta=cuenta + 1

if pepperoni == "s":
    cuenta +=2