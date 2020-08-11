# Standard library imports
# Third party imports
# Local application imports
from modules.bcolor import Bcolors
from modules.functions import clear, printError, showOptions, selectOption
import modules.history as history

if __name__ == "__main__":
    clear()

    # init instance History()
    htr = history.History()

    # if existe una historia
        # continuar la historia
            # editar mi ingreso
            # ver nuevamente la historia
            # salir
    # else iniciar una historia
        # necesito inspiración
            # imagenes
            # musica
            # estoy listo para empezar
        # estoy listo para empezar

    # check if an history already exists
    if(htr.exists()):
        while True:
            clear()
            print(f"{Bcolors.HEADER}Es momento de continuar la historia: {Bcolors.ENDC}\n")
            new_part = input(f"{htr.get_full()} {Bcolors.OKGREEN}")
            
            if htr.add_new_part(new_part):
                clear()
                print(f"{Bcolors.ENDC}Tu historia a sido guardada: {Bcolors.OKBLUE}{htr.get_full()}{Bcolors.ENDC}\n")
                break
            else:
                continue
    else:
        # iniciar la historia
        htr.begin()
    
    # create the matrix for the menu with [text, func()]
    options = [
        ["Editar mi ingreso.", htr.edit],
        ["Ver la historia completa.", htr.print_full],
        ["Salir.", exit]
    ]

    while True:
        showOptions(options)
        optionSelected = selectOption(options)

        if options[optionSelected-1][1] == exit:
            clear()
            print(f"{Bcolors.FAIL}¡Adios!{Bcolors.ENDC}\n")
            exit()
        else:
            clear()
            # call the function in options[x][1]()
            options[optionSelected-1][1]()
            continue