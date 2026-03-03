qtdNumeros = int(input())

for _ in range(qtdNumeros):
    numero = input()
    soma = 0
    for digito in numero:
        soma += int(digito)
    print(soma)
