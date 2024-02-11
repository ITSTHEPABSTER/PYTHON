import dumb_menu

def cocacola(unidades):
    print("El coste de la Coca Cola es de 1,5€")
    coste = 1.5
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0 and unidades > 0:
        print(f"Tu cambio es de {dinero_restante}€")
        unidades -= 1
        print(f"Quedan {unidades} de cocacola")
    elif unidades == 0:
        print("No quedan Cocacolas :(")
    else:
        print("A PAGARRRRR🤑!!!")
    
    return unidades

def fanta(unidades):
    print("El coste de la Fanta es de 1,5€")
    coste = 1.5
    unidades = 5
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")
        unidades -= 1
    elif unidades == 0:
        print("No quedan Fanta :(")
    else:
        print("A PAGARRRRR🤑!!!")
    
    return unidades

def agua(unidades):
    print("El coste del agua es de 1€")
    coste = 1
    unidades = 10
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste
    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")
        unidades -= 1
    elif unidades == 0:
        print("No quedan Agua :(")

    else:
        print("A PAGARRRRR🤑!!!")

def limon(unidades):
    print("El coste de el Aquarius de Limón es de 1,5€")
    coste = 1.5
    unidades = 4
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")
    
        unidades -= 1
    elif unidades == 0:
        print("No quedan Aquarius de Limón :(")

    else:
        print("A PAGARRRRR🤑!!!")
    return unidades

def naranja(unidades):
    print("El coste de el Aquarius de Naranja es de 1,5€")
    coste = 1.5
    unidades = 4
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")
        unidades -= 1
    elif unidades == 0:
        print("No quedan Aquarius de Naranja :(")
    else:
        print("A PAGARRRRR🤑!!!")
    
    return unidades

def aquarius():
    tipos_aquarius = ["-Aquarius de Limón", "Aquarius de Naranja", "Volver al menú principal"]
    indice = dumb_menu.get_menu_choice(tipos_aquarius)
    unidades_limon = 4
    unidades_naranja = 4

    if indice == 0:
        limon(unidades_limon)
        input("Presiona enter para continuar...")

    if indice == 1:
        naranja(unidades_naranja)
        input("Presiona enter para continuar...")

    if indice == 2:
            main()
            input("Presiona enter para continuar...")


def sprite(unidades):
    print("El coste de el Sprite es de 1.5€")
    coste = 1.5
    unidades = 5
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Sprite :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades


def kitkat (unidades):
    print("El coste de el Kitkat es de 1€")
    coste = 1
    unidades = 5
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Kitkat :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades

def conchitas (unidades):
    print("El coste de las Conchitas es de 0.5€")
    coste = 0.5
    unidades = 10
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Conchitas :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades

def huesitos (unidades):
    print("El coste de los huesitos es de 0.5€")
    coste = 0.5
    unidades = 8
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Huesitos :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades

def gofres (unidades):
    print("El coste de los gofres es de 1€")
    coste = 1
    unidades = 10
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Gofres :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades

def oreo (unidades):
    print("El coste de los oreo es de 1€")
    coste = 1
    unidades = 10
    dinero = float(input("Introduzca el dinero: €"))
    dinero_restante = dinero-coste

    if dinero_restante >= 0:
        print(f"Tu cambio es de {dinero_restante}€")

        unidades -= 1
    elif unidades == 0:
        print("No quedan Oreos :(")

    else:
        print("A PAGARRRRR🤑!!!")

    return unidades

def snacks():
    opciones = ["-Kitkat","-Conchitas", "-Huesitos", "-Gofres","-Oreo" , "-Volver al menú principal"]
    unidades_kitkat = 5
    unidades_conchitas = 10
    unidades_huesitos = 8
    unidades_gofres = 10
    unidades_oreo = 10
    while True:
        indice = dumb_menu.get_menu_choice(opciones)
        if indice == 0:
            kitkat(unidades_kitkat)
            input("Presiona enter para continuar...")

        if indice == 1:
            conchitas(unidades_conchitas)
            input("Presiona enter para continuar...")

        if indice == 2:
            huesitos(unidades_huesitos)
            input("Presiona enter para continuar...")
        
        if indice == 3:
            gofres(unidades_gofres)
            input("Presiona enter para continuar...")

        if indice == 4:
            oreo(unidades_oreo)
            input("Presiona enter para continuar...")
        
        if indice == 5:
            main()
            input("Presiona enter para continuar...")
            
     
      
def main():
    opciones = ["-Bebidas🥤","-Snacks🍫", "-Salir😥"]
    while True:
        indice = dumb_menu.get_menu_choice(opciones)
        if indice == 0:
            bebidas()
            input("Presiona enter para continuar...")

        if indice == 1:
            snacks()
            input("Presiona enter para continuar...")

        if indice == 2:
            input("Presiona enter para continuar...")
            exit()

def bebidas():
    opciones1 = ["-Cocacola", "-Fanta", "-Aquarius", "-Agua", "-Sprite", "-Volver al menú principal"]    
    unidades_cocacola = 5
    unidades_fanta = 5
    unidades_agua = 10
    unidades_sprite = 5
    while True:
        indice = dumb_menu.get_menu_choice(opciones1)
        if indice == 0:
            unidades_cocacola = cocacola(unidades_cocacola)
            input("Presiona enter para continuar...")

        if indice == 1:
            unidades_fanta = fanta(unidades_fanta)
            input("Presiona enter para continuar...")

        if indice == 2:
            aquarius()
            input("Presiona enter para continuar...")

        if indice == 3:
            agua(unidades_agua)
            input("Presiona enter para continuar...")

        if indice == 4:
            sprite(unidades_sprite)
            input("Presiona enter para continuar...")

        if indice == 5:
            main()
            input("Presiona enter para continuar...")

main()