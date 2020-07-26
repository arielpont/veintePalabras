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
    #si el usuario aún no añadió nada a la historia no puede editar.
    if settings.history.getNewPartHistory() != "":

        #muestro el último ingreso o edición del usuario
        print(f"Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, tu último ingreso fue:\n{Bcolors.OKGREEN}{settings.history.getNewPartHistory()}{Bcolors.ENDC}\n")
        
        #le preguntamos si está seguro de proseguir con la edición
        if confirm(f"{Bcolors.OKGREEN}¿Estás seguro que queres editar tu parte de la historia?{Bcolors.ENDC}\n{Bcolors.FAIL}Esta opción sobreescribirá tu último ingreso.{Bcolors.ENDC}"):
            print(f"{Bcolors.HEADER}{settings.player.getUserName()} {settings.player.getUserSername()}, lo que escribas a continuación sobreescribirá tu último ingreso: {Bcolors.ENDC}")

            clear()
            #actualizo solo sí el usuario añadió algo distinto a ""
            if settings.history.updateNewPartHistory():
                print(f"Tu historia a sido editada: {Bcolors.OKBLUE}{settings.history.getFullHistory()}{Bcolors.ENDC}\n")
            else:
                print(f"{Bcolors.FAIL}No haz escrito nada nuevo, se conservará tu ingreso anterior.\n{Bcolors.ENDC}")
        else:
            clear()
    else:
        print(f"{Bcolors.FAIL}No hay nada para editar porque no has continuado la historia.\n{Bcolors.ENDC}")
      
    