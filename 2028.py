2028
'''Imprimir uma sequência em que cada número indica também a quantidade de vezes que ele se repete'''
i = 1
while True:
    try:
        N = int(input())
        sequencia = []
        if N >= 0:
            sequencia.append(0)
        if N >= 1:
            sequencia.append(1)
        for num in range(2, N + 1):
            sequencia.extend([num] * num)
        count = len(sequencia)
        print(f'Caso {i}: {count} numero{"s" if count != 1 else ""}')
        print(' '.join(map(str, sequencia)))
        print()
        i += 1
    except EOFError:
        break