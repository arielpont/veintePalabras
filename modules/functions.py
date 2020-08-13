# Standard library imports
import os
# Third party imports
# Local application imports
from modules.bcolor import Bcolors

def confirm(msg):
    """ Return True if user write 'yes' or 'y' and False 'no' or 'n' (not sensible). """

    while True:
        userInput = str(input(f"{msg}\n[YES/NO]: {Bcolors.OKGREEN}"))
        print(f"{Bcolors.ENDC}")

        if userInput.lower() in ('y', 'yes'):
            return True
        elif userInput.lower() in ('n', 'no'):
            return False
        else:
            print_error("Ustede no ingresó una opción válida, por favor vuelva a intentarlo.")
            continue

def clear():
    """ Clean the console in all OS. """

    #windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    #mac and linux
    else: 
        _ = os.system("clear")

def print_error(msg):
    """ Print with style an error messagge. """

    print(f"\n{Bcolors.CREDBG}  {msg}  {Bcolors.ENDC}")
    input(f"{Bcolors.FAIL}-> Presiona ENTER para continuar{Bcolors.ENDC}\n")
    clear()

def select_option(options):
    """ Argument is an LIST or TUPLE. Return a index valid INT. """

    while True:
        try:
            userInput = int(input(f"\n{Bcolors.OKGREEN}Ingrese el número de la opción que deseé: {Bcolors.ENDC}"))

            if userInput <= len(options) and userInput > 0:
                break
            else:
                clear()
                print_error("Por favor, selecciona una opción válida.")
                show_options(options)
                continue

        except ValueError:
            clear()
            print_error("Ustede no ingresó un número, por favor vuelva a intentarlo.")
            show_options(options)
            continue
        else:
            print_error("Hubo un error. Vuelva a ingresar un número válido.")
            continue

    return userInput

def show_options(options):
    """ Print a LIST or TUPLE and add numbers at the begin of each option. """

    if options != [] and options != () and (type(options) is list or type(options) is tuple):
        print(f"{Bcolors.HEADER}{Bcolors.BOLD}#  Menu{Bcolors.ENDC}")
        count = 1
        for option in options:
            print(f"{Bcolors.OKGREEN}{str(count)}.{Bcolors.ENDC} {option[0]}")
            count += 1
    else:
        pass
