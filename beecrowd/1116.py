1116
'''Coletar um número inteiro que indicará a quantidade de casos testes. Posteriormente, realizar a divisão de um número por outro'''
numCasosTestes = int(input())
for _ in range(1,numCasosTestes + 1):
    x, y = map(int,input().split())
    try:
        print(f'{x/y:.1f}')
    except:
        print('divisao impossivel')