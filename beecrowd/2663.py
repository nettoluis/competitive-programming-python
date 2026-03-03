def inverte(sequencia):
    sequenciaInvertida = []
    for i in range(len(sequencia) - 1, -1, -1):
        sequenciaInvertida.append(sequencia[i])

    return sequenciaInvertida


def insercaoOrdenada(sequencia, elemento):
    for i in range(len(sequencia) - 1, -1, -1):
        if sequencia[i] <= elemento:
            sequencia.insert(i + 1, elemento)
            return

    sequencia.insert(0, elemento)


def contadorMaioresIguais(sequencia, comparacao):
    contador = 0
    for e in sequencia:
        if e >= comparacao:
            contador += 1

    return contador


def main():
    qtd = int(input())

    minimo = int(input())
    
    notas = []
    for _ in range(qtd):
        nota = int(input())
        if not notas:
            notas.append(nota)
        else:
            insercaoOrdenada(notas, nota)

    notas = inverte(notas)
    notaCorte = notas[minimo - 1]
    passados = contadorMaioresIguais(notas, notaCorte)
    print(passados)


main()
