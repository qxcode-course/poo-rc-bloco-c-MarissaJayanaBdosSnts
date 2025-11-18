class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return "Foo(" + str(self.x) + ")"


lista_vazia = []
lista_preenchida = [1, 2, 3, 4, 5]
lista_preenchida_objetos = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

print("Lista vazia:", lista_vazia)
print("Lista preenchida:", lista_preenchida)

print("Lista objetos:")
for obj in lista_preenchida_objetos:
    print(str(obj))

print("Tamanho lista preenchida:", len(lista_preenchida))


lista_preenchida.append(6)
print("Após append:", lista_preenchida)

lista_preenchida.pop()
print("Após pop:", lista_preenchida)


lista_preenchida.insert(0, 99)
print("Após inserir no início:", lista_preenchida)

lista_preenchida.pop(0)
print("Após remover do início:", lista_preenchida)

lista_preenchida.insert(2, 123)
print("Após inserir na pos 2:", lista_preenchida)

lista_preenchida.pop(2)
print("Após remover pos 2:", lista_preenchida)

texto = "-".join(str(x) for x in lista_preenchida)
print("Join formatado:", texto)


n = 10
sequencia = []
for i in range(n + 1):
    sequencia.append(i)

print("Sequência 0..n:", sequencia)


valores_aleatorios = []
seed = 7
for i in range(5):
    seed = (seed * 3 + 1) % 10
    valores_aleatorios.append(seed)

print("Valores aleatórios (sem biblioteca):", valores_aleatorios)
print("Primeiro elemento:", lista_preenchida[0])
print("Último elemento:", lista_preenchida[len(lista_preenchida) - 1])


print("For-range:")
for elem in lista_preenchida:
    print(elem)

print("For indexado:")
for i in range(len(lista_preenchida)):
    print("índice", i, "valor", lista_preenchida[i])

def procurar_laço(lista, x):
    for elem in lista:
        if elem == x:
            return True
    return False


print("Procurar 3 (laço):", procurar_laço(lista_preenchida, 3))
print("Procurar 3 (in):", 3 in lista_preenchida)

pares = []
for x in lista_preenchida:
    if x % 2 == 0:
        pares.append(x)

print("Filtrados pares:", pares)

quadrados = []
for x in lista_preenchida:
    quadrados.append(x * 2)

print("Transformando (x2):", quadrados)

def remover_primeiro(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            lista.pop(i)
            return True
    return False


remover_primeiro(lista_preenchida, 4)
print("Remover primeiro 4:", lista_preenchida)


def remover_todos(lista, x):
    i = 0
    while i < len(lista):
        if lista[i] == x:
            lista.pop(i)
        else:
            i += 1

print("Ordenação com sort:", sorted([5, 3, 1, 4, 2]))
print("Reverso com reverse:", list(reversed([1, 2, 3, 4])))

lista_teste = [1, 2, 3, 2, 4, 2, 5]
remover_todos(lista_teste, 2)
print("Remover todos os 2:", lista_teste)

print("Funções nativas úteis:")
print(" - append")
print(" - pop")
print(" - insert")
print(" - remove")
print(" - sort")
print(" - reverse")
print(" - index")
print(" - count")





