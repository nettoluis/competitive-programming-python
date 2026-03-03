1124
'''Coletar a largura e comprimento de um elevador e os raios de dois cilidros e indicar se é possível colocar os dois juntos no elevador'''
import math

while True:
    larguraElevador, comprimentoElevador, raioUm, raioDois = [int(x) for x in input().split()]
    if larguraElevador == 0 and comprimentoElevador == 0 and raioUm == 0 and raioDois == 0:
        break
    diametroUm = raioUm * 2
    diametroDois = raioDois * 2
    L = max(larguraElevador, comprimentoElevador)
    W = min(larguraElevador, comprimentoElevador)
    possivel = False
    if (diametroUm + diametroDois <= L) and \
       (max(diametroUm, diametroDois) <= W):
        possivel = True
    elif (diametroUm + diametroDois <= W) and \
         (max(diametroUm, diametroDois) <= L):
        possivel = True
    elif (diametroUm <= W and diametroDois <= L):
        possivel = True
    elif (diametroDois <= W and diametroUm <= L):
        possivel = True
    print('S' if possivel else 'N')