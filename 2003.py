2003
'''Coletar vários horários e indicar o atraso máximo de um rapaz sabendo que ele pode demorar até 1 hora pra se arrumar e precisa estar em um ponto de ônibus às 8h00. Além disso, o programa acaba em EOF'''
while True:
    try:
        hora, minuto = map(int,input().split(':'))
        atrasoCalculo = (((hora * 60) + (minuto + 60)) - 480)
        print(f'Atraso maximo: {atrasoCalculo}') if atrasoCalculo > 0 else print(f'Atraso maximo: 0')
    except EOFError:
        break