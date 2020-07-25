##################
##### IMPORT #####
##################

try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import clear, showOptions, selectOption
except ImportError:
    print("ImportError: el módulo 'functions' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

try:
    import time
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    time = None

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

        #option 1
        if optionSelected == 1:
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")

            try:
                import include.optContinue as optContinue
                optContinue.play()
            except ImportError:
                print("ImportError: el módulo 'optContinue' no se ha podido importar.")

        #option 2
        elif optionSelected == 2:
            #marian hace la opción 2
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")

        #option 3
        elif optionSelected == 3:
            clear()
            print(f"{Bcolors.OKGREEN}Elegista la opción: {Bcolors.ENDC} {options[optionSelected - 1]}\n")

            #chequeo si están definidos los objetos globales "player" y "history"
            if settings.player and settings.history is not None:
                try:
                    import include.optEdit as optEdit
                    optEdit.play()
                except ImportError:
                    print("ImportError: el módulo 'optEdit' no se ha podido importar.")
            else:
                print(f"{Bcolors.FAIL}Debes ingresar tu parte de la historia para poder editarla.{Bcolors.ENDC}\n")

        #option 4
        elif optionSelected == 4:
            clear()
            print(f"{Bcolors.FAIL}¡Adiós!{Bcolors.ENDC}\n")
            exit()

        else:
            clear()
            print(f"{Bcolors.FAIL}Por favor, selecciona una opción válida.{Bcolors.ENDC}\n")
