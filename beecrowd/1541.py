1541
'''Coletar três valores que indicam as medidas da casa e a porcentagem de ocupação de um terreno nesse bairro'''
while True:
    try:
        medida1, medida2, porcentagem = map(int,input().split())
        areaNecessaria = medida1 * medida2
        tamanhoTerreno = areaNecessaria * (100 / porcentagem)
        tamanhoLadoTerreno = tamanhoTerreno ** 0.5
        print(f'{int(tamanhoLadoTerreno)}')
    except ValueError:
        break
