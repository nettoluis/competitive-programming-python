2161
'''Dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.'''
resultado = 0.0
quantidadeDeRepeticoes = int(input())
for _ in range(quantidadeDeRepeticoes):
    resultado = 1 / (6 + resultado)
print(f'{3 + resultado:.10f}')
