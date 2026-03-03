PALAVRA = set('codeforces')
qtdLetras = int(input())

for _ in range(qtdLetras):
    letra = input()
    print('YES') if letra in PALAVRA else print('NO')
