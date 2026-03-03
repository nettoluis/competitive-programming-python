def absoluto(a):
    return ((a ** 2) ** 0.5)


def contaEscadinhas(sequencia):
    if len(sequencia) == 1 or len(sequencia) == 2:
        return 1
    escadinhas = 1
    diferencaAtual = absoluto(sequencia[0] - sequencia[1])
    for i in range(1, len(sequencia) - 1):
        atual, posterior = sequencia[i], sequencia[i + 1]
        if absoluto(atual - posterior) == diferencaAtual:
            continue
        else:
            escadinhas += 1
            diferencaAtual = absoluto(atual - posterior)

    return escadinhas
    
def main():
    qtd, sequencia = int(input()), list(map(int, input().split()))

    escadinhas = contaEscadinhas(sequencia)

    print(escadinhas)

    

main()
