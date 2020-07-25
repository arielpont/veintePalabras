try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

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

try:
    import time
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    time = None

#ejecuto
def play():
    #creación de la instancia de la clase User()
    
    settings.player = User()

    #seteo del nombre y apellido del usuario
    settings.player.setUserName(str(input("Hola, ingrese su nombre: ")))
    settings.player.setUserSername(str(input(f"Muy bien {Bcolors.OKGREEN}{settings.player.getUserName()}{Bcolors.ENDC}, ahora ingrese su apellido: ")))
    settings.player.setUserEmail(str(input(f"Genial {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, por último ingrese su email: ")))
    print(f"Ahora sí, es un gusto tenerlo aquí {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}, {settings.player.getUserEmail()}.{Bcolors.ENDC}\n")

    print(f"{Bcolors.FAIL}El horario de su registro es: {settings.player.getUserLoginTime()}{Bcolors.ENDC}")

    #creación de la instancia History()
    settings.history = History()
    print(f"{Bcolors.HEADER}Es momento de continuar la historia {settings.player.getUserName()} {settings.player.getUserSername()}:{Bcolors.ENDC}")
    settings.history.setNewPartHistory(input(f"{Bcolors.OKGREEN}...{str(settings.history.getLastPartHistory())}{Bcolors.ENDC} "))

    clear()

    if settings.history.saveNewPartHistory():
        print("Tu historia a sido guardada: ")
        print(f"\n{Bcolors.OKBLUE}{settings.history.getFullHistory()}{Bcolors.ENDC}")
    else:
        print(f"{Bcolors.FAIL}No se ha añadido nada nuevo a la historia.{Bcolors.ENDC}")

    print(f"\nMuy bien {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, ahora es momento de que esta historia siga creciendo.\nCompartí este programa con quien quieras que continue escribiendo la historia.\n\n")