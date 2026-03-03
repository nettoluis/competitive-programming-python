def main():
    primeiroNumero, segundoNumero, resultado = input(), input(), ''
    for i in range(len(primeiroNumero)):
        resultado += '1' if primeiroNumero[i] != segundoNumero[i] else '0'
    print(resultado)
main()
