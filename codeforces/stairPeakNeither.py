def pico(a, b, c):
    if a < b > c:
        return True
    
    return False


def escada(a, b, c):
    if a < b < c:
        return True
    
    return False


def main():
    qtd = int(input())

    for _ in range(qtd):
        a, b, c = [int(x) for x in input().split()]
        if escada(a, b, c):
            print('STAIR')
        elif pico(a, b, c):
            print('PEAK')
        else:
            print('NONE')


main()
