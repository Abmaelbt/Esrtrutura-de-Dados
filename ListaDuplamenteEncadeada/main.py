from ListaDuplaEncadeada import ListaDuplaEncadeada


lista = ListaDuplaEncadeada()

lista.inserir_como_primeiro(7)
lista.inserir_antes_do_atual(10)
lista.inserir_apos_atual(32)
lista.inserir_como_ultimo(43)
lista.inserir_como_primeiro(23)
lista.inserir_na_posicao_k(4, 20)
lista.excluir_atual()
lista.excluir_elemento(4)
lista.excluir_elemento(1)

print("Elemento atual:", lista.atual.elemento)
lista.imprimir_lista()