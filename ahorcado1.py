import random

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "computadora", "juego", "ahorcado", "desarrollo", "inteligencia", "algoritmo"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    print(resultado)

def pedir_letra():
    return input("Introduce una letra: ").lower()

def mostrar_ahorcado(intentos):
    etapas = [  # Etapa 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Etapa 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Etapa 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Etapa 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Etapa 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Etapa 1
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # Etapa 0
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    print(etapas[intentos])

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = set()
    letras_incorrectas = set()
    intentos_restantes = 6

    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos_restantes > 0:
        mostrar_ahorcado(intentos_restantes)
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        print(f"Intentos restantes: {intentos_restantes}")
        
        letra = pedir_letra()
        
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya has intentado esa letra. Prueba con otra.")
            continue
        
        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            if set(palabra_secreta) == letras_adivinadas:
                print(f"¡Felicidades! Has ganado. La palabra era: {palabra_secreta}")
                return
        else:
            letras_incorrectas.add(letra)
            intentos_restantes -= 1
            print("Letra incorrecta.")
    
    mostrar_ahorcado(0)
    print(f"¡Oh no! Has perdido. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()