from Supermatriz import Supermatriz

Matriz1 = Supermatriz(3, 4)
Matriz2 = Supermatriz(5, 5)
Matriz3 = Supermatriz(2, 7)

Matriz1.atribuir(1, 2, 4)
Matriz2.atribuir(4, 4, 33)
Matriz3.atribuir(2, 7, 10)

valor1 = Matriz1.acessar(1, 2)
valor2 = Matriz2.acessar(4, 4)
valor3 = Matriz3.acessar(2, 7)

print(valor1)
print(valor2)
print(valor3)