2139
'''Coletar o mês e o dia e indicar se é vespera de natal, já passou ou quantos dias faltam'''
while True:
    try:
        diasMeses = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mesEscolhido, diaEscolhido = map(int,input().split())
        diasDecorridos = sum(diasMeses[:mesEscolhido]) + diaEscolhido
        diasFaltam = 360 - diasDecorridos
        if diasFaltam > 1:
            print(f'Faltam {diasFaltam} dias para o natal!')
        elif diasFaltam == 1:
            print(f'E vespera de natal!')
        elif diasFaltam == 0:
            print(f'E natal!')
        else:
            print(f'Ja passou!')
    except EOFError:
        break