1962
'''Coletar um número inteiro que indica a quantidade de casos a serem analisados. Posteriomente, indicar em que ano aconteceu determinado evento sabendo há quanto tempo ocorreu'''
qtdDeCasos = int(input())
for _ in range(qtdDeCasos):
    tempoTranscorrido = int(input())
    anoOcorrencia = (2015 - tempoTranscorrido) if tempoTranscorrido < 2015 else (2015 - (tempoTranscorrido) + 1) if tempoTranscorrido == 2015 else ((tempoTranscorrido + 1) - 2015)
    print(f'{abs(anoOcorrencia)} D.C.') if tempoTranscorrido < 2015 else print(f'{anoOcorrencia} A.C.')