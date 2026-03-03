preco, moedas = [int(x) for x in input().split()]

qtd = 1
while True:
    if (preco * qtd) % 10 == 0 or (preco * qtd) % 10 == moedas:
        break
    else:
        qtd += 1
print(qtd)
