quantidadeTestes = int(input())

for teste in range(quantidadeTestes):
    numeros = sorted([int(x) for x in input().split()])
    if not numeros[2] - (sum(numeros) - numeros[2]):
        print('YES')
    else:
        print('NO')
