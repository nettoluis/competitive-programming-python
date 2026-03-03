def main():
    qtd = int(input())

    for _ in range(qtd):
        tamanho, fator = map(int, input().split())
        s, t = [int(x) for x in input().split()], [int(x) for x in input().split()]

        

        print('YES') if sorted(s) == sorted(t) else print('NO')


main()
