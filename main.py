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

#libreria para reproducir sonidos
#try:
    #from playsound import playsound
#except:
    #print("ImportError: el módulo 'playsound' no se ha podido importar.")

################
##### MAIN #####
################

if __name__ == "__main__":
    # hago sonar un wav
    # playsound("audio/bienvenido.wav", False)
    
    clear()
    while True:
        #1. Continuar la historia
        #2. Leer últimas 20 palabras de la historia
        #3. Editar mí último ingreso
        #4. Salir
        options = (
            'Continuar la historia.',
            f'Leer últimas 20 palabras de la historia {Bcolors.FAIL}(en desarrollo).{Bcolors.ENDC}',
            f'Editar mí último ingreso.',
            'Salir.'
        )

        showOptions(options)
        optionSelected = selectOption(options)
        print("\n")

        #option 1
        if optionSelected == 1:
            clear()

            try:
                import include.optContinue as optContinue
                optContinue.play()
            except ImportError:
                print("ImportError: el módulo 'optContinue' no se ha podido importar.")

        #option 2
        elif optionSelected == 2:

            clear()
            print("Usted leerá las últimas veinte palabras escritas... esperamos le resulten inspiradoras\n")
            
            from include.history import HISTORY_PATH
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                historyPrint = f.read()
                listsplit = historyPrint.split()

                # @marian te animas a hacer la siguiente linea de código con un for?
                new_list = " ".join(listsplit[-20:])
                print(f"{new_list}\n")
            

        #option 3
        elif optionSelected == 3:
            clear()

            #chequeo si están definidos los objetos globales "player" y "history"
            if settings.player and settings.history is not None:
                try:
                    import include.optEdit as optEdit
                    optEdit.play()
                except ImportError:
                    print("ImportError: el módulo 'optEdit' no se ha podido importar.")
            else:
                print(f"{Bcolors.FAIL}No puedes editar aún porque no has añadido nada a la historia.{Bcolors.ENDC}\n")

        #option 4
        else:
            clear()
            print(f"{Bcolors.FAIL}¡Adiós!{Bcolors.ENDC}\n")
            exit()
