def bubbleSort(sequencia, tamanhoSequencia):
    mudancas = 0
    for i in range(tamanhoSequencia - 1):
        if sequencia[i] > sequencia[i + 1]:
            swap(sequencia, i, i + 1)
            mudancas += 1

    if mudancas > 0:
        bubbleSort(sequencia, tamanhoSequencia - 1)


def swap(sequencia, i1, i2):
    temp = sequencia[i1]
    sequencia[i1] = sequencia[i2]
    sequencia[i2] = temp


def main():
    while True:
        try:
            populacao, consultas = [int(x) for x in input().split()]

            notas = []
            for _ in range(populacao):
                notas.append(int(input()))

            bubbleSort(notas, len(notas))
            for _ in range(consultas):
                i = int(input())
                print(notas[-i])
        except EOFError:
            break


main()
