2547
'''Coletar a quantidade de visitantes, altura minima e altura maxima do brinquedo. Posteriormente, indicar quantos desses podem brincar'''
while True:
    try:
        quantidadeVisitantes, alturaMinima, alturaMaxima = [int(x) for x in input().split()]
        visitantesPermitidos = 0
        for _ in range(quantidadeVisitantes):
            alturaVisitante = int(input())
            if alturaMinima <= alturaVisitante <= alturaMaxima:
                visitantesPermitidos += 1
        print(visitantesPermitidos)
    except EOFError:
        break