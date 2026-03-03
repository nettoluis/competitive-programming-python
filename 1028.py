1028
'''Coletar a quantidade de casos testes. Posteriormente, coletar duas quantidades de figurinhas. Retornar o MDC entre eles'''
def calcularMDC(a, b):
    while b:
        a, b = b, a % b
    return a
quantidadeCasosTeste = int(input())
for caso in range(quantidadeCasosTeste):
    numeroUm, numeroDois = [int(x) for x in input().split()]
    print(calcularMDC(numeroUm, numeroDois))