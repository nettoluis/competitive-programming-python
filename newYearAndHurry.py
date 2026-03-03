quantidadeQuestoes, minutos = [int(x) for x in input().split()]
tempoMaximo = 240
tempoRestante = tempoMaximo - minutos
questoesResolvidas = 0

for questao in range(1, quantidadeQuestoes + 1):
    if questao * 5 <= tempoRestante:
        tempoRestante -= questao * 5
        questoesResolvidas += 1

print(questoesResolvidas)    
