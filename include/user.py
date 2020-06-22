try:
    import  pytz
except ImportError:
    pytz = None

from datetime import datetime

class User:
    """ clase para manejar los usuarios """
    
    #variables
    userName = ""
    userSername = ""
    userEmail = ""
    userLogin = ""

    #métodos
    def __init__(self):
        #obtener la fecha y hora de logeuo del usuario
        timeZone = pytz.timezone("Europe/London")
        dateTimeZone = datetime.now(timeZone)
        self.setUserLogin("UTC+0, "+dateTimeZone.strftime("%H:%M:%S, %d/%m/%Y"))

    def __iter__(self):
        pass

    def __next__(self):
        pass

    #encapsulamiento de variables
    def getUserName(self):
        return self.userName

    def setUserName(self, set):
        self.userName = set
        return self.userName

    def getUserSername(self):
        return self.userSername

    def setUserSername(self, set):
        self.userSername = set
        return self.userSername

    def getUserEmail(self):
        return self.userEmail

    def setUserEmail(self, set):
        self.userEmail = set
        return self.userEmail

    def getUserLogin(self):
        return self.userLogin

    def setUserLogin(self, set):
        self.userLogin = set
        return self.userLogin

    #(tarea) crear funciones para almacenar los datos de los usuarios en un archivo