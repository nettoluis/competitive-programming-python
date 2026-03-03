2523
'''Coletar uma string e concatenar as letras escolhidas e imprimí-las'''
while True:
    try:
        letras = input()
        quantidadeLetras = int(input())
        escolhasLetras = [int(x) for x in input().split()]
        print(''.join(letras[i - 1] for i in escolhasLetras))
    except EOFError:
        break