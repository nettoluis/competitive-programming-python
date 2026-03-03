2167
'''Coletar um número inteiro que indica a quantidade de velocidades coletadas. Posteriormente indicar qual coleta indica uma redução de velocidade'''
quantidadeColetas = int(input())
listaVelocidades, localizacao = [int(x) for x in input().split()], 0
for i in range(0, quantidadeColetas - 1):
    if listaVelocidades[i] > listaVelocidades[i + 1]:
        localizacao = i + 2
        break
print(localizacao)