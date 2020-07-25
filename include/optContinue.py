try:
    import time
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    time = None

try:
    from include.functions import clear
except ImportError:
    print("ImportError: el módulo 'functions' no se ha podido importar.")

#importar clases
try:
    from include.user import User
except ImportError:
    print("ImportError: el módulo 'User' no se ha podido importar.")
    user = None

try:
    from include.history import History
except ImportError:
    print("ImportError: el módulo 'History' no se ha podido importar.")
    history = None

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")
    bcolor = None

#ejecuto
def play():
    #creación de la instancia de la clase User()
    player = User()

    #seteo del nombre y apellido del usuario
    player.setUserName(str(input("Hola, ingrese su nombre: ")))
    player.setUserSername(str(input(f"Muy bien {Bcolors.OKGREEN}{player.getUserName()}{Bcolors.ENDC}, ahora ingrese su apellido: ")))
    player.setUserEmail(str(input(f"Genial {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}{Bcolors.ENDC}, por último ingrese su email: ")))
    print(f"Ahora sí, es un gusto tenerlo aquí {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}, {player.getUserEmail()}.{Bcolors.ENDC}\n")

    print(f"{Bcolors.FAIL}El horario de su registro es: {player.getUserLoginTime()}{Bcolors.ENDC}")

    #delay de 2 segundos
    time.sleep(2)
    clear()

    #creación de la instancia History()
    history = History()
    print(f"{Bcolors.HEADER}Es momento de continuar la historia {player.getUserName()} {player.getUserSername()}:{Bcolors.ENDC}")
    history.setNewPartHistory(input(f"{Bcolors.OKGREEN}...{str(history.getLastPartHistory())} {Bcolors.ENDC} "))

    #delay de 2 segundos
    time.sleep(2)
    clear()

    if history.saveNewPartHistory():
        print("Tu historia a sido guardada: ")
        print(f"\n{Bcolors.OKBLUE}{history.getFullHistory()}{Bcolors.ENDC}")
    else:
        print(f"{Bcolors.FAIL}No se ha añadido nada nuevo a la historia.{Bcolors.ENDC}")

    print(f"\nMuy bien {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}{Bcolors.ENDC}, ahora es momento de que esta historia siga creciendo.\nCompartí este programa con quien quieras que continue escribiendo la historia.\n\n")
    time.sleep(2)