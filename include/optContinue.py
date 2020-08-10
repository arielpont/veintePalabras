try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import clear, maxLen20, printError
except ImportError:
    print("ImportError: el módulo 'functions' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

#ejecuto
def play():
    # importo clase User()
    try:
        from include.user import User
    except ImportError:
        print("ImportError: el módulo 'User' no se ha podido importar.")

    # creación de la instancia de la clase User()
    settings.player = User()

    # seteo del nombre y apellido del usuario
    settings.player.setUserName(str(input(f"Hola, ingrese su nombre: {Bcolors.OKGREEN}")))
    settings.player.setUserSername(str(input(f"{Bcolors.ENDC}Muy bien {Bcolors.OKGREEN}{settings.player.getUserName()}{Bcolors.ENDC}, ahora ingrese su apellido: {Bcolors.OKGREEN}")))
    settings.player.setUserEmail(str(input(f"{Bcolors.ENDC}Genial {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, por último ingrese su email: {Bcolors.OKGREEN}")))
    
    clear()
    print(f"{Bcolors.ENDC}Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}, {settings.player.getUserEmail()}.{Bcolors.ENDC}")
    print(f"El horario de su registro es: {Bcolors.OKGREEN}{settings.player.getUserLoginTime()}{Bcolors.ENDC}\n")

    # importo clase History()
    try:
        from include.history import History
    except ImportError:
        print("ImportError: el módulo 'History' no se ha podido importar.")

    # creación de la instancia History()
    settings.history = History()
    print(f"{Bcolors.HEADER}Es momento de continuar la historia: {Bcolors.ENDC}")
    
    # el usuario debe ingresar algo menor a igual a 20 palabras
    while True:
        new = input(f"...{str(settings.history.getLastPartHistory())} {Bcolors.OKGREEN}")

        if maxLen20(new):
            settings.history.setNewPartHistory(new)
            break
        else:
            continue

    clear()

    if settings.history.saveNewPartHistory():
        print(f"{Bcolors.ENDC}Tu historia a sido guardada:")
        print(f"\n{Bcolors.OKBLUE}{settings.history.getFullHistory()}{Bcolors.ENDC}")
    else:
        printError("No se ha añadido nada nuevo a la historia.")

    print(f"\nMuy bien {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, ahora es momento de que esta historia siga creciendo.\nCompartí este programa con quien quieras que continue escribiendo la historia.\n")