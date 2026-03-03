def timesRepetidos(sequencia, vezes):
    limiteParticipacoes = 5 - vezes
    participantesDisponiveis = 0
    for elemento in sequencia:
        if elemento <= limiteParticipacoes:
            participantesDisponiveis += 1
    return participantesDisponiveis


def main():
    quantidade, vezes = [int(x) for x in input().split()]
    participacoes = [int(x) for x in input().split()]

    participantes = timesRepetidos(participacoes, vezes)

    print(participantes // 3)


main()
