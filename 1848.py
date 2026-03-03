1848
"""Coletar os números da loteria de acordo com as piscadas em binário de um corvo no universo de Game Of Thrones"""
for _ in range(3):
    valorLoteria = 0
    while True:
        acaoCorvo = input()
        if acaoCorvo == 'caw caw':
            break
        else:
            valorLoteria += 1 if acaoCorvo == '--*' else 2 if acaoCorvo == '-*-' else 3 if acaoCorvo == '-**' else 4 if acaoCorvo == '*--' else 5 if acaoCorvo == '*-*' else 6 if acaoCorvo == '**-' else 7
    print(f'{valorLoteria}')