import random
import dumb_menu
import urllib.request as url
import json
import folium
from datetime import datetime

# Presentación del programa
print("¡Bienvenido a Órbita Tr3s!")
print("Aquí podrás elegir los meses de 2023 en los cuales ocurren los eventos del espacio")

# Las elecciones y sus datos
def octubre():
    print("Octubre:")
    print("Eventos espaciales del mes de Octubre:")
    print("6 de octubre: Luna en cuarto menguante")
    print("8-9 Dracónidas lluvia de estrellas")
    print("14 Luna nueva y eclipse parcial de sol en Canarias")
    print("21-22 Oriónidas lluvia de estrellas")
    print("22 Luna en cuarto creciente")
    print("23 Venus en máxima elongación oeste")
    print("28 Luna llena y Eclipse parcial en España")
    print("29 Cambio de hora")

def noviembre():
    print("Noviembre:")
    print("Eventos espaciales del mes de Noviembre:")
    print("3 Oposición de Júpiter")
    print("13 Luna nueva y oposición Urano")
    print("17-18 Leónidas lluvia de estrellas")
    print("27 Luna llena")
    print("30 Manhattanhenge (Solsticio de Manhattan)")

def diciembre():
    print("Diciembre:")
    print("Eventos espaciales del mes de Diciembre:")
    print("4 Mercurio máxima elongación este")
    print("13 Luna llena")
    print("14-15 Gemínidas lluvia de estrellas")
    print("22 Solsticio de invierno o verano")
    print("22-23 Úrsidas lluvia de estrellas")
    print("27 Luna nueva") 

def datos_curiosos():
    print("Datos Curiosos")
    print("¿Sabías que?: ")
    datos = ["Mercurio tiene cola",
            "Hay un hombre enterrado en la Luna",
            "Hay un planeta que probablemente esté formado por diamantes",
            "En Neptuno y Urano llueven diamantes",
            "Hay una nube de agua flotando en el espacio",
            "Figuras de lego fueron enviadas a orbitar Júpiter",
            "Un anillo de bodas perdido se encontró en el espacio",
            "Hay más árboles en la tierra que estrellas en la Vía Láctea",
            "Neptuno solo ha completado una órbita alrededor del sol desde su descubrimiento"]
    print(random.choice(datos))

def satelite():
    ISS = url.Request("http://api.open-notify.org/iss-now.json")
    response_ISS = url.urlopen(ISS)

    ISS_obj = json.loads(response_ISS.read())

    print(ISS_obj['iss_position']['latitude'])
    print(ISS_obj['iss_position']['longitude'])

    long = ISS_obj['iss_position']['longitude']
    lat = ISS_obj['iss_position']['latitude']

    m = folium.Map(location=[lat, long], zoom_start=2, tiles='Stamen Terrain')
    icon = folium.Icon(color="red")
    folium.Marker([lat, long], tooltip="ISS", icon=icon).add_to(m)
    print(m)

    astros = url.Request("http://api.open-notify.org/astros.json")
    response_astros = url.urlopen(astros)

    astros_obj = json.loads(response_astros.read())

    print(astros_obj['number'])

    astros_list = []
    for count, item in enumerate(astros_obj['people'], start=0):
        print(astros_obj['people'][count]['name'])
        astros_list.append(astros_obj['people'][count]['name'])

    # Latitud y Logitud de la Ciudad de Madrid (usada como ejemplo)
    latitud = 40.4
    longitud = -3.7
    n = 5  # número de veces que pasará la ISS

    Pass = url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud, longitud, n))
    response_Pass = url.urlopen(Pass)

    Pass_obj = json.loads(response_Pass.read())

    pass_list = []
    for count, item in enumerate(Pass_obj["response"], start=0):
        pass_list.append(Pass_obj['response'][count]['risetime'])
        print(datetime.fromtimestamp(pass_list[count]).strftime('%d-%m-%Y %H:%M:%S'))

def main():
    opciones = ["-Octubre", "-Noviembre", "-Diciembre", "-Datos Curiosos", "-Satelite", "-Salir"]

    while True:
        indice = dumb_menu.get_menu_choice(opciones)
        if indice == 0:
            octubre()
            input("Presiona enter para continuar...")

        if indice == 1:
            noviembre()
            input("Presiona enter para continuar...")

        if indice == 2:
            diciembre()
            input("Presiona enter para continuar...")

        if indice == 3:
            datos_curiosos()
            input("Presiona enter para continuar...")

        if indice == 4:
            satelite()
            input("Presiona enter para continuar...")

        if indice == 5:
            print("Adiós con el corazón")
            exit()

if __name__ == "__main__":
    main()
