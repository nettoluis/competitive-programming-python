def main():
    qtd = int(input())

    hobbits, humanos, elfos, anoes, magos = 0, 0, 0, 0, 0
    for _ in range(qtd):
        nome, raca = input().split()
        match raca:
            case "X":
                hobbits += 1
            case "M":
                magos += 1
            case "H":
                humanos += 1
            case "E":
                elfos += 1
            case "A":
                anoes += 1

    print(f'{hobbits} Hobbit(s)\n{humanos} Humano(s)\n{elfos} Elfo(s)\n{anoes} Anao(oes)\n{magos} MAgo(s)')


main()
