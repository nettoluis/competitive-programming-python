2031
'''Coletar a quantidade de partidas a serem jogadas. Posteriormente indicar quem ganhou'''
quantidadePartidas = int(input())
comoGanhar = {
    'ataque': ['pedra','papel'],
    'pedra': ['papel'],
    'papel': ['']
}
for _ in range(quantidadePartidas):
    jogadorUm, jogadorDois = input(), input()
    if jogadorUm == 'papel' and jogadorDois == 'papel':
        print('Ambos venceram')
    elif jogadorDois in comoGanhar[jogadorUm]:
        print('Jogador 1 venceu')
    elif jogadorUm in comoGanhar[jogadorDois]:
        print('Jogador 2 venceu')
    elif jogadorUm == 'ataque' and jogadorDois == 'ataque':
        print('Aniquilacao mutua')
    else:
        print('Sem ganhador')
