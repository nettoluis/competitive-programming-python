quantidadeCasos = int(input())
for caso in range(quantidadeCasos):
    dividendo, divisor = [int(num) for num in input().split()]
    resto = dividendo % divisor
    if resto == 0:
        print(0)
    elif resto > divisor:
        print(resto - divisor)
    else:
        print(divisor - resto)
