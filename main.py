try:
    import sys, os, glob, pytz
except ImportError:
    sys = None
    os = None
    glob = None
    pytz = None

#importamos las clases
from include.user import User
from include.history import History
from include.bcolor import Bcolors

#funciones
def clear(): 
    #windows 
    if __name__ == "nt": 
        _ = os.system("cls") 
    #mac and linux
    else: 
        _ = os.system("clear")

if __name__ == "__main__":
    clear()
    
    #creamos una instancia de la clase User()
    player = User()

    #setiamos el nombre y apellido del usuario
    player.setUserName(input("Hola, ingresa tu nombre: "))
    player.setUserSername(input(f"Muy bien {player.getUserName()}, ahora ingresa tu apellido: "))
    print(f"{Bcolors.OKGREEN}Ahora sí, es un gusto tenerte aquí {player.getUserName()} {player.getUserSername()}.")
    print(player.getUserLogin())

    history = History()
    print(history.getHistory())

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
