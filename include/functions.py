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

#imprime una lista de opciones (list or tuple)
def showOptions(options):
    if options != "" and type(options) is list or type(options) is tuple:
        count = 1
        for option in options:
            print(f"{str(count)}. {option}")
            count += 1
    else:
        pass


#ingresar números enteros
def selectOption(options):
    while True:
        try:
            userInput = int(input(f"\n{Bcolors.OKGREEN}Ingrese el número de la opción que deseé: {Bcolors.ENDC}"))      
        except ValueError:
            clear()
            print(f"{Bcolors.FAIL}Ustede no ingresó un número, por favor vuelva a intentarlo.{Bcolors.ENDC}\n")
            showOptions(options)
            continue
        else:
            break
    
    return userInput