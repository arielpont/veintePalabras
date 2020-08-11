# Standard library imports
import os
from time import sleep
# Third party imports
# Local application imports
from modules.bcolor import Bcolors

def clear(): 
    #windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    #mac and linux
    else: 
        _ = os.system("clear")

def printError(msg):
    print(f"\n{Bcolors.CREDBG}  {msg}  {Bcolors.ENDC}")
    input(f"{Bcolors.FAIL}-> Presiona ENTER para continuar{Bcolors.ENDC}\n")
    clear()

# imprime una lista de opciones (list or tuple)
def showOptions(options):
    """ Imprime en pantalla un LIST o TUPLE """

    if options != [] and options != () and (type(options) is list or type(options) is tuple):
        print(f"{Bcolors.HEADER}{Bcolors.BOLD}#  Menu{Bcolors.ENDC}")
        count = 1
        for option in options:
            print(f"{Bcolors.OKGREEN}{str(count)}.{Bcolors.ENDC} {option[0]}")
            count += 1
    else:
        pass

# ingresar números enteros
def selectOption(options):
    """ Devuelve un INT """

    while True:
        try:
            userInput = int(input(f"\n{Bcolors.OKGREEN}Ingrese el número de la opción que deseé: {Bcolors.ENDC}"))

            if userInput <= len(options) and userInput > 0:
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
