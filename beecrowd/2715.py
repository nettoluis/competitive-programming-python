def absoluto(a):
    return int((a ** 2) ** 0.5)


def soma(lista, ini, fim):
    soma = 0
    for i in range(ini, fim):
        soma += lista[i]

    return soma


def calculaMenorDiferenca(lista, qtd):
    total, esquerda = soma(lista,0, qtd), 0
    menorDiferenca = float('inf')

    for i in range(qtd - 1):
        esquerda += lista[i]
        direita  = total - esquerda
        diferencaAtual = absoluto(direita - esquerda)

        if diferencaAtual < menorDiferenca:
            menorDiferenca = diferencaAtual

    return menorDiferenca


def main():
    while True:
        try:
            qtd = int(input())
            tarefas = [int(x) for x in input().split()]

            menorDiferenca = calculaMenorDiferenca(tarefas, qtd)

            print(menorDiferenca)
        except EOFError:
            break


main()
