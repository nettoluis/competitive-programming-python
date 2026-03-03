1175
"""Coletar vinte valores inteiros e imprimir suas posições invertidas, ou seja, o último com primeiro e assim por diante"""
listaVetor, contador = [], 19
while contador >= 0:
     num = int(input())
     listaVetor.insert(0,f'N[{contador}] = {num}')
     contador -= 1
if len(listaVetor) == 20:
    for i in range(len(listaVetor)):
         print(listaVetor[i])
1175.2
nums = [int(input()) for _ in range(20)]
nums.reverse()
for i in range(20):
    print(f'N[{i}] = {nums[i]}')