1142
"""Coletar um número inteiro que determinará a quantidade de linhas e depois imprimir uma sequência de três números seguidos da palavra PUM, a cada linha adicionando 4 a cada número."""
vezes = int(input())
for num in range(1,vezes * 4,4):
    print(f'{num} {num + 1} {num + 2} PUM')