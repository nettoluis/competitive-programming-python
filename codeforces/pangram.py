quantidadeLetras = int(input())
palavraTestada = input().lower()
if quantidadeLetras >= 26: print('YES') if len(set(palavraTestada)) == 26 else print('NO')
else: print('NO')
