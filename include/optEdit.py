
try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

def play():
    print(f"Hola {Bcolors.OKGREEN}{settings.player.getUserName()} {settings.player.getUserSername()}{Bcolors.ENDC}, ¿estás seguro que queres editar tu parte de la historia?")
    print(f"Tu último ingreso fue:\n{Bcolors.OKGREEN}{settings.history.getNewPartHistory()}{Bcolors.ENDC}\n")