2310
'''Coletar a quantidade de jogadores que vão ser analisados. Posteriormente, coletar o nome do jogador, a quantidade de tentativas de saque, bloqueio e ataque e a quantidade de acertos de cada'''
quantidadeJogadores = int(input())
tentativasSaquesTotal, tentativasBloqueiosTotal, tentativasAtaquesTotal ,acertosSaquesTotal, acertosBloqueiosTotal, acertosAtaquesTotal = 0, 0, 0, 0, 0, 0
for _ in range(quantidadeJogadores):
    nome = input()
    saqueTentativas, bloqueioTentativas, ataqueTentativas = map(int, input().split())
    saqueAcertos, bloqueioAcertos, ataqueAcertos = map(int, input().split())
    tentativasSaquesTotal += saqueTentativas
    tentativasBloqueiosTotal += bloqueioTentativas
    tentativasAtaquesTotal += ataqueTentativas
    acertosSaquesTotal += saqueAcertos
    acertosBloqueiosTotal += bloqueioAcertos
    acertosAtaquesTotal += ataqueAcertos
print(f'Pontos de Saque: {(acertosSaquesTotal/ tentativasSaquesTotal) * 100:.2f} %.\nPontos de Bloqueio: {(acertosBloqueiosTotal/ tentativasBloqueiosTotal) * 100:.2f} %.\nPontos de Ataque: {(acertosAtaquesTotal/ tentativasAtaquesTotal) * 100:.2f} %.')

