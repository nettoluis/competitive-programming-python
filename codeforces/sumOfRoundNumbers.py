quantidadeCasos = int(input())

for caso in range(quantidadeCasos):
    original = input()
    decomposicao = []
    for i in range(len(original)):
        if original[i] == '0':
            continue
        else:
            valor = original[i] + ('0' * (len(original) - 1 - i))
            decomposicao.append(valor)
    print(f'{len(decomposicao)}\n{" ".join(decomposicao)}')
