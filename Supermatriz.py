from Superarray import Superarray


class Supermatriz(Superarray):
    def __init__(self, numero_de_linhas, numero_de_colunas):
        super().__init__(1, numero_de_linhas) #chamando os atributos da classe Superarray
        
        #definindo o num de col, linhas e matriz padrao
        self.__liminf_col = 1
        self.__limsup_col = numero_de_colunas
        self.__matriz = [[None]*numero_de_colunas for _ in range(numero_de_linhas)]
        
    def atribuir(self, linha, coluna, valor):
        # verifico se os valores informados para linha e coluna estao fora dos limites do construtor
        # para verificar linha, pego os limites do superarray
        # dispara exceção se tiver fora dos limites
        if (linha > self.limsup or linha < self.liminf or
            coluna > self.__limsup_col or coluna < self.__liminf_col
        ):
            raise ValueError('Posição informada esta fora dos limites da matriz')
        
        else:
            # subtrai os liminf para obter o indice correto matematico de uma matriz
            self.__matriz[linha - self.liminf][coluna - self.__liminf_col] = valor
    
    def acessar(self,linha, coluna):
        if (linha > self.limsup or linha < self.liminf or
            coluna > self.__limsup_col or coluna < self.__liminf_col
        ):
            raise ValueError('Posição informada esta fora dos limites da matriz')
        
        else:
            return self.__matriz[linha-self.liminf][coluna-self.__liminf_col]
        
    def imprimir(self):
        for linha in self.__matriz:
            print(linha)