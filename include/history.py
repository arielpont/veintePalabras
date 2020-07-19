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

    #métodos
    def __init__(self):
        
        historyFilePath = "dist/history.txt"

        if not os.path.exists(os.path.dirname(historyFilePath)):
            #el archivo no existe
            try:
                #intento crear el archivo y le cargo el principio de la historia
                os.makedirs(os.path.dirname(historyFilePath))
                with open(historyFilePath, "w") as file:
                    file.write("En un antiguo poblado Chino exisitía una costumbre muy rara. Los habitantes")
            except OSError:
                print("No se pudo crear el archivo " + historyFilePath)
        else:
            #el archivo ya existe
            pass

        #abro el archivo en modo lectura
        fileObject = open(r""+historyFilePath, encoding="utf-8")

        self.setFullHistory(fileObject.read())
        #guardo las últimas 20 palabras
        self.setLastPartHistory(((self.getFullHistory()).split())[-20:])
        self.setLastPartHistory(self.listToString(self.getLastPartHistory()))

    def __iter__(self):
        pass

    def __next__(self):
        pass

    #encapsulamiento de variables
    def getFullHistory(self):
        return self.fullHistory
    
    def setFullHistory(self, set):
        self.fullHistory = set
        return self.fullHistory
    
    def getLastPartHistory(self):
        return self.lastPartHistory
    
    def setLastPartHistory(self, set):
        self.lastPartHistory = set
        return self.lastPartHistory

    def getNewPartHistory(self):
        return self.newPartHistory
    
    def setNewPartHistory(self, set):
        self.newPartHistory = set
        return self.newPartHistory
    
    #convertir una list en string
    def listToString(self, list):  
        str = " " 
        return (str.join(list))
    
    #guardar la nueva parte de la historia
    def saveNewPartHistory(self):
        """ esta función es para guardar el nuevo fragmento de la historia """

        if self.getNewPartHistory() != "":
            fileObject = open(r"dist/history.txt", "a", encoding="utf-8")
            fileObject.write(" " + self.getNewPartHistory())
            fileObject.close()

            fileObject = open(r"dist/history.txt", "r", encoding="utf-8")
            self.setFullHistory(fileObject.read() + "...")
            fileObject.close()
            return True
        else:
            return False