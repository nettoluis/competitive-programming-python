2505
'''Coletar um número e retornar se ele é autopotencial ou não'''
while True:
    try:
        numeroAnalisado = int(input())
        tamanho = len(str(numeroAnalisado))
        mod = 10 ** tamanho
        resultado = pow(numeroAnalisado, numeroAnalisado, mod)
        print('SIM' if resultado == numeroAnalisado else 'NAO')
    except EOFError:
        break