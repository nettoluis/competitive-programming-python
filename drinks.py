quantidadeCopos = int(input())
total = 0
listaPorcentagens = [int(porcentagem) for porcentagem in input().split()]
for porcentagem in listaPorcentagens:
    total += porcentagem
print(f'{(total * 100) / (quantidadeCopos * 100):.12f}')
