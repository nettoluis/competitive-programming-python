2164
'''Coletar o número da localização de um número da sequência de Fibonnaci. Posteriormente, utilizar a fórmula de Binet para indicar qual é esse número com uma casa decimal de precisão'''
localizacao = int(input())
raizDe5 = 5 ** 0.5
fibonacci = ((((1 + raizDe5)/2) ** localizacao) - (((1 - raizDe5)/2) ** localizacao))/raizDe5
print(f'{fibonacci:.1f}')