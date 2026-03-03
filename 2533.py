2533
#Coletar as notas e as cargas horárias de um estudante e aplicar a fórmula especificada
while True:
    try:
        quantidadeMaterias, operacaoUm, operacaoDois = int(input()), 0, 0
        for _ in range(quantidadeMaterias):
            nota, cargaHoraria = [int(x) for x in input().split()]
            operacaoUm += nota * cargaHoraria
            operacaoDois += cargaHoraria
        print(f'{operacaoUm /(operacaoDois * 100):.4f}')
    except EOFError:
        break