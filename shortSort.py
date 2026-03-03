quantidadePalavras = int(input())

for _ in range(quantidadePalavras):
    errados = 0
    teste = input()
    if teste[0] != 'a':
        errados += 1
    if teste[1] != 'b':
        errados += 1
    if teste[2] != 'c':
        errados += 1
    if errados > 2: print('NO')
    else: print('YES')
