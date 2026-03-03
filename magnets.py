quantidadeImas = int(input())
contadorFilas = 0
ultimoValor = 0
for ima in range(quantidadeImas):
    ima = input()
    contadorFilas += 1 if ima != ultimoValor else 0
    ultimoValor = ima
print(contadorFilas)
