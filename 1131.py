1131
"""Coletar a quantidade de gols do Inter e do Grêmio em um Grenal e ao final perguntar se gostaria de fazer uma nova análise. Ao final de todas as análise, imprimir a quantidade de grenais, quantas vitorias do Inter, quantas vitórias do Grêmio, quantos empates e quem foi o maior vencedor e, se não tiver, imprimir 'Nao houve vencedor'"""
vitoriasInter,vitoriasGremio, empates, partidasAnalisadas = 0, 0, 0, 0
while True:
    golsInter, golsGremio = map(int, input().split())
    if golsInter > golsGremio:
        vitoriasInter += 1
    elif golsGremio > golsInter:
        vitoriasGremio += 1
    else:
        empates += 1
    partidasAnalisadas += 1
    recomecar = int(input('Novo grenal (1-sim 2-nao)\n'))
    if recomecar != 1:
        break
print(f'{partidasAnalisadas} grenais')
print(f'Inter:{vitoriasInter}\nGremio:{vitoriasGremio}\nEmpates:{empates}')
print('Inter venceu mais') if vitoriasInter > vitoriasGremio else print('Grêmio venceu mais') if vitoriasGremio > vitoriasInter else print('Nao houve vencedor')
