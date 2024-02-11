import random
def bien():
    mensajes = ["¡Muy bien!",
                 "¡Perfecto campeón!",
                  "¡Genial!",
                  "Eres una máquina"]
    mensaje_aleatorio = random.choice(mensajes)
    print(mensaje_aleatorio)
import random
def mal():
    mensajes = ["No vamos en buen camino.¡Tú puedes!",
                 "Eres muy malo eh.",
                  "Eres malísimo",
                  "¡No te rindas!" ]
    mensaje_aleatorio = random.choice(mensajes)
    print(mensaje_aleatorio)
print("Bienvenido a mi lista de juegos.")
eleccion = input("\n-Preguntas y respuestas(Pasapalabra)\n-Test de personalidad\n-Aventura\n-Fortnite\n-Adivina el número\n-Matemáticas(Mates)\n\n¿Cúal te gustaria escoger?: ")
#Pasapalabra
if eleccion == "pasapalabra":
    print("¡Escogiste Pasapalabra!. Este juego consiste en acertar la definición de una palabra con esa letra")
    respuesta = input("Empezemos con la letra a:Planta de tronco leñoso, grueso y elevado que se ramifica a cierta altura del suelo formando la copa.\n").lower()
    if respuesta == "arbol":
        bien()
    else:
        print("No pasa nada que esto acaba de empezar.") 
    respuesta = input("Letra b:Niño recién nacido o de pocos meses y que todavía no anda.\n")
    if respuesta == "bebe":
        bien()
    else:
        mal()
    respuesta = input("Letra c:Mamífero équido, macho, de tamaño mediano o grande, pelo corto de color generalmente uniforme y orejas cortas; se domestica con facilidad y suele usarse para la monta; hay muchas especies diferentes.\n").lower()
    if respuesta == "caballo":
        bien()
    else:
        mal()   
    respuesta = input("Letra d:Conjunto de monedas y billetes que se usan como medio legal de pago.\n").lower()
    if respuesta == "dinero":
        bien()
    else:
        mal()
    respuesta = input("Letra e:EL MEJOR PAÍS DEL MUNDO\n").lower()
    if respuesta == "españa":
        print("Eres unos de los míos")
    else:
        print("Se respeta pero creo que estás equivocado")
    respuesta = input("Letra f:Que carece de belleza o atractivo y no resulta agradable de contemplar o de escuchar.\n").lower()
    if respuesta == "feo":
        bien()
    else:
        mal()
    respuesta = input("Letra g:Que tiene un tamaño superior al que se considera normal o superior en comparación al de otra cosa de su misma naturaleza.\n").lower()
    if respuesta == "grande":
        bien()
    else:
        mal()
    respuesta = input("Letra h:Aeronave con una gran hélice en su parte superior central y otra más pequeña en la cola; este sistema permite que el aparato despegue y aterrice en vuelo vertical, se desplace en el aire hacia delante o hacia atrás, a derecha o izquierda o, incluso, que se mantenga suspendido en el aire.\n").lower()
    if respuesta == "helicoptero":
        bien()
    else:
        mal()
    respuesta = input("Letra i:Mineral constituido por una combinación de dos óxidos de hierro, de color negruzco, muy pesado, que tiene la propiedad de atraer el hierro, el acero y algún otro cuerpo.\n").lower()
    if respuesta == "iman":
        bien()
    else:
        mal()
    respuesta = input("Letra j:Sustancia sólida o líquida que, mezclada con agua, sirve para lavarse o lavar la ropa, fregar, etc.; se obtiene de la combinación de un álcali con los ácidos del aceite u otro cuerpo graso.\n").lower()
    if respuesta == "jabon":
        bien()
    else:
        mal()
    respuesta = input("Letra k:Mamífero marsupial de hasta 80 cm de longitud, aspecto parecido a un osezno, con abundante pelo gris rojizo, orejas grandes y peludas, y cuatro patas prensiles y provistas de uñas afiladas; sus movimientos son muy lentos, es arborícola y vive en Australia.\n").lower()
    if respuesta == "koala":
        bien()
    else:
        mal()
    respuesta = input("Letra l:Éxito o resultado muy satisfactorio en una cosa.\n").lower()
    if respuesta == "logro":
        bien()
    else:
        mal()
    respuesta = input("Letra m:Mujer que ha tenido uno o más hijos, o animal hembra que ha tenido una o más crías.").lower()
    if respuesta == "madre":
        bien()
    else:
        mal()
    respuesta = input("Letra n:Precipitación en forma de pequeños cristales de hielo, generalmente ramificados, provenientes de la congelación de partículas de agua en suspensión en la atmósfera, que se pueden agrupar al caer y llegar a la superficie terrestre en forma de copos blancos, los cuales a su vez y en determinadas condiciones de temperatura se agrupan formando una capa sobre la superficie terrestre.").lower()
    if respuesta == "nieve":
        bien()
    else:
        mal()
    respuesta = input("Letra ñ(Contiene la ñ):Mano cerrada.\n").lower()
    if respuesta == "puño":
        bien()
    else:
        mal()
    respuesta = input("Letra o:Metas o deseos que se proponen las personas a sí mismas.\n").lower()
    if respuesta == "objetivo":
        bien()
    else:
        mal()
    respuesta = input("Letra p:Trozo de madera más largo que grueso y generalmente de forma cilíndrica y fácil de manejar.\n").lower()
    if respuesta == "palo":
        bien()
    else:
        mal()
    respuesta = input("Letra q:Ciencia que estudia la composición y las propiedades de la materia y de las transformaciones que esta experimenta sin que se alteren los elementos que la forman.\n").lower()
    if respuesta == "química":
        bien()
    else:
        mal()
    respuesta = input("Letra r:Mamífero roedor más grande que el ratón, de pelo basto y rígido, cola larga, patas cortas, cabeza pequeña y orejas tiesas; es nocturno, muy fecundo, destructor y voraz, y vive tanto en bosques y desiertos como en construcciones humanas o barcos; hay muchas especies, que se diferencian sobre todo en color y tamaño.\n").lower()
    if respuesta == "rata":
        bien()
    else:
        mal()
    respuesta = input("Letra s:Líquido, de color rojo en los vertebrados, que, impulsado por el corazón, circula por los vasos sanguíneos del cuerpo de las personas y los animales, transportando oxígeno, alimentos y productos de desecho.\n").lower()
    if respuesta == "sangre":
        bien()
    else:
        mal()
    respuesta = input("Letra t:Fruto de esta planta, comestible, de piel roja, verde o amarilla, lisa y brillante, pulpa muy jugosa y semillas amarillas y planas.\n").lower()
    if respuesta == "tomate":
        bien()
    else: 
        mal()
    respuesta = input("Letra u:Conjunto de todo lo que tiene existencia física, en la Tierra y fuera de ella.\n").lower()
    if respuesta == "universo":
        bien()
    else:
        mal()
    respuesta = input("Letra v:Nombre genérico de la ropa que cubre y resguarda el cuerpo humano.\n").lower()
    if respuesta == "vestido":
        bien()
    else:
        mal()
    respuesta = input("Letra w:Tecnología que permite conectar diferentes equipos informáticos a través de una red inalámbrica de banda ancha\n").lower()
    if respuesta == "wifi":
        bien()
    else:
        mal()
    respuesta = input("Letra x:Instrumento musical de percusión formado por una serie de láminas de madera dispuestas horizontalmente y ordenadas según su tamaño que, al ser golpeadas, emiten sonidos correspondientes a diferentes notas musicales; se toca con dos o cuatro macillas.\n").lower()
    if respuesta == "xilofono":
        bien()
    else:
        mal()
    respuesta = input("Letra y:Mamífero équido, hembra, de tamaño mediano o grande, pelo corto de color generalmente uniforme y orejas cortas; se domestica con facilidad y suele usarse para la monta; hay muchas especies diferentes.\n").lower()
    if respuesta == "yegua":
        bien()
    else:
        mal()
    respuesta = input("Letra z:Líquido contenido en el tejido de las frutas que puede extraerse por presión, cocción, etc., y beberse.\n").lower()
    if respuesta == "zumo":
        bien()
    else:
        mal()
