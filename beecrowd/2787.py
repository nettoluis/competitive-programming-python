def main():
    linhas = int(input())
    colunas = int(input())

    resultado = int(not((linhas + colunas) % 2))

    print(resultado)


main()
