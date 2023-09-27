class Superarray:
    def __init__(self, inicio, fim):
        #verifica se a ordenacao e crescente ou decrescente
        if fim >= inicio:
            self.liminf = inicio
            self.limsup = fim
        else:
            self.liminf = fim
            self.limsup = inicio
        #definindo a array vazia
        self.__array = [None]*(self.limsup - self.liminf+ 1)
    #atrubui de acordo com a posicao        
    def atribuir(self, posicao, valor):
        #se a posicao tiver fora dos limites, dispara erro
        if posicao >  self.limsup or posicao < self.liminf:
            raise ValueError
        else:
            #atribui o valor no array considerando a sua posicao de fato (=! lista py)
            self.__array[posicao - self.liminf] = valor
    
    def acessar(self, posicao):
        if posicao >  self.limsup or posicao < self.liminf:
            raise IndexError
        else:
            return self.__array[posicao -  self.liminf]
        
