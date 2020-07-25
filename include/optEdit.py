try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import confirm
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

def play():
    print(f"Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, Tu último ingreso fue:\n{Bcolors.OKGREEN}{settings.history.getNewPartHistory()}{Bcolors.ENDC}\n")
    
    if confirm("¿Estás seguro que queres editar tu parte de la historia?"):
        print("YES")
    else:
        print("NO")
      
    