2221
'''Coletar a quantidade de partidas. Posteriormente, coletar o valor do bônus, os atributos de ataque, defesa e nível de Dabriel e depois de Guarte e, por fim, imprimir quem foi o vencedor ou se foi empate'''
quantidadePartidas = int(input())
for _ in range(quantidadePartidas):
    valorBonus = int(input())
    ataqueDabriel, defesaDabriel, nivelDabriel = map(int,input().split())
    ataqueGuarte, defesaGuarte, nivelGuarte = map(int,input().split())
    golpeDabriel, golpeGuarte = (ataqueDabriel + defesaDabriel) / 2, (ataqueGuarte + defesaGuarte) / 2
    if nivelDabriel % 2 == 0:
        golpeDabriel += valorBonus
    if nivelGuarte % 2 == 0:
        golpeGuarte += valorBonus
    if golpeDabriel > golpeGuarte:
        print('Dabriel')
    elif golpeGuarte > golpeDabriel:
        print('Guarte')
    else:
        print('Empate')