2163
'''Coletar a quantidade de linhas e de colunas de um matriz. Indicar qual a posição do sabre de luz sabendo que ele é um 42 cercado por 7s'''
quantidadeLinhas, quantidadeColunas = map(int, input().split())
matriz = []
for _ in range(quantidadeLinhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)
sabreEncontrado, resultado = False, '0 0'
for linha in range(1, quantidadeLinhas - 1):
    for coluna in range(1, quantidadeColunas - 1):
        if matriz[linha][coluna] == 42:
            if (matriz[linha - 1][coluna - 1] == 7 and
                matriz[linha - 1][coluna] == 7 and
                matriz[linha - 1][coluna + 1] == 7 and
                matriz[linha][coluna - 1] == 7 and
                matriz[linha][coluna + 1] == 7 and
                matriz[linha + 1][coluna - 1] == 7 and
                matriz[linha + 1][coluna] == 7 and
                matriz[linha + 1][coluna + 1] == 7):
                sabreEncontrado = True
                resultado = f"{linha + 1} {coluna + 1}"
                break
    if sabreEncontrado:
        break
print(resultado)