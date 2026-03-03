numeroAnalisado = input()
contador4, contador7 = numeroAnalisado.count('4'), numeroAnalisado.count('7')
quantidadeNumerosSorte = contador4 + contador7
print('YES') if (quantidadeNumerosSorte == 4) or (quantidadeNumerosSorte == 7) else print('NO')
