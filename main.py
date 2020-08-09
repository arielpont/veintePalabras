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
            
            # para abrir archivos suele ser mejor WITH porque abre y cierra automaticamente.
            # es importante SIEMPRE indicar el ENCODING="UTF-8". Esto soluciona los problemas de caracteres con tildes y ñ por ejemplo.
            # por convenciones siempre se usa la variable "f" para abrir archivos con WITH
            with open("dist/history.txt", "r", encoding="utf-8") as f:
                historyPrint = f.read()
                listsplit = historyPrint.split()

                # @marian te animas a hacer la siguiente linea de código con un for?
                new_list = "".join(listsplit[-20]+" "+listsplit[-19]+" "+listsplit[-18]+" "+listsplit[-17]+" "+listsplit[-16]+" "+listsplit[-15]+" "+listsplit[-14]+" "+listsplit[-13]+" "+listsplit[-12]+" "+listsplit[-11]+" "+listsplit[-10]+" "+listsplit[-9]+" "+listsplit[-8]+" "+listsplit[-7]+" "+listsplit[-6]+" "+listsplit[-5]+" "+listsplit[-4]+" "+listsplit[-3]+" "+listsplit[-2]+" "+listsplit[-1])
                
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
        elif optionSelected == 4:
            clear()
            print(f"{Bcolors.FAIL}¡Adiós!{Bcolors.ENDC}\n")
            exit()

        else:
            clear()
            print(f"{Bcolors.FAIL}Por favor, selecciona una opción válida.{Bcolors.ENDC}\n")
