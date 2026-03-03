qtdTestes = int(input())

for _ in range(qtdTestes):
    tamanho = int(input())
    lista = sorted([int(x) for x in input().split()])
    pode = True
    i, j = 0, 1
    for iteracoes in range(tamanho - 1):
        if (lista[j] - lista[i]) <= 1:
            lista.pop(i)
        else:
            pode = False
            break
    print('YES') if pode else print('NO')
