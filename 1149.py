1149
"""Coletar um número inteiro A e um número positivo não nulo ordem e imprimir a soma de A + i for i in range(0,ordem)"""
soma = 0
while True:
    entradaUsuario = list(map(int,input().split(" ")))
    for num in entradaUsuario:
        A = entradaUsuario[0]
        N = num if num > 0 else None
    break
for i in range(0,N):
    soma += A + i
print(soma)