class Nodo:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no


def construir_arbol():
    # se construye un arbol
    raiz = Nodo("¿Es un animal?")
    # si el usuario elije si, se ira para on lado
    raiz.si = Nodo("¿Tiene cuatro patas?",
                   Nodo("¿Tiene cola?",
                        Nodo("¿Es doméstico?", Nodo("Perro"), Nodo("León")),
                        Nodo("¿Vuela?", Nodo("Ardilla"), Nodo("Canguro"))),
                   Nodo("¿Tiene plumas?",
                        Nodo("¿Vuela?", Nodo("Águila"), Nodo("Pato")),
                        Nodo("¿Es acuático?", Nodo("Tiburón"), Nodo("Cebra"))))
    # aqui si el usuario elije no, se ira apra el otro lado
    raiz.no = Nodo("¿Es un objeto?",
                   Nodo("¿Se usa para escribir?",
                        Nodo("¿Escribe en papel?", Nodo("Lápiz"), Nodo("Teclado")),
                        Nodo("¿Se usa para cocinar?", Nodo("Taza"), Nodo("Cuchillo"))),
                   Nodo("¿Es un superhéroe?",
                        Nodo("¿Vuela?", Nodo("Superman"), Nodo("Batman")),
                        Nodo("¿Tiene superpoderes?", Nodo("Spiderman"), Nodo("Ironman"))))
    return raiz


def adivinar(nodo):
    # en esta parte adivina lo que el usuario piensa vasado en lo que el elija
    respuesta = input(nodo.pregunta + " (si/no): ").lower()
    if respuesta == "si":
        if nodo.si is not None:
            adivinar(nodo.si)
        else:
            print("¡Adiviné que es un " + nodo.pregunta + "!")
    elif respuesta == "no":
        if nodo.no is not None:
            adivinar(nodo.no)
        else:
            print("¡Adiviné que es un " + nodo.pregunta + "!")
    else:
        print("Respuesta no válida. Por favor, responde 'si' o 'no'.")


def jugar_nuevamente():
    return input("¿Quieres jugar nuevamente? (si/no): ").lower() == "si"


raiz = construir_arbol()
while True:
    print("Piensa en un objeto, animal o personaje, y yo intentaré adivinarlo.")
    adivinar(raiz)
    respuesta = input("¿Era eso en lo que estabas pensando? (si/no): ").lower()
    if respuesta == "si":
        print("¡Genial! He adivinado correctamente XD, enlo que piensas, e ganado yo.")
    else:
        nuevo_objeto = input("¿En qué estabas pensando? :3 ")
        print("¡Oh, con que era eso en lo que estabas pensando! haz ganado tu esta vez pero para la próxima vez adivinaré en lo que piensas.")
    if not jugar_nuevamente():
        print("¡Gracias por jugar! Hasta la próxima ves.")
        break


