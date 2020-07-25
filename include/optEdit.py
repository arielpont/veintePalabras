try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import confirm, clear
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

def play():

    if settings.history.getNewPartHistory() != "":

        print(f"Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, Tu último ingreso fue:\n{Bcolors.OKGREEN}{settings.history.getNewPartHistory()}{Bcolors.ENDC}\n")
        
        if confirm("¿Estás seguro que queres editar tu parte de la historia?"):
            print(f"{Bcolors.HEADER}{settings.player.getUserName()} {settings.player.getUserSername()}, lo que escribas a continuación sobreescribirá tu último ingreso. Si te arrepientes puedes no ingresar nada y presionar ENTER para omitir la edición de tu último ingreso: {Bcolors.ENDC}")

            clear()

            if settings.history.updateNewPartHistory(input(f"{Bcolors.OKGREEN}...{str(settings.history.getLastPartHistory())}{Bcolors.ENDC} ")):
                print("Tu historia a sido editada: ")
                print(f"\n{Bcolors.OKBLUE}{settings.history.getFullHistory()}{Bcolors.ENDC}")
            else:
                print(f"{Bcolors.FAIL}No haz escrito nada nuevo, se conservará tu ingreso anterior.\n{Bcolors.ENDC}")
        else:
            clear()
    else:
        print(f"{Bcolors.FAIL}No puedes editar porque no has ingresado nada nuevo a la historia.\n{Bcolors.ENDC}")
      
    