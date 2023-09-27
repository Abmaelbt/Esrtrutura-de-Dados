from ListaDuplaEncadeada import ListaDuplaEncadeada


lista = ListaDuplaEncadeada()

lista.inserir_como_ultimo(10)
lista.inserir_como_ultimo(20)
lista.inserir_como_primeiro(7)
lista.inserir_na_posicao_k(2, 45)
lista.excluir_primeiro()

print("Elemento atual:", lista.atual.elemento)


