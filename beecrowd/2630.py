2630
'''Coletar a quantidade de casos testes. Posteriormente, coletar qual o tipo de operação vai ser realizada com as escalas de vermelho, verde e azul. Por fim, indicar o valor de P.'''
quantidadeCasos = int(input())
for caso in range(quantidadeCasos):
    operacao = input()
    escalaVermelho, escalaVerde, escalaAzul = [int(x) for x in input().split()]
    print(f'Caso #{caso + 1}: {int((30/100 * escalaVermelho) + (59/100 * escalaVerde) + (11/100 * escalaAzul)):.0f}') if operacao == 'eye' else print(f'Caso #{caso + 1}: {int((escalaVermelho + escalaVerde + escalaAzul)/3)}') if operacao == 'mean' else print(f'Caso #{caso + 1}: {min(escalaVermelho,escalaVerde,escalaAzul)}') if operacao == 'min' else print(f'Caso #{caso + 1}: {max(escalaVermelho,escalaVerde,escalaAzul)}')