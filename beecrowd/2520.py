2520
'''Criar um matriz e indicar a distância entre dois pontos'''
while True:
    try:
        quantidadeLinhas, quantidadeColunas = [int(x) for x in input().split()]
        matriz = []
        for linha in range(quantidadeLinhas):
            linha = [int(x) for x in input().split()]
            matriz.append(linha)
        for i in range(quantidadeLinhas):
            if 2 in matriz[i]:
                xPokemon, yPokemon = i, matriz[i].index(2)
            if 1 in matriz[i]:
                xAsh, yAsh = i, matriz[i].index(1)
        print(f'{abs(xAsh - xPokemon) + abs(yAsh - yPokemon)}')
    except EOFError:
        break