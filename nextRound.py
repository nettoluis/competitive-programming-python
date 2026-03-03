quantidadeParticipantes, lugarCorte = map(int,input().split())
recordesParticipantes = [int(x) for x in input().split()]
recordeCorte, vencedores = recordesParticipantes[lugarCorte - 1], 0
for participante in recordesParticipantes:
    if participante >= recordeCorte and participante > 0:
        vencedores += 1
print(vencedores)
