def main():
    n = int(input())

    saida = ""
    
    pares = []
    for i in range(2, n + 1, 2):
        pares.append(i)

    impares = []
    for i in range(1, n+1, 2):
        impares.append(i)

    if n == 1:
        print(1)
    elif 2 <= n <= 3:
        print("NO SOLUTION")
    else:
        saida = " ".join(str(par) for par in pares) + " " + " ".join(str(impar) for impar in impares)

        print(saida)

main()
