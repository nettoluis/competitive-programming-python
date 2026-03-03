numero, quantidadeAcoes = [int(x) for x in input().split()]
for _ in range(quantidadeAcoes):
    numeroStr = str(numero)
    if numeroStr[-1] == '0':
        numero //= 10
    else:
        numero -= 1
print(numero)
