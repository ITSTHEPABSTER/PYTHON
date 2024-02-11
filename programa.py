import dumb_menu

def sumar():
    print("Sumar")
    numero1 = int(input("Introduce el un numero:    "))
    numero2 = int(input("Introduce otro numero:   "))
    print(numero1+numero2)

def resta():
    print("Resta")
    numero1 = int(input("Introduce el un numero:    "))
    numero2 = int(input("Introduce otro numero:   "))
    print(numero1-numero2)

def multiplicar():
    print("Multiplicar")
    numero1 = int(input("Introduce el un numero:    "))
    numero2 = int(input("Introduce otro numero:   "))
    print(numero1*numero2)

def dividir():
    print("Dividir")
    numero1 = int(input("Introduce el un numero:    "))
    numero2 = int(input("Introduce otro numero:   "))
    print(numero1/numero2)

def main():
    opciones = ["Sumar","Restar","Multiplicar","Dividir" , "Salir"]

    while True:
        indice = dumb_menu.get_menu_choice(opciones)
        if indice == 0:
            sumar()
            input("Presiona enter para continuar...")

        if indice == 1:
            resta()
            input("Presiona enter para continuar...")
        
        if indice == 2:
            multiplicar()
            input("Presiona enter para continuar...")

        if indice == 3:
            dividir()
            input("Presiona enter para continuar...")
        
        if indice == 4:
            print("Adiós con el corazón")
            exit()

if __name__=="__main__":
    main()