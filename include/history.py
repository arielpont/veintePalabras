class History:
    """ clase para manejar las historias """
   
    #variables
    fullHistory = ""
    lastPartHistory = ""
    newPartHistory = ""

    #métodos
    def __init__(self):
        fileObject = open(r"data/history.txt", encoding="utf-8")
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
        if self.getNewPartHistory() != "":
            fileObject = open(r"data/history.txt", "a", encoding="utf-8")
            fileObject.write(" " + self.getNewPartHistory())
            fileObject.close()

            fileObject = open(r"data/history.txt", "r", encoding="utf-8")
            self.setFullHistory(fileObject.read() + "...")
            fileObject.close()
            return True
        else:
            return False

