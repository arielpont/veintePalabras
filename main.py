##################
##### IMPORT #####
##################

try:
    import sys
    import os
    import glob
    import time
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    sys = None
    os = None
    glob = None
    time = None

#importación de las clases
try:
    from include.user import User
except ImportError:
    print("ImportError: el módulo 'User' no se ha podido importar.")

try:
    from include.history import History
except ImportError:
    print("ImportError: el módulo 'History' no se ha podido importar.")

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
            
################
##### MAIN #####
################

if __name__ == "__main__":
    clear()

    while True:

        #1. Continuar la historia
        #2. Leer últimas 20 palabras de la historia
        #3. Editar mí último ingreso
        #4. Salir
        options = (
            'Continuar la historia.',
            f'Leer últimas 20 palabras de la historia {Bcolors.FAIL}(en desarrollo).{Bcolors.ENDC}',
            f'Editar mí último ingreso {Bcolors.FAIL}(en desarrollo).{Bcolors.ENDC}',
            'Salir.'
        )

        showOptions(options)

        optionSelected = selectOption(options)

        print("\n")

        if optionSelected == 1:
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")

            #creación de la instancia de la clase User()
            player = User()

            #seteo del nombre y apellido del usuario
            player.setUserName(str(input("Hola, ingrese su nombre: ")))
            player.setUserSername(str(input(f"Muy bien {Bcolors.OKGREEN}{player.getUserName()}{Bcolors.ENDC}, ahora ingrese su apellido: ")))
            player.setUserEmail(str(input(f"Genial {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}{Bcolors.ENDC}, por último ingrese su email: ")))
            print(f"Ahora sí, es un gusto tenerlo aquí {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}, {player.getUserEmail()}.{Bcolors.ENDC}")
            
            print("\n")
            print(f"{Bcolors.FAIL}El horario de su registro es: {player.getUserLoginTime()}{Bcolors.ENDC}")

            #delay de 2 segundos
            time.sleep(2)
            clear()

            #creación de la instancia History()
            history = History()
            print(f"{Bcolors.HEADER}Es momento de continuar la historia {player.getUserName()} {player.getUserSername()}:{Bcolors.ENDC}")
            history.setNewPartHistory(input(f"{Bcolors.OKGREEN}...{str(history.getLastPartHistory())} {Bcolors.ENDC} "))
            
            #delay de 2 segundos
            time.sleep(1)
            clear()

            if history.saveNewPartHistory():
                print("Tu historia a sido guardada: ")
                print(f"\n{Bcolors.OKBLUE}{history.getFullHistory()}{Bcolors.ENDC}")
            else:
                print(f"{Bcolors.FAIL}No se ha añadido nada nuevo a la historia.{Bcolors.ENDC}")

            print(f"\nMuy bien {Bcolors.OKGREEN}{player.getUserName()} {player.getUserSername()}{Bcolors.ENDC}, ahora es momento de que esta historia siga creciendo.\nCompartí este programa con quien quieras que continue escribiendo la historia.\n\n")
            time.sleep(1)

        elif optionSelected == 2:
            #marian hace la opción 2
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")
        elif optionSelected == 3:
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")
        elif optionSelected == 4:
            clear()
            print(f"{Bcolors.FAIL}¡Adiós!{Bcolors.ENDC}\n")
            exit()
        else:
            clear()
            print(f"{Bcolors.FAIL}Por favor, selecciona una opción válida.{Bcolors.ENDC}\n")