#Test de personalidad   
    
elif eleccion == "test de personalidad":
    import random

    def apertura():
        preguntas = ["¿Te gusta probar cosas nuevas?:   ",
                "¿Te interesa la exploración de ideas?: ",
                "¿Eres imaginativo y creativo?: ",
                "¿Te gustan las experiencias emocionantes?: ",
                "¿Disfrutas de la música y las artes?:  "]
        mensaje_aleatorio = random.choice(preguntas)
        return mensaje_aleatorio

    def conciencia():
        preguntas =  ["¿Eres una persona organizada?",
                  "¿Te gusta tener un plan y seguirlo?",
                  "¿Eres responsable y confiable?",
                  "¿Te enojas con las personas que llegan tarde?",
                  "¿Eres perfeccionista?"]
        return preguntas

    def extroversión(): 
        preguntas =["¿Te gusta estar en el centro de atención?",
                "¿Eres el alma de la fiesta?",
                "¿Te gusta conocer gente nueva?",
                "¿Te gusta hablar en público?",
                "¿Disfrutas de grandes grupos de personas?"]
        return preguntas

    def amabilidad(): 
        preguntas = ["¿Te preocupas por los demás?",
                 "¿Te esfuerzas por hacer felices a los demás?",
                 "¿Eres compasivo y empático?",
                 "¿Te gusta ayudar a los demás?",
                 "¿Te preocupas por los animales y el medio ambiente?"]
        return preguntas

    def neuroticismo(): 
        preguntas = ["¿Te sientes ansioso con frecuencia?",
                 "¿Te preocupas por las cosas pequeñas?",
                 "¿Te sientes triste o deprimido con frecuencia?",
                 "¿Te asustan las cosas nuevas o desconocidas?",
                 "¿Eres fácilmente estresado?"]
        return preguntas
    
    print("Esto es un test para conocerte más.")
    print("Hay 5 tipos:")
    print("- Apertura: Muestra en qué grado un sujeto tiende a buscar nuevas experiencias personales y concibe de una manera creativa su futuro.")
    print("- Conciencia: Este rasgo de personalidad se refiere a cuán centrado está el sujeto en sus objetivos, además de cuán disciplinado se muestra para la consecución de dichos fines.")
    print("- Extroversión: Define el grado en que el sujeto se muestra abierto con los demás y canaliza su energía en contextos sociales.")
    print("- Amabilidad: Este grado define a las personas que exhiben una gran amabilidad mostrarán signos de confianza, altruismo, amabilidad y afecto.")
    print("- Este grado define a las personas que exhiben altos niveles de neuroticismo tenderán a experimentar cambios de humor, ansiedad e irritabilidad. ")
    print("¡Empecemos!")

    respuesta1 = input(apertura()).lower()
    if respuesta1 == "si":
        print("¡Genial!\nTienes mucha imaginación y perspicacia")
    else:
        print("ok")

    respuesta2 = input(conciencia()[0]).lower()
    if respuesta2 == "si":
        print("¡Genial!\nTienes altos niveles de consideración, buen control de los impulsos y conductas dirigidas a objetivos.")
    else:
        print("ok")

    respuesta3 = input(extroversión()[0]).lower()
    if respuesta3 == "si":
        print("¡Genial!\nEs fácilmente identificable y ampliamente reconocible como 'alguien que se llena de energía en compañía de otros'.")
    else:
        print("ok")

    respuesta4 = input(amabilidad()[0]).lower()
    if respuesta4 == "si":
        print("Las personas que exhiben una gran amabilidad mostrarán signos de confianza, altruismo, amabilidad y afecto.")
    else:
        print("ok")

    respuesta5=input(neuroticismo()[0]).lower()
    if respuesta5 == "si":
        print("¡Genial!\nEl neuroticismo se caracteriza por tristeza, mal humor e inestabilidad emocional.")
    else:
        print("ok")
