1929
'''Coletar quatro comprimentos de arestas e confirmar se é possível construir um triângulo'''
a, b, c, d = map(int, input().split())
print('S') if (a + b > c and a + c > b and b + c > a) or (a + b > d and a + d > b and b + d > a) or (a + c > d and a + d > c and c + d > a) or (b + c > d and b + d > c and c + d > b) else print('quantidadeFazendas')