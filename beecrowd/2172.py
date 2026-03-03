2172
'''Coletar o multiplicador e o valor a se multiplicado e imprim-i-lo'''
while True:
    multiplicador, multiplicado = map(int,input().split())
    if multiplicador == 0 and multiplicado == 0:
        break
    else:
        print(f'{multiplicador * multiplicado}')