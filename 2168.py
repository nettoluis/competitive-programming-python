2168
'''Coletar as matrizes que representam as quadras de Portland e indicar se são seguras ou não'''
ordemMatriz = int(input())
matriz = []
for _ in range(ordemMatriz + 1):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
for i in range(ordemMatriz):
    mensagem = ''
    for j in range(ordemMatriz):
        quantidadeCameras = 0
        if matriz[i][j] == 1:
            quantidadeCameras += 1
        if matriz[i][j + 1] == 1:
            quantidadeCameras += 1
        if matriz[i + 1][j] == 1:
            quantidadeCameras += 1
        if matriz[i + 1][j + 1] == 1:
            quantidadeCameras += 1
        if quantidadeCameras >= 2:
            mensagem += 'S'
        else:
            mensagem += 'U'
    print(mensagem)