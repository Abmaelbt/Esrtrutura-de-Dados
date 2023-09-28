class No:
    def __init__(self, elemento):
        self.__elemento = elemento
        self.__proximo = None
        self.__anterior = None


@property
def elemento (self):
    self.__elemento

@property
def proximo (self):
    self.__proximo

@property
def anterior (self):
    self.__anterior


@elemento.setter
def elemento(self, elemento):
    self.__elemento = elemento

@proximo.setter
def proximo(self, proximo):
    self.__proximo = proximo

@anterior.setter
def anterior(self, anterior):
    self.__anterior = anterior