#aventura
elif eleccion == "aventura":
    import time

    # Definir función para pausar el juego
    def pausar_juego():
        time.sleep(1)

    # Saludo e introducción
    print("¡Bienvenido al modo aventura!")
    pausar_juego()
    print("Estás en una cueva oscura y fría.")
    pausar_juego()

    # Ofrecer opciones al jugador
    print("¿Qué te gustaría hacer?")
    pausar_juego()
    print("1) Explorar la cueva")
    pausar_juego()
    print("2) Descansar y recuperar energía")
    pausar_juego()
    print("3) Salir de la cueva")
    pausar_juego()

    # Obtener elección del jugador
    eleccionaventura = input("Ingrese el número de la opción que desea elegir: ")

    # Realizar acción basada en elección del jugador
    if eleccionaventura == "1":
        print("¡Te aventuras más adentro en la cueva!")
        pausar_juego()
        print("Te encuentras un monstruo")
        pausar_juego()
        print("¿Qué te gustaría hacer?")
        pausar_juego()
        print("1)Lo matas")
        pausar_juego()
        print("2)Te piras")
        pausar_juego()
        eleccionaventura2 = input("Ingrese el número de la opción que desea elegir: ")
        if eleccionaventura2 == "1":
            print("Lo matas y te encuentras una gema")
            pausar_juego()
            print("¿Qué te gustaría hacer?")
            pausar_juego()
            print("1)Cogerlo")
            pausar_juego()
            print("2)Irte")
            eleccionaventura3 = input("Ingrese el número de la opción que desea elegir:").lower()
            if eleccionaventura3 == "1":
                print("Coges la gema y mueres")
            elif eleccionaventura3 == "2":
                print("Sales de la cueva sano y te vas a tu casa")
        elif eleccionaventura2 == "2":
            print("Sales de la cueva sano y te vas a tu casa")
    elif eleccionaventura == "2":
        print("Te sientas a descansar y recuperas energía pero mueres porque has pisado en una mina.")
    elif eleccionaventura == "3":
        print("Sales de la cueva y te encuentras en un paisaje impresionante.")
    else:
        print("Esa no es una opción válida.")
    # Despedida
    pausar_juego()
    print("¡Gracias por jugar! Vuelve pronto.")

#Fortnite
elif eleccion == "fortnite":
    import time

    # Definir función para pausar el juego
    def pausar_juego():
        time.sleep(1)
    #Inicio de la partida
    print("Pues preparate porque esto no es un juego")
    pausar_juego()
    print("Ha empezado la partida del siglo!!.")
    pausar_juego()
    print("¿Dónde quieres caer?")
    pausar_juego()
    print("1)Pisos picados(Hay muchas personas pero hay más riesgo de muerte)")
    pausar_juego()
    print("2)Señorío de la Sal(Hay muy buen loot pero no es muy poblado")
    pausar_juego()
    print("3)Chiringuito Chatarra(Muy poco loot y hay muy poca gente)")
    pausar_juego()
    print("4)Aterrizaje Afortunado(Muy buen loot,no hay mucha gente pero no está en el centro del mapa entonces la tormenta te puede pillar por tonto)")
    pausar_juego()
    mapa = input("Ingrese el número de la opción que desea elegir:  ").lower()
    #Pisos picados
    if mapa== "1":
        print("Hay mucha gente en Pisos Picados.")
        pausar_juego()
        print("¿Qué prefieres hacer?")
        pausar_juego()
        print("1)Irte de Pisos Picados y coger un arma en una casa segura sin gente")
        pausar_juego()
        print("2)Pelearte con un man por un arma en una casa con 3 personas")
        pausar_juego()
        eleccion1pisos=input("Ingrese el número de la opción que desea elegir:  ").lower()
        #irte de pisos picados
        if eleccion1pisos == "1":
            print("Coges una pistola de mierda.")
            pausar_juego()
            print("¿A donde quieres ir?") 
            pausar_juego()
            print("1)Te vas a un pueblo sin gente")
            pausar_juego()
            print("2)Vuelves a Pisos Picados")
            pausar_juego()
            print("3)Campeas")
            pausar_juego()
            eleccion2pisos= input("Ingrese el número de la opción que desea elegir:").lower()
            #pueblo
            if eleccion2pisos=="1":
                print("Te has encontrado un buen looteo pero hay un man.")
                pausar_juego()
                print("Que quieres hacer?")
                pausar_juego()
                print("1)Pelear")
                pausar_juego()
                print("2)Pirarte")
                pausar_juego()
                eleccion3pisos =input("Ingrese el número de la opción que desea elegir:").lower()
                #pelear
                if eleccion3pisos == "1":
                    print("Has ganado la batalla pero te has quedado a poca vida.")
                    print("Que haces ahora subnormal?")
                    pausar_juego()
                    print("1)Vas en busca de loot")
                    pausar_juego()
                    print("2)Campear")
                    pausar_juego()
                    eleccion4pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                    #loot
                    if eleccion4pisos == "1":
                        print("Tuviste suerte eh.")
                        pausar_juego()
                        print("Tienes un botiquín.")
                        pausar_juego()
                        print("Quedan 20 personas.")
                        pausar_juego()
                        print("¿Qué quieres hacer?")
                        pausar_juego()
                        print("1)Atacar al enemigo más cercano")
                        pausar_juego()
                        print("2)Construir tu base")
                        pausar_juego()
                        print("Campear")
                        pausar_juego()
                        eleccion5pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                        #atacar
                        if eleccion5pisos == "1":
                            print("Pierdes la pelea con un escopetazo a la cabeza")
                        #campear
                        elif eleccion5pisos == "2":
                            print("No te cubriste bien y te snipearon")
                         #base
                        elif eleccion5pisos == "3":
                            print("Has matado a 2 personas con tu gran base y quedan 3 personas en la partida pero viene la tormenta.")
                            pausar_juego()
                            print("Que quieres hacer?")
                            pausar_juego()
                            print("1)Moverte para estar a salvo de la tormenta")
                            pausar_juego()
                            print("2)Pelearte con un man")
                            pausar_juego()
                            eleccion6pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                            #mover
                            if eleccion6pisos == "1":
                                print("Te matan con un scar")
                            #pelear
                            elif eleccion6pisos == "2":
                                print("Matas a un pavo.")
                                pausar_juego()
                                print("QUEDA 1 PERSONA!!")
                                pausar_juego()
                                print("El personaje esta corriendo hacia la tormenta mientras tu estas en la misma posición que él.")
                                pausar_juego()
                                print("Que haces ahora?")
                                pausar_juego()
                                print("1)Pelear")
                                pausar_juego()
                                print("2)Ir hacia la tormenta y olvidarte del man")
                                pausar_juego()
                                eleccion7pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                                #pelear
                                if eleccion7pisos == "1":
                                    print("GANAS LA PARTIDA.")
                                    pausar_juego()
                                    print("GG")
                                    pausar_juego()
                                    print("MUY EZZZZZ,NO?")
                                    pausar_juego()
                                    print("Espero verte por aqui de nuevo.")
                                    pausar_juego()
                                    print("ADIOS :)")
                                    pausar_juego()
                                #irte
                                elif eleccion7pisos == "2":
                                    print("Te matan por detrás.")
                                    pausar_juego()
                                    print("Muy bien intentado pero a la siguiente lo conseguirás")
                                    pausar_juego()
                                    print("SIKEEEE L BOZO")
                                    pausar_juego()
                    #campear
                    elif eleccion4pisos == "2":
                        print("Te mata la tormenta por gay")         
                #pirarte
                elif eleccion3pisos == "2":
                    print("Te han snipeado.")
                    pausar_juego()
                    print("JODETEEE. PA EL LOBBYYYYYYYYYYYYYYYYYYYYYYYYY")        
            #campeas
            elif eleccion2pisos == "3":
                print("Has matado a alguien campeando como una puta rata.")
                pausar_juego()
                print("Qué haces ahora?")
                pausar_juego()
                print("1)Sigues campeando")
                pausar_juego()
                print("2)Te piras a coger materiales")
                pausar_juego()
                eleccion3pisos =input("Ingrese el número de la opción que desea elegir:").lower()
                #campear
                if eleccion3pisos == "1":
                    print("Eres muy aburrido,no?")
                    pausar_juego()
                    print("Quedan 4 personas porque tuviste suerte con tu localización en el mapa.")
                    pausar_juego()
                    print("¿Qué haces ahora?")
                    pausar_juego()
                    print("1)Campear")
                    pausar_juego()
                    print("2)Base")
                    pausar_juego()
                    print("3)Atacar con una pistola")
                    pausar_juego()
                    eleccion4pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                    #campear
                    if eleccion4pisos == "1":
                        print("QUEDAN 1 PERSONA!!.")
                        pausar_juego()
                        print("El personaje esta corriendo hacia la tormenta mientras tu estas en la misma posición que el.")
                        pausar_juego()
                        print("Que haces ahora?")
                        pausar_juego()
                        print("1)Pelear")
                        pausar_juego()
                        print("2)Ir hacia la tormenta y olvidarte del man")
                        pausar_juego()
                        eleccion5pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                        #pelear
                        if eleccion5pisos == "1":
                            print("GANAS LA PARTIDA.")
                            pausar_juego()
                            print("GG.")
                            pausar_juego()
                            print("MUY EZZZZZ,NO?")
                            pausar_juego()
                            print("Espero verte por aqui de nuevo. ADIOS :)")
                            pausar_juego()
                        #irte
                        elif eleccion5pisos == "2":
                            print("Te matan por detrás. Muy bien intentado pero a la siguiente lo conseguirás\n SIKEEEE L BOZO")
                    #base
                    elif eleccion4pisos == "2":
                        print("Has matado a 2 personas con tu gran base y quedan 3 personas en la partida pero viene la tormenta.")
                        pausar_juego()
                        print("Que quieres hacer?")
                        pausar_juego()
                        print("1)Moverte para estar a salvo de la tormenta")
                        pausar_juego()
                        print("Pelearte con un man")
                        pausar_juego()
                        eleccion5pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                        #mover
                        if eleccion5pisos == "1":
                            print("Te matan con un scar")
                        #pelear
                        elif eleccion5pisos == "2":
                            print("Matas a un pavo.")
                            pausar_juego()
                            print("QUEDA 1 PERSONA!!")
                            pausar_juego()
                            print("El personaje esta corriendo hacia la tormenta mientras tu estas en la misma posición que el.")
                            pausar_juego()
                            print("Que haces ahora?")
                            pausar_juego()
                            print("1)Pelear")
                            pausar_juego()
                            print("2)Ir hacia la tormenta y olvidarte del man")
                            pausar_juego()
                            eleccion6pisos = input("Ingrese el número de la opción que desea elegir:").lower()
                            #pelear
                            if eleccion6pisos == "pelear":
                                print("GANAS LA PARTIDA.")
                                pausar_juego()
                                print("GG.")
                                pausar_juego()
                                print("MUY EZZZZZ,NO?")
                                pausar_juego()
                                print("Espero verte por aqui de nuevo. ADIOS :)")
                                pausar_juego()
                                
                            #irte
                            elif eleccion6pisos == "irte":
                                print("Te matan por detrás")
                                pausar_juego()
                                print("Muy bien intentado pero a la siguiente lo conseguirás")
                                pausar_juego()
                                print("SIKEEEE L BOZO")
                                pausar_juego()

                    #atacar
                    elif eleccion4pisos == "3":
                        print("Te conviertes en NINJA y ganas la partida")
                        pausar_juego()
                        print("¡No te lo esperabas,eh!")


            #irte
            elif eleccion2pisos == "2":
                print("Te matan por tonto")     
        #pelear
        elif eleccion1pisos == "2":
            print("Mueres por GILIPOLLAS")
            pausar_juego()
            print("NO VUELVAS A JUGAR ERES MUY MALO")
    #Señorío de la Sal
    if mapa == "2":
        print("Has caido en Señorío de la Sal y tienes un buen loot pero ves a una persona en la casa de delante.")
        pausar_juego()
        print("¿Qué haces?")
        pausar_juego()
        print("1)Atacar")
        pausar_juego()
        print("2)Seguir looteando")
        pausar_juego
        eleccionseñorio = input("Ingrese el número de la opción que desea elegir:").lower()
        #atacar
        if eleccionseñorio == "1":
            print("Perdiste la batalla,eres muy malo")
        #loot
        elif eleccionseñorio == "2":
            print("¡Te has encontrado un scar!.")
            pausar_juego()
            print("¡Qué haces ahora?")
            pausar_juego()
            print("1)Ir hacia el centro de la tormenta y construir una base")
            pausar_juego()
            print("2)Buscar gente")
            pausar_juego()
            print("3)Campear")
            pausar_juego()
            eleccionseñorio1 = input("Ingrese el número de la opción que desea elegir:").lower()
            #base
            if eleccionseñorio1 == "1":
                print("Te matan de un snipazo.")
            #gente
            elif eleccionseñorio1 == "2":
                print("Matas a una persona con una scar y quedan 15 personas")
                pausar_juego()
                print("¿Qué haces ahora?")
                pausar_juego()
                print("1)Seguir buscando gente")
                pausar_juego()
                print("2)Base")        
                pausar_juego()    
                eleccionseñorio2 = input("Ingrese el número de la opción que desea elegir:").lower()
                #gente
                if eleccionseñorio2 == "1":
                    print("Pues no eres Ninja y te matan por gay")
                #base
                elif eleccionseñorio2 == "2":
                    print("No has matado a nadie pero calculaste mal la zona pero ves a un man corriendo.")
                    pausar_juego()
                    print("¿Qué haces ahora?")
                    pausar_juego()
                    print("1)Correr hacia la tormenta")
                    pausar_juego()
                    print("2)Pelear")
                    pausar_juego()
                    eleccionseñorio3 = input("Ingrese el número de la opción que desea elegir:").lower()
                    #tormenta
                    if eleccionseñorio3 == "1":
                        print("Te mantienes vivo pero ves a un tío viniendo hacia ti pero tienes una grieta para escaparte")
                        pausar_juego()
                        print("Qué haces ahora?")
                        pausar_juego()
                        print("1)Escaparte con la grieta")
                        pausar_juego()
                        print("2)Pelear")
                        pausar_juego()
                        eleccionseñorio4=input("Ingrese el número de la opción que desea elegir:").lower()
                        #grieta
                        if eleccionseñorio4 =="1":
                            print("Has conseguido escapar y quedan 6 personas.")
                            pausar_juego()
                            print("Qué haces ahora?")
                            pausar_juego()
                            print("1)Base")
                            pausar_juego()
                            print("2)Pelear")
                            pausar_juego()
                            eleccionseñorio5 = input("Ingrese el número de la opción que desea elegir:").lower()
                            #base
                            if eleccionseñorio5 == "1":
                                print("Has matado a un man con un snipazo de los tuyos")
                                pausar_juego()
                                print("Qué haces ahora?")
                                pausar_juego()
                                print("1)Ir a por el man")
                                pausar_juego()
                                print("2)Seguir en base")
                                pausar_juego()
                                eleccionseñorio6 = input("Ingrese el número de la opción que desea elegir:").lower()
                                #man
                                if eleccionseñorio6 == "1":
                                    print("Lo has matado con el subfusil y queda 1 persona.")
                                    pausar_juego()
                                    print("Qué haces ahora?")
                                    pausar_juego()
                                    print("1)Ir a por el tío")
                                    pausar_juego()
                                    print("2)Base")
                                    pausar_juego()
                                    eleccionseñorio7=input("Ingrese el número de la opción que desea elegir:").lower()
                                    #tío
                                    if eleccionseñorio7 == "1":
                                        print("GANAS LA PARTIDA Y PARA DE PADREAR QUE SE TE DA BIEN")
                                    #base
                                    elif eleccionseñorio7 =="2":
                                        print("Te rusea y pierdes el 1vs1")
                                #base
                                elif eleccionseñorio6 == "2":
                                    print("Te come la tormenta por tonto")
                            #pelear
                            elif eleccionseñorio5 =="2":
                                print("Matas a 1 persona pero te viene un tío por detrás y te mata")
                        #pelear
                        elif eleccionseñorio4 =="2":
                            print("Te han metido un escopetazo en la cabeza")
                    #pelear
                    elif eleccionseñorio3 == "2":
                        print("El tío era Clix mi pana.Mala suerte")
            #campear
            elif eleccionseñorio1 == "3":
                print("Te matan con una trampa por tonto")
    #chiringuito
    elif mapa == "3":
        print("Has looteado y ves a un tío pero viene la tormenta")
        pausar_juego()
        print("¿Qué quieres hacer?")
        pausar_juego()
        print("1)Atacar")
        pausar_juego()
        print("2)Correr hacia la tormenta")
        eleccionchiringuito1 = input("Ingrese el número de la opción que desea elegir:").lower()
        #atacar
        if eleccionchiringuito1 =="1":
            print("Lo matas y ya que estás en el punto.")
            pausar_juego()
            print("¿Qué quieres hacer?")
            pausar_juego()
            print("1)Base")
            pausar_juego()
            print("2)Campear")
            pausar_juego()
            print("3)Atacar")
            eleccionchiringuito2 = input("Ingrese el número de la opción que desea elegir:").lower()
            #base
            if eleccionchiringuito2 == "1":
                print("Es una partida muy aburrida y quedan 10 personas pero tienes que moverte y ves a un man")
                pausar_juego()
                print("¿Qué quieres hacer?")
                pausar_juego()
                print("1)Moverte y construir una base")
                pausar_juego()
                print("2)Matarlo")
                eleccionchiringuito3 = input("Ingrese el número de la opción que desea elegir:")
                #base
                if eleccionchiringuito3 =="1":
                    print("Como ibas muy atrasado pues te han matado de un snipazo desde una montaña")
                #matar
                elif eleccionchiringuito3 =="2":
                    print("Lo matas y llegas al punto sano")
                    pausar_juego()
                    print("¿Qué haces?")
                    pausar_juego()
                    print("1)Atacar")
                    pausar_juego()
                    print("2)Base")
                    eleccionchiringuito4 = input("Ingrese el número de la opción que desea elegir:")
                    #atacar
                    if eleccionchiringuito4 == "1":
                        print("No eres Clix")
                    #base
                    elif eleccionchiringuito4 == "2":
                        print("Has matado a un tío con el sniper y ves a un tío ruseandote pero es la última persona")
                        pausar_juego()
                        print("¿Qué haces?")
                        pausar_juego()
                        print("1)Escaparte")
                        pausar_juego()
                        print("2)Atacas")
                        eleccionchiringuito5 = input("Ingrese el número de la opción que desea elegir:").lower()
                        #escapar
                        if eleccionchiringuito5 == "1":
                            print("Te mata por detrás con un fusil de asalto")
                        #atacar
                        elif eleccionchiringuito5 == "2":
                            print("GANAS LA PARTIDA")
                            pausar_juego()
                            print("ESPERO VERTE PRONTO")
        

            #campear
            elif eleccionchiringuito2 == "2":
                print("Entras a una casa y te mata una trampa")
            #atacar
            elif eleccionchiringuito2 == "3":
                print("NO ERES NINJA")
        #tormenta
        elif eleccionchiringuito1 == "2":
            print("Te mató la tormenta por pelear con el man")
    elif mapa == "4":
        print("Ves a un tío en una casa")
        pausar_juego()
        print("¿Qué vas a hacer?")
        pausar_juego()
        print("1)Atacar")
        pausar_juego()
        print("2)Irte")
        eleccionaterrizaje1 = input("Ingrese el número de la opción que desea elegir:").lower()
        if eleccionaterrizaje1 == "1":
            print("Lo matas y te vas hacia el punto pero te encuentras a un man corriendo")
            pausar_juego()
            print("¿Qué haces?")
            pausar_juego()
            print("1)Atacar")
            pausar_juego()
            print("2)Irte")
            eleccionaterrizaje2 = input("Ingrese el número de la opción que desea elegir:").lower()
            if eleccionaterrizaje2 == "1":
                print("Lo matas pero te come la tormenta")
            elif eleccionaterrizaje2 == "2":
                print("Estás en el punto")
                pausar_juego()
                print("¿Qué quieres hacer?")
                pausar_juego()
                print("1)Base")
                pausar_juego()
                print("2)Campear")
                pausar_juego()
                print("3)Atacar")
                eleccionaterrizaje3 = input("Ingrese el número de la opción que desea elegir:").lower()
                if eleccionaterrizaje3 == "1":
                    print("Pues no encuentras a nadie y justo cuando te ibas a dormir te viene un tío")
                    pausar_juego()
                    print("¿Qué quieres hacer?")
                    pausar_juego()
                    print("1)Atacar")
                    pausar_juego()
                    print("2)Escaparte")
                    eleccionaterrizaje4 = input("Ingrese el número de la opción que desea elegir:").lower()
                    if eleccionaterrizaje4 == "1":
                        print("Lo matas y como no ves a nadie pues por la cara quedan 2 personas y los ves peleandose")
                        pausar_juego()
                        print("¿Qué haces ahora?")
                        pausar_juego()
                        print("1)Meterte en pelea")
                        pausar_juego()
                        print("2)Esperar a que acabe la batalla")
                        eleccionaterrizaje5 = input("Ingrese el número de la opción que desea elegir:").lower()
                        if eleccionaterrizaje5 == "1":
                            print("Te matan por tonto")
                        elif eleccionaterrizaje5 == "2":
                            print("Eres el más listo de la clase y lo matas con un fusil de asalto")
                            pausar_juego()
                            print("MUY EZZZ NO?")

                elif eleccionaterrizaje3 == "2":
                    print("Te mata una trampa al entrar a la casa")
                elif eleccionaterrizaje3 == "3":
                    print("NO ERES NINJA")
        elif eleccionaterrizaje1 == "2":
            print("TE MATA A TI POR MARICÓN")
                

#Matemáticas
elif eleccion =="mates":
    import random
    def genera_numero(a, b):
        numero = random.randint(a, b)
        return numero

    ejecucion = True

    while ejecucion:
        operaciontipo=input("¿Qué desee?.\n-Sumar\n-Restar\n-Multiplicar\n-Dividir\\\nSi desee salir pulsa la tecla 0 ").lower()
        if operaciontipo == "sumar":
            numero1 = genera_numero(1, 1000)
            numero2 = genera_numero(1,1000)
            print(f"Dime el resultado de: {numero1} + {numero2}")
            resultado = int(input("Introduce un resultado: "))
            if resultado == numero1 + numero2:
                print("Correcto")
            else:
                print("Falso")
            

        elif operaciontipo == "restar":
            print(f"Dime el resultado de:{genera_numero(1, 1000)} - {genera_numero(1,1000)}")

        elif operaciontipo == "multiplicar":
            print(f"Dime el resultado de:{genera_numero(1, 100)} * {genera_numero(1,1000)}")

        elif operaciontipo == "dividir":
            print(f"Dime el resultado de:{genera_numero(1, 100)} / {genera_numero(1,1000)}")
        elif operaciontipo == "0":
            ejecucion = False

        else:
            operaciontipo=("No existe ese tipo de operación")
        

            
#Adivina el número
elif eleccion == "adivinaelnumero":
    print("Pues preparate porque esto no es un juego.Este juego consiste en adivinar el número del 1 al 100.")
    import random
    numero = random.randint(1,50)
    respuesta = ...
    print("¡Adivina el numero que estoy pensando ahora mismo!")

    while numero != respuesta:
        respuesta = int(input("Indroduce un numero entre 1 y 100:"))
        if respuesta > numero:
            print("Introduce un numero menor:")
        elif respuesta < numero:
            print("Introduce un numero mayor:")
        else:
            print("Has acertado!")