# Standard library imports
# Third party imports
# Local application imports
from modules.bcolor import Bcolors
from modules.functions import clear, print_error, show_options, select_option
import modules.history as history

if __name__ == "__main__":
    clear()

    # init instance History()
    htr = history.History() 

    # check if an history already exists and then continue writing
    if(htr.exists()):
        history_is_new = False

        while True:
            clear()
            print(f"{Bcolors.HEADER}Es momento de continuar la historia: {Bcolors.ENDC}\n")
            new_part = input(f"{htr.get_full()} {Bcolors.OKGREEN}")
            
            if htr.add_new_part(new_part):
                clear()
                print(f"{Bcolors.ENDC}Tu historia a sido guardada:")
                print(f"{Bcolors.OKBLUE}{htr.get_full()}{Bcolors.ENDC}\n")

                break
            else:
                continue
    # init a new history from blank
    else:
        history_is_new = True

        htr.begin()  

    # create the matrix for the menu with [text, func()]
    options = [
        ["Editar mi ingreso.", htr.edit],
        ["Ver la historia completa.", htr.print_full],
        ["Salir.", exit]
    ]

    while True:
        show_options(options)
        option = select_option(options)

        if options[option-1][1] == exit:
            clear()
            print(f"{Bcolors.FAIL}¡Adios!{Bcolors.ENDC}\n")
            exit()
        elif options[option-1][1] == htr.edit:
            clear()

            if history_is_new:
                # call the function to reset the history (only in case the user is starting a new story)
                htr.edit(reset = True)
                continue
            else:
                htr.edit(reset = False)
                continue
        else:
            clear()
            # call the function in options[x][1]()
            options[option-1][1]()
            continue