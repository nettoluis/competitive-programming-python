1858
'''Coletar a quantidade de pessoas que ele terá que adivinhar e depois imprimir o menor valor possível'''
qtdPessoas = int(input())
numeracoesPessoas = list(map(int,input().split()))
print(f"{numeracoesPessoas.index(min(numeracoesPessoas)) + 1}")
