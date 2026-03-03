qtdTestes = int(input())

for _ in range(qtdTestes):
    tamanho = int(input())
    lista = [int(x) for x in input().split()]
    digitos = tuple(set(lista))
    for digito in digitos:
        if lista.count(digito) == 1:
            print(lista.index(digito) + 1)
