qtdTestes = int(input())

for _ in range(qtdTestes):
    a, b = [int(numero) for numero in input().split()]
    diferencaDecimal = -((b - a)) // 10 if (b - a) < 0 else (b - a) // 10
    diferencaMenor = 1 if not not(b - a) % 10 else 0
    print(diferencaDecimal + diferencaMenor)
