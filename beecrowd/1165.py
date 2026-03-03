1165
"""Coletar um número inteiro que indica a quantidade de números analisados. Depois, analisar se determinada quantidade de números é primo ou não"""
qtdDeAnalises = int(input())
for _ in range(1,qtdDeAnalises + 1):
    dividendo, divisor, qtdDivisores = int(input()), 1, []
    for divisor in range(1, dividendo + 1, 1):
        qtdDivisores.append(divisor) if dividendo % divisor == 0 else None
    print(f'{dividendo} eh primo')if len(qtdDivisores) <= 2 else print(f'{dividendo} nao eh primo')