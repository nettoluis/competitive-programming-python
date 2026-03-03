def main():
    restante = int(input())
    tempoA, tempoB = [int(x) for x in input().split()]

    soma = tempoA + tempoB

    print(f'Deixa para amanha!') if soma > restante else print(f'Farei hoje!')


main()
