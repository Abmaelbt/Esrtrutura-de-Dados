from no import no
# o No sempre vai buscar o sucessor ou antecessor de acordo com o ponteiro



class ListaDuplaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def acessar_atual(self):
        # verifica se o atual nao e nulo
        if self.atual is None:
            raise ValueError("Não existe valor no Nó atual")
        else:
            return self.atual

    def inserir_antes_do_atual(self, novo):
        novo_no = No(novo)
        anterior = self.atual.anterior  # armazeno o NO an

        novo_no.anterior = anterior
        novo_no.proximo = self.atual
        self.atual.anterior = novo_no
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
        novo_no.anterior = self.ultimo
        if self.ultimo is not None:
            self.ultimo.proximo = novo_no
        else:
            self.primeiro = novo_no
        self.ultimo = novo_no
        self.atual = novo_no

    def inserir_como_primeiro(self, novo):
        novo_no = No(novo)
        novo_no.proximo = self.primeiro
        if self.primeiro is not None:
            self.primeiro.anterior = novo_no
        else:
            self.ultimo = novo_no
        self.primeiro = novo_no
        self.atual = novo_no

    def inserir_na_posicao_k(self, k, novo):

        if k < 0:
            return
        # se = 0, significa que será o primeiro da lista
        if k == 0:
            self.inserir_como_primeiro(novo)
            return

        novo_no = No(novo)
        atual = self.primeiro
        for _ in range(k - 1):
            if atual is None:
                return
            atual = atual.proximo

        if atual is None:
            return

        novo_no.anterior = atual
        novo_no.proximo = atual.proximo
        if atual.anterior is not None:
            atual.proximo.anterior = novo_no
        else:
            self.ultimo = novo_no
        atual.proximo = novo_no
        self.atual = novo_no

    def excluir_atual(self):
        if self.atual is None:
            raise ValueError("Não existe valor no Nó atual")

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

        while atual is not None:
            if atual.valor == chave:
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
            raise IndexError("K nao pode ser menor que 0")

        if k == 0:
            self.excluir_primeiro()

        atual = self.primeiro

        anterior = atual.anterior
        proximo = atual.proximo

        for _ in range(k - 1):
            if atual is None:
                raise ValueError("Não existe valor no nó atual buscado")
            atual = atual.proximo

        if atual is None:
            raise ValueError("Não existe valor no índice atual")

        if anterior is not None:
            anterior.proximo = proximo
        else:
            self.primeiro = proximo

        if proximo is not None:
            proximo.anterior = anterior
        else:
            self.ultimo = anterior

        atual = atual.proximo
        # testar melhor!

    def buscar(self, chave):
        atual = self.primeiro
        posicao = 0
        while atual is not None:
            if atual.elemento == chave:
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
