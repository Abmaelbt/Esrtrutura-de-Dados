from no import No


class ListaDuplaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def acessar_atual(self):
        # verifica se o atual nao e nulo
        # se nao for, retorna o atual
        if self.atual is None:
            raise ValueError("Não existe valor no Nó atual")
        else:
            return self.atual

    def inserir_antes_do_atual(self, novo):
        novo_no = No(novo)
        anterior = self.atual.anterior  # armazeno o NO anterior na variavel

        # o proximo do novo vai ser o atual
        # o anterior do novo vai ser o anterior do atual
        # ao final, o atual vai ser o novo NO
        novo_no.anterior = anterior
        novo_no.proximo = self.atual
        self.atual.__anterior = novo_no
        if anterior is not None:
            anterior.proximo = novo_no
        else:
            self.primeiro = novo_no
        self.atual = novo_no

    def inserir_apos_atual(self, novo):
        novo_no = No(novo)
        # armazeno o proximo NO na variavel
        proximo = self.atual.proximo
        # passos de acordo com o slide 17 sobre listas duplamente encadeadas:
        # passo 2:
        novo_no.proximo = proximo
        # passo 3:
        novo_no.anterior = self.atual
        # passo 4:
        self.atual.proximo = novo_no
        # passo 5:
        if proximo is not None:
            proximo.anterior = novo_no
        else:
            self.ultimo = novo_no
        # aponto o ponteiro para o recém atual
        self.atual = novo_no

    def inserir_como_ultimo(self, novo):
        novo_no = No(novo)

        # novo NO ja comeca como anterior ao ultimo
        # se o meu ultimo atual nao for Nulo, o proximo a ele sera o novo NO
        # se for nulo e porque nao existe valor na lista e ele sera o primeiro
        # ponteiro aponta o NO pro ultimo e atual

        novo_no.anterior = self.ultimo
        if self.ultimo is not None:
            self.ultimo.proximo = novo_no
        else:
            self.primeiro = novo_no
        self.ultimo = novo_no
        self.atual = novo_no

    def inserir_como_primeiro(self, novo):
        novo_no = No(novo)

        # novo NO comeca como proximo ao primeiro
        # se o meu primeiro atual nao for Nulo, o anterior a ele sera o novo NO
        # se for nulo e porque nao existe valor na lista apos o primeiro e ele sera o ultimo
        # ponteiro aponta o NO pro primeiro e atual

        novo_no.proximo = self.primeiro
        if self.primeiro is not None:
            self.primeiro.anterior = novo_no
        else:
            self.ultimo = novo_no
        self.primeiro = novo_no
        self.atual = novo_no

    def inserir_na_posicao_k(self, k, novo):

        if k < 0:
            raise IndexError('Indice não pode ser menor que 0')
        # se = 0, significa que será o primeiro da lista
        if k == 0:
            self.inserir_como_primeiro(novo)
            return

        novo_no = No(novo)
        atual = self.primeiro  # move o ponteiro para o inicio da lista
        # faco a interacao de acordo com K
        # se o valor atual for None a funcao para
        # senao, o meu atual vai ser o proximo
        for _ in range(k - 1):
            if atual is None:
                return
            atual = atual.proximo

        # se apos a iteracao o atual ainda e Nulo, a funcao e interrompida
        if atual is None:
            return

        # anterior ao Novo NO sera o atual
        # proximo ao Novo NO sera o proximo do atual
        # se o anterior do atual nao for nulo, o anterior do proximo do atual e o novo NO
        # se nao for, ele entao sera o ultimo

        novo_no.anterior = atual
        novo_no.proximo = atual.proximo
        if atual.anterior is not None:
            atual.proximo.anterior = novo_no
        else:
            self.ultimo = novo_no
        atual.proximo = novo_no
        self.atual = novo_no

    def excluir_atual(self):
        # se for Nulo, dispara excecao:
        if self.atual is None:
            raise ValueError("Não existe valor no Nó atual")

        # armazena o NO anterior e proximo do atual em duas variaveis
        # seguir os passos conforme slide:
        # proximo do anterior sera o proximo e nao mais o atual
        # anterior do proximo sera o anterior e nao mais o atual

        anterior = self.atual.anterior
        proximo = self.atual.proximo

        if anterior is not None:
            anterior.proximo = proximo
        else:
            self.primeiro = proximo

        if proximo is not None:
            proximo.anterior = anterior
        else:
            self.ultimo = anterior

        self.atual = proximo

    def excluir_primeiro(self):
        if self.primeiro is None:
            return
        # se o cursor tiver no primeiro NO, transfiro ele para o NO seguinte
        if self.atual == self.primeiro:
            self.atual = self.primeiro.proximo

        if self.primeiro.proximo is not None:
            # se o NO seguinte existir, o anterir dele que antes era o primeiro, passará a ser None(será excluido)
            self.primeiro.proximo.anterior = None
        else:
            # se nao existir e porque so tem esse elemente, entao o mesmo sera None
            self.ultimo = None
        # o meu primeiro no passara a ser o proximo e ele deixa de existir
        self.primeiro = self.primeiro.proximo

    def excluir_ultimo(self):
        if self.ultimo is None:
            raise ValueError("Não existe valor no primeiro Nó")
        if self.atual == self.ultimo:
            self.atual = self.ultimo.anterior

        if self.ultimo.anterior is not None:
            self.ultimo.anterior.proximo = None
        else:
            self.primeiro = None
        self.ultimo = self.ultimo.anterior

    def excluir_elemento(self, chave):
        atual = self.primeiro

        # cursor comeca na primeira posicao
        # enquando o atual nao for nulo:
        # 1 - verifico se o valor e igual a chave
        # 1.1 - verifico se o NO atual da iteracao e igual ao NO atual da lista
        # 1.2 - se for igual, o atual vai apontar para o proximo garantindo que o cursor seja mantido
        # 2 - exclui o elemento e aponto o cursor para o proximo do meu atual caso haja mais elementos a excluir
        while atual is not None:
            if atual.elemento == chave:
                if self.atual == atual:
                    self.atual = atual.proximo

                proximo = atual.proximo
                anterior = atual.anterior

                if anterior is not None:
                    anterior.proximo = proximo
                else:
                    self.primeiro = proximo

                if proximo is not None:
                    proximo.anterior = anterior
                else:
                    self.ultimo = anterior

            atual = atual.proximo

    def excluir_da_pos(self, k):
        if k < 0:
            return
        # se == 0 e o primeiro elemento
        if k == 0:
            self.excluir_primeiro()

        # atual comeca como primeiro
        # enquanto o atual nao for nulo:
        # 1 - verifico se a posicao e igual a K
        # 1.1 - verifico se o atual da iteracao e igual o atual da lista, se igual o atual da iteracao sera o proximo
        # 2 - armazeno os NOS anterior e atual e variaveis para realizar a exclusao do elemento
        # 3 - ponteiro aponta pro proximo do meu atual da iteracao
        # 4 - adiciona 1 na posicao para a verificacao dos elementos se o while nao for correspondido no inicio
        atual = self.primeiro
        posicao = 0

        while atual is not None:
            if posicao == k:
                if self.atual == atual:
                    self.atual = atual.proximo

                anterior = atual.anterior
                proximo = atual.proximo

                if anterior is not None:
                    anterior.proximo = proximo
                else:
                    self.primeiro = proximo

                if proximo is not None:
                    proximo.anterior = anterior
                else:
                    self.ultimo = anterior

                return
            atual = atual.proximo
            posicao += 1

    def buscar(self, chave):
        atual = self.primeiro
        posicao = 0
        while atual is not None:
            if atual.__elemento == chave:
                self.atual = atual
                return True
            else:
                atual = atual.proximo
                posicao += 1
        return False

    def avancar_k_posicoes(self, k):
        for _ in range(k):
            if self.atual is not None:
                self.atual = self.atual.proximo

    def retroceder_k_posicoes(self, k):
        for _ in range(k):
            if self.atual is not None:
                self.atual = self.atual.anterior

    def ir_para_primeiro(self):
        self.atual = self.primeiro

    def ir_para_ultimo(self):
        self.atual = self.ultimo

    def imprimir_lista(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.elemento, end=" ")
            atual = atual.proximo
        print()
