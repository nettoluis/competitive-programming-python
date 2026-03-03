def encontrarDiferente():
    primeiro, segundo, terceiro = [int(numero) for numero in input().split()]
    if primeiro == segundo:
        return terceiro
    if primeiro == terceiro:
        return segundo
    if segundo == terceiro:
        return primeiro

def main():
    quantidadeCasos = int(input())

    for _ in range(quantidadeCasos):
        print(encontrarDiferente())


main()
