try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import clear, maxLen20
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
    settings.player.setUserName(str(input(f"Hola, ingrese su nombre: {Bcolors.OKGREEN}")))
    settings.player.setUserSername(str(input(f"{Bcolors.ENDC}Muy bien {Bcolors.OKGREEN}{settings.player.getUserName()}{Bcolors.ENDC}, ahora ingrese su apellido: {Bcolors.OKGREEN}")))
    settings.player.setUserEmail(str(input(f"{Bcolors.ENDC}Genial {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, por último ingrese su email: {Bcolors.OKGREEN}")))
    
    clear()
    print(f"{Bcolors.ENDC}Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}, {settings.player.getUserEmail()}.{Bcolors.ENDC}")
    print(f"El horario de su registro es: {Bcolors.FAIL}{settings.player.getUserLoginTime()}{Bcolors.ENDC}\n")

    #creación de la instancia History()
    settings.history = History()
    print(f"{Bcolors.HEADER}Es momento de continuar la historia: {Bcolors.ENDC}")
    
    #el usuario debe ingresar algo menor a igual a 20 palabras
    while True:
        new = input(f"...{str(settings.history.getLastPartHistory())} {Bcolors.OKGREEN}")

        if maxLen20(new):
            settings.history.setNewPartHistory(new)
            break
        else:
            continue

    clear()

    if settings.history.saveNewPartHistory():
        print(f"{Bcolors.ENDC}Tu historia a sido guardada: ")
        print(f"\n{Bcolors.OKBLUE}{settings.history.getFullHistory()}{Bcolors.ENDC}")
    else:
        print(f"{Bcolors.FAIL}No se ha añadido nada nuevo a la historia.{Bcolors.ENDC}")

    print(f"\nMuy bien {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, ahora es momento de que esta historia siga creciendo.\nCompartí este programa con quien quieras que continue escribiendo la historia.\n")