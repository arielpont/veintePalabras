# Standard library imports
import os
# Third party imports
# Local application imports
from modules.functions import clear, print_error, confirm
from modules.bcolor import Bcolors

class History:
    """ Clase para manejar las historias """

    HISTORY_PATH = "dist/history.txt"

    def __init__(self):
        self.backup_history = ""

    def add_new_part(self, new_part):
        """ Esta función es para guardar el nuevo fragmento de la historia """
        
        if new_part != "":
            if self.max_len20(new_part):

                # do a backup of the history just for in case user wants to edit
                with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
                    self.backup_history = f.read()

                # append new part history
                with open(self.HISTORY_PATH, "a", encoding="utf-8") as f:
                    f.write(f" {new_part}")
                    return True
            else:
                print_error("Debes ingresar hasta 20 palabras.")
                return False
        else:
            print_error("Debes añadir algo a la historia.")
            return False

    def begin(self):
        """ Start writting de history """

        if not os.path.exists(os.path.dirname(self.HISTORY_PATH)):
            
            try:
                os.makedirs(os.path.dirname(self.HISTORY_PATH))

                with open(self.HISTORY_PATH, "w", encoding="utf-8") as f:
                    f.write("En un antiguo poblado Chino los habitantes")
                    # do a backup of the history just for in case user wants to edit
                    self.backup_history = "En un antiguo poblado Chino los habitantes"
                    
            except OSError:
                print_error("No se pudo crear el archivo " + self.HISTORY_PATH)

        else:
            print(f"{Bcolors.OKBLUE}¡Encontramos una historia creada!{Bcolors.ENDC}\n")
    
    def edit(self, reset):
        """ Edit the last user input. If reset = True reseat all the history. """
        
        x = len(self.get_full()) - len(self.backup_history)

        if not reset:
            x -= 1

        print(f"Su último ingreso es: {Bcolors.OKGREEN}{self.get_full()[-x:]}{Bcolors.ENDC}\n")

        print(f"{Bcolors.FAIL}Al editar, su último ingreso será sobreescrito y no podrá se recuperado.{Bcolors.ENDC}\n")
        
        if confirm("¿Está seguro que quiere editar su último ingreso?"):
            
            with open(self.HISTORY_PATH, "w", encoding="utf-8") as f:
                if reset:
                    f.write("<<< Inicio >>>")
                else:
                    f.write(self.backup_history)

            while True:
                clear()
                new_part = input(f"{self.get_full()} {Bcolors.OKGREEN}")
                if self.max_len20(new_part):
                    if self.add_new_part(new_part):
                        print(f"{Bcolors.ENDC}Tu historia a sido guardada: {Bcolors.OKBLUE}{self.get_full()}{Bcolors.ENDC}\n")
                        break
                    else:
                        continue
                else:
                    continue

        else:
            clear()
            print(f"{Bcolors.OKGREEN}Usted eligió no editar su último ingreso.{Bcolors.ENDC}\n")

    def exists(self):
        """ Return True if the history.txt exists and is not empty.
            Return False if the history.txt dosn't exists or it is empty. """
        
        if os.path.exists(os.path.dirname(self.HISTORY_PATH)):
            with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
                if len(f.read()) > 0:
                    return True
                else:
                    return False
        else:
            return False

    def get_full(self):
        with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
           return f.read()
    
    def max_len20(self, msg):
        if len(msg.split()) <= 20:
            return True
        else:
            return False
    
    def print_full(self):
        with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
           print(f"{Bcolors.OKBLUE}{f.read()}{Bcolors.ENDC}\n")
            