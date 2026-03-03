2140
'''Coletar o valor a ser pago e a nota dada pelo cliente. Posteriormente, declarar se é possível o comerciante devolver o troco em apenas duas notas'''
notas = [100, 50, 20, 10, 5, 2]
while True:
    contador = 0
    valorCompra, valorPago = map(int,input().split())
    if valorCompra == 0 and valorPago == 0:
        break
    else:
        valorTroco = valorPago - valorCompra
        for nota in notas:
            if nota <= valorTroco:
                valorTroco -= nota
                contador += 1
        print('possible') if contador == 2 else print('impossible')