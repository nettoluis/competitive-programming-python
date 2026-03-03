1118
'''Coletar um par de valores para calcular a média semestral de um aluno. Ao final, perguntar ao usuário se ele quer fazer um novo cálculo '''
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
        print('novo calculo (1-sim 2-nao)')
    except:
        continue
    else:
        decisaoUsuario = int(input())
        match decisaoUsuario:
            case 1:
                continue
            case 2:
                break
            case _:
                print('novo calculo (1-sim 2-nao)')
                decisaoUsuario = int(input())