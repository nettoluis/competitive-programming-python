quantidadeCasos, x = int(input()), 0
for caso in range(quantidadeCasos):
    operacao = input()
    if '++' in operacao:
        x += 1
    else:
        x -= 1
print(x)
