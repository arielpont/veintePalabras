try:
    import os
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    os = None

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

#####################
##### FUNCIONES #####
#####################

def clear(): 
    #windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    #mac and linux
    else: 
        _ = os.system("clear")

def printError(msg):
    print(f"{Bcolors.CREDBG}  {msg}  {Bcolors.ENDC}\n")

# imprime una lista de opciones (list or tuple)
def showOptions(options):
    """ Imprime en pantalla una LIST o TUPLE """

    if options != [] or options != () and type(options) is list or type(options) is tuple:
        
        print(f"{Bcolors.HEADER}{Bcolors.BOLD}#  Menu{Bcolors.ENDC}")
        count = 1
        for option in options:
            print(f"{Bcolors.OKGREEN}{str(count)}.{Bcolors.ENDC} {option}")
            count += 1
    else:
        pass

# ingresar números enteros
def selectOption(options):
    """ Permite ingresar números enteros. Como argumento recibe una LIST or TUPLE """

    while True:
        try:
            userInput = int(input(f"\n{Bcolors.OKGREEN}Ingrese el número de la opción que deseé: {Bcolors.ENDC}"))

            if userInput <= len(options):
               break 
            else:
                clear()
                printError("Por favor, selecciona una opción válida.")
                showOptions(options)
                continue

        except ValueError:
            clear()
            printError("Ustede no ingresó un número, por favor vuelva a intentarlo.")
            showOptions(options)
            continue
        else:
            printError("Hubo un error. Vuelva a ingresar un número válido.")
            continue

    return userInput

# confirmar YES o NO
def confirm(msg):
    while True:
        userInput = str(input(f"{msg}\n[Y/N]: "))

        if userInput.lower() in ('y', 'yes'):
            return True
        elif userInput.lower() in ('n', 'no'):
            return False
        else:
            print(f"{Bcolors.FAIL}Ustede no ingresó una opción válida, por favor vuelva a intentarlo.{Bcolors.ENDC}\n")
            continue

# max 20 words lenght
def maxLen20(msg):
    if len(msg.split()) <= 20:
        return True
    else:
        print(f"{Bcolors.FAIL}Su ingreso sobrepasa el límite máximo de 20 palabras. Vuelva a intentarlo.{Bcolors.ENDC}\n")
        return False
