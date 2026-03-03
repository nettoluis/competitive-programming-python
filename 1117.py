1117
'''Coletar um par de valores para calcular a média semestral de um aluno '''
while True:
    nota1, nota2 = float(input()), float(input())
    while nota1 < 0 or nota1 > 10:
        print('nota invalida')
        nota1 = float(input())
    while nota2 < 0 or nota2 > 10:
        print('nota invalida')
        nota2 = float(input())
    try:
        print(f'media = {((nota1 + nota2)/ 2):.2f}')
    except:
        print('nota invalida')
    else:
        break



