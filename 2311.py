2311
'''Coletar a quantidade de participantes. Depois coletar o nome da participante, o grau de dificuldade, e a lista de notas. Por fim, imprimir o nome seguido das notas com duas casas decimais de precisão.'''
quantidadeParticipantes = int(input())
for _ in range(quantidadeParticipantes):
    nome = input()
    grauDificuldade = float(input())
    listaNotas = list(map(float, input().split()))
    listaNotas.remove(max(listaNotas))
    listaNotas.remove((min(listaNotas)))
    print(f'{nome} {sum(listaNotas) * grauDificuldade:.2f}')