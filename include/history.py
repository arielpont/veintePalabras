try:
    import include.settings as settings
except ImportError:
    print("ImportError: el módulo 'settings' no se ha podido importar.")

try:
    from include.functions import clear, maxLen20
except ImportError:
    print("ImportError: el módulo 'fuctions' no se ha podido importar.")

try:
    from include.bcolor import Bcolors
except ImportError:
    print("ImportError: el módulo 'Bcolors' no se ha podido importar.")

try:
    import os
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    os = None

class History:
    """ clase para manejar las historias """
   
    # variables
    fullHistory = ""
    lastPartHistory = ""
    newPartHistory = ""
    # los nombres de las variables constantes van siempre en mayus.
    HISTORY_PATH = "dist/history.txt"

    #métodos
    def __init__(self):

        if not os.path.exists(os.path.dirname(self.HISTORY_PATH)):
            #el archivo no existe
            try:
                #intento crear el archivo y le cargo el principio de la historia
                os.makedirs(os.path.dirname(self.HISTORY_PATH))
                with open(self.HISTORY_PATH, "w") as file:
                    file.write("En un antiguo poblado Chino exisitía una costumbre muy rara. Los habitantes")
            except OSError:
                print("No se pudo crear el archivo " + self.HISTORY_PATH)
        else:
            #el archivo ya existe
            pass

        #abro y cierro el archivo en modo lectura
        with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
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
        #seteo solo si existe algún valor relevante
        if set != "":
            self.newPartHistory = set
        else:
            pass
    
    #convertir una list en string
    def listToString(self, list):  
        str = " " 
        return (str.join(list))
    
    #guardar la nueva parte de la historia
    def saveNewPartHistory(self):
        """ esta función es para guardar el nuevo fragmento de la historia """

        if self.getNewPartHistory() != "":
            #añado nuevo fragmento de historia
            with open(self.HISTORY_PATH, "a", encoding="utf-8") as f:
                f.write(" " + self.getNewPartHistory())

            #actualizo la la variable fullHistory
            with open(self.HISTORY_PATH, "r", encoding="utf-8") as f:
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
                with open(self.HISTORY_PATH, "w", encoding="utf-8") as f:
                    f.write(self.getFullHistory())
                    return True
            except:
                return False
        else:
            return False

            