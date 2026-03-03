2543
'''Coletar a quantidade de videos e o identificador. Posteriormente, indicar qual a quantidade de vídeos desse identificador jogando Contra-strike'''
while True:
    try:
        quantidadeVideos, identificadorJogador = [int(x) for x in input().split()]
        videosJogador = 0
        for _ in range(quantidadeVideos):
            identificadorVideo, identificadorJogo = [int(x) for x in input().split()]
            if identificadorVideo == identificadorJogador and identificadorJogo == 0:
                videosJogador += 1
        print(videosJogador)
    except EOFError:
        break