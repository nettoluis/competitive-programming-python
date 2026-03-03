def analise(p1, p2, mishka, chris):
    if p1 > p2:
        mishka += 1
    elif p1 < p2:
        chris += 1
    else:
        mishka += 1
        chris += 1

    return mishka, chris


def main():
    qtdRodadas = int(input())

    mishka, chris = 0, 0
    for _ in range(qtdRodadas):
        p1, p2 = [int(resultado) for resultado in input().split()]
        mishka, chris = analise(p1, p2, mishka, chris)

    print('Mishka') if mishka > chris else print('Chris') if chris > mishka else print('Friendship is magic!^^')


main()
