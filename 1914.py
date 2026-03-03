1914
'''Coletar o número de partidas e indicar quem ganha o par ou impar'''
qtdPartidas = int(input())
for _ in range(qtdPartidas):
    dadosPartida = list(input().split())
    jogadaUm, jogadaDois = map(int,input().split())
    print(f'{dadosPartida[dadosPartida.index("PAR") - 1]}')if (jogadaUm + jogadaDois) % 2 == 0 else print(f'{dadosPartida[dadosPartida.index("IMPAR") - 1]}')