import os
import include.settings as settings
from include.functions import clear, maxLen20
from include.bcolor import Bcolors

# variables constantes
HISTORY_PATH = "dist/history.txt"

class History:
    """ clase para manejar las historias """

    #métodos
    def __init__(self):

        # variables de instancia
        self.fullHistory = ""
        self.lastPartHistory = ""
        self.newPartHistory = ""

        if not os.path.exists(os.path.dirname(HISTORY_PATH)):
            #el archivo no existe
            try:
                #intento crear el archivo y le cargo el principio de la historia
                os.makedirs(os.path.dirname(HISTORY_PATH))

                # 1. ¿queres inspiración?
                    # 1a. música
                    # 2a. imágenes en bit

                # 2. Ya estoy listo para empezar mi historia

                with open(HISTORY_PATH, "w") as file:
                    file.write("Holaaaaa")
                    # "En un antiguo poblado Chino exisitía una costumbre muy rara. Los habitantes"
            except OSError:
                print("No se pudo crear el archivo " + HISTORY_PATH)
        else:
            #el archivo ya existe
            pass

        #abro y cierro el archivo en modo lectura
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            self.setFullHistory(f.read())
            #guardo las últimas 20 palabras
            self.setLastPartHistory(((self.getFullHistory()).split())[-20:])
            self.setLastPartHistory(self.listToString(self.getLastPartHistory()))

    #encapsulamiento de variables
    def getFullHistory(self):
        return self.fullHistory
    def setFullHistory(self, set):
        self.fullHistory = set
    
    def getLastPartHistory(self):
        return self.lastPartHistory
    def setLastPartHistory(self, set):
        self.lastPartHistory = set

    def getNewPartHistory(self):
        return self.newPartHistory
    def setNewPartHistory(self, set):
        # seteo solo si existe algún valor relevante
        if set != "":
            self.newPartHistory = set
        else:
            pass
    
    # convertir una list en string
    def listToString(self, list):  
        str = " " 
        return (str.join(list))
    
    #guardar la nueva parte de la historia
    def saveNewPartHistory(self):
        """ esta función es para guardar el nuevo fragmento de la historia """

        if self.getNewPartHistory() != "":
            #añado nuevo fragmento de historia
            with open(HISTORY_PATH, "a", encoding="utf-8") as f:
                f.write(" " + self.getNewPartHistory())

            #actualizo la la variable fullHistory
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                self.setFullHistory(f.read())
            return True
        else:
            return False

    def deleteNewPartHistory(self, num):
        try:
            num = int(num)
            self.setFullHistory((self.getFullHistory()[:-num]))
            return True
        except:
            return False
    
    def updateNewPartHistory(self):
        """ esta función es para editar el nuevo fragmento de la historia """

        #el usuario debe ingresar algo menor a igual a 20 palabras
        while True:
            new = input(f"{Bcolors.OKGREEN}...{str(settings.history.getLastPartHistory())}{Bcolors.ENDC} ")
            
            if maxLen20(new):
                break
            else:
                continue
        
        #calculamos el lenght de su último ingreso y borramos ese mismo número de la historia full
        if self.deleteNewPartHistory(len(self.getNewPartHistory())):
            clear()
            print(f"{Bcolors.FAIL}Se han borrado {Bcolors.BOLD}{int(len(str(self.getNewPartHistory())))}{Bcolors.ENDC} {Bcolors.FAIL}caracteres finales de la historia.{Bcolors.ENDC}\n")
            #sobreescribimos la variable "newPartHistory" con lo que el usuario editó.
            self.setNewPartHistory(new)
            #actualizamos la historia completa
            self.setFullHistory(self.getFullHistory() + self.getNewPartHistory())
            #escribimos en el archivo la historia completa con el último ingreso del usuario editado
            try:
                with open(HISTORY_PATH, "w", encoding="utf-8") as f:
                    f.write(self.getFullHistory())
                    return True
            except:
                return False
        else:
            return False

            