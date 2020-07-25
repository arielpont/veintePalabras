try:
    import os
except ImportError:
    print("ImportError: no se han podido importar todos los módulos.")
    os = None

class History:
    """ clase para manejar las historias """
   
    #variables
    fullHistory = ""
    lastPartHistory = ""
    newPartHistory = ""
    historyFilePath = "dist/history.txt"

    #métodos
    def __init__(self):

        if not os.path.exists(os.path.dirname(self.historyFilePath)):
            #el archivo no existe
            try:
                #intento crear el archivo y le cargo el principio de la historia
                os.makedirs(os.path.dirname(self.historyFilePath))
                with open(self.historyFilePath, "w") as file:
                    file.write("En un antiguo poblado Chino exisitía una costumbre muy rara. Los habitantes")
            except OSError:
                print("No se pudo crear el archivo " + self.historyFilePath)
        else:
            #el archivo ya existe
            pass

        #abro y cierro el archivo en modo lectura
        with open(self.historyFilePath, "r", encoding="utf-8") as f:
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
            with open(self.historyFilePath, "a", encoding="utf-8") as f:
                f.write(" " + self.getNewPartHistory())

            #actualizo la la variable fullHistory
            with open(self.historyFilePath, "r", encoding="utf-8") as f:
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
    
    def updateNewPartHistory(self, new):
        """ esta función es para editar el nuevo fragmento de la historia """

        if new != "":
            if self.deleteNewPartHistory(len(self.getNewPartHistory())):
                print(f"Se han borrado {int(len(str(self.getNewPartHistory())))} caracteres finales de la historia.")
                self.setNewPartHistory(new)
                self.setFullHistory(self.getFullHistory() + self.getNewPartHistory())

                try:
                    with open(self.historyFilePath, "w", encoding="utf-8") as f:
                        f.write(self.getFullHistory())
                        return True
                except:
                    return False
            else:
                return False
        else:
            return False

            