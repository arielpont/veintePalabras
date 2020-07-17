try:
    import sys
    import os
    import glob
    import time
except ImportError:
    sys = None
    os = None
    glob = None
    time = None

#importación de las clases
from include.user import User
from include.history import History
from include.bcolor import Bcolors

#funciones
def clear(): 
    #windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    #mac and linux
    else: 
        _ = os.system("clear")

if __name__ == "__main__":
    clear()
    
    #creación de la instancia de la clase User()
    player = User()

    #seteo del nombre y apellido del usuario
    player.setUserName(input("Hola, ingresa tu nombre: "))
    player.setUserSername(input(f"Muy bien {player.getUserName()}, ahora ingresa tu apellido: "))
<<<<<<< HEAD
    print(f"{Bcolors.OKGREEN}Un gusto tenerte aquí {player.getUserName()} {player.getUserSername()}.")
    print(player.getUserLogin())
=======
    player.setUserEmail(input(f"Genial {player.getUserName()}, por último ingresá tu email: "))
    print(f"{Bcolors.OKGREEN}Ahora sí, es un gusto tenerte aquí {player.getUserName()} {player.getUserSername()}, {player.getUserEmail()}.")
    print(player.getUserLoginTime())
>>>>>>> 8c88908a80deed98eb1b1351a93179eda1426d17

    #delay de 2 segundos
    time.sleep(2)
    clear()

    #creación de la instancia History()
    history = History()
    print(f"{Bcolors.HEADER}Es momento de continuar la historia {player.getUserName()} {player.getUserSername()}:")
    history.setNewPartHistory(input(f"{Bcolors.OKGREEN}{Bcolors.BOLD}..." + str(history.getLastPartHistory()) + "\n"))
    
    #delay de 2 segundos
    time.sleep(2)
    clear()

    if history.saveNewPartHistory():
        print("Tu historia a sido guardada: ")
        print(f"{Bcolors.UNDERLINE}" + "\n" + history.getFullHistory())
    else:
        print("No se ha añadido nada nuevo a la historia.")

    print(f"{Bcolors.HEADER}" + "\nMuy bien " + player.getUserName() + " " + player.getUserSername() + ", ahora es momento de que esta historia siga viajando.\nCompartí este programa con quien quieras para que continue la historia.\n\n")
    time.sleep(2)

    #filePath = input("Ingrese la ruta: ")
    #fileName = input("Ingrese el nombre del archivo y su extensión: ")
    
    #if os.path.exists("content/history.txt"):
        #pass



    #Si no existe historia, comenzar una

    #Si ya existe una historia, debo seguirla
        #Traer las últimas palabras con un máximo de 20 palabras
        #Continuar la historia usando hasta 20 palabras máximo.
        #Guardarla
            #Si sos la última persona te muestro la historia completa

            #Si quedan fragmento por completar, imprimo indicación de reenviar este programa.

    #Si la historia ya está terminada porque participaron 7 persona, la imprimo completa.
