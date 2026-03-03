quantidadeTestes = int(input())

for _ in range(quantidadeTestes):
    palavra = input().lower()
    condicao = 'yes' == palavra
    print('YES') if condicao else print('NO')
