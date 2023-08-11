class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            print("A pilha está vazia.")

    def top(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            print("A pilha está vazia.")

    def is_empty(self):
        return len(self.itens) == 0

    def size(self):
        return len(self.itens)
