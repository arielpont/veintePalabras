class History:
    """ clase para manejar las historias """
   
    #variables
    history = ""

    #funciones
    def __init__(self):
        a_file = open("data/history.txt", encoding="utf-8")
        self.setHistory(a_file.read())

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def getHistory(self):
        return self.history
    
    def setHistory(self, set):
        self.history = set
        return self.history

    #encapsulamiento de variables