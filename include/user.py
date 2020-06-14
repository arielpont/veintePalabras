class User:
    """ clase para manejar los usuarios """
    
    #variables
    userName = ""
    userSername = ""
    userLogin = ""

    def __init__(self):
        #guardar la fecha de logeuo del usuario
        pass

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

    def getUserLogin(self):
        return self.userLogin

    def setUserLogin(self, set):
        self.userLogin = set
        return self.userLogin