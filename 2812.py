def swap(s, i1, i2):
    temp = s[i1]
    s[i1] = s[i2]
    s[i2] = temp


def trocas(sequencia, p1, p2):
    maior, i_maior = 0, 0
    for i in range(p1, len(sequencia)):
        elemento = sequencia[i]
        if elemento >= maior:
            maior = sequencia[i]
            i_maior = i

    swap(sequencia, i_maior, p1)

    menor, i_menor = float('inf'), 0
    for i in range(p2 - 1, len(sequencia)):
        elemento = sequencia[i]
        if elemento <= menor:
            menor = sequencia[i]
            i_menor = i

    swap(sequencia, i_menor, p2)


def ordenacao_amarildica(sequencia):
    maiores_ponteiro, menores_ponteiro = 0, 1
    for _ in range(len(sequencia) // 2):
        trocas(sequencia, maiores_ponteiro, menores_ponteiro) 
        maiores_ponteiro += 2
        menores_ponteiro += 2


def main():
    qtd = int(input())

    for _ in range(qtd):
        tamanho = int(input())
        sequencia = [int(x) for x in input().split()]

        ordenacao_amarildica(sequencia)
        lista = [str(x) for x in sequencia]

        print(f'{" ".join(lista)}')
        print()


main()
