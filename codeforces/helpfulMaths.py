numerosASeremSomados : list[int] = sorted([int(num) for num in input().split('+')])
print('+'.join(str(numerosASeremSomados[elemento]) for elemento in range(len(numerosASeremSomados))))
