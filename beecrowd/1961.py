1961
'''Coletar a altura do pulo do sapo e a quantidade de canos. Posteriormente verificar se a diferença absoluta entre a altura do cano posterior e a do cano anterior é ,no máximo, igual à altura do pulo do sapo'''
alturaPulo, quantidadeCanos = map(int,input().split())
alturasCanos = list(map(int,input().split()))
for i in range(len(alturasCanos) - 1):
    if abs(alturasCanos[i + 1] - alturasCanos[i]) > alturaPulo:
        vitoria = 0
        break
    else:
        vitoria = 1
print('YOU WIN') if vitoria == 1 else print('GAME OVER')