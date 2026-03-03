2059
'''Analisar um jogo de par ou ímpar'''
par, jogadaUm, jogadaDois, roubou, acusouRoubo = map(int, input().split())
soma = jogadaUm + jogadaDois
jogador1Ganha = False
if (par == 1 and soma % 2 == 0) or (par == 0 and soma % 2 != 0):
    jogador1Ganha = True
if roubou == 1:
    if acusouRoubo == 1:
        jogador1Ganha = False
    else:
        jogador1Ganha = True
elif acusouRoubo == 1:
    jogador1Ganha = True
if jogador1Ganha:
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')