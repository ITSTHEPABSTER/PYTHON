x=int(input("Escribe un numero entero:  "))
y=int(input(f"Escriba un número mayor que{x}:   "))

while (y <= x):
    print(f"LE HE DICHO QUE ESCRIBA UN NÚMERO MAYOR QUE {x}")
    y=int(input(f"Escriba un numero entero mayor que {x}"))

    par_impar=""

for i in range (x,y+1):
    if(i/2==0):
        par_impar="par"
        print(f"El número {i} es par")
    else:
        par_impar="impar"
        print(f"El número es impar")
