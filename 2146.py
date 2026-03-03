2146
'''Coletar um número e retornar o antecessor dele'''
while True:
    try:
        senhaEscrita = int(input())
        print(senhaEscrita - 1)
    except EOFError:
        break