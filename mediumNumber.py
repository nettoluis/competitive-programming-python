qtdTestes = int(input())

for _ in range(qtdTestes):
    a, b, c = [int(x) for x in input().split()]
    if (a > b and a < c) or (a < b and a > c):
        print(a)
    elif (a > b and b > c) or (a < b and b < c):
        print(b)
    else:
        print(c)
