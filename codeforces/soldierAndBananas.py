precoBananaOriginal, dinheiro, quantidadeBananas = [int(x) for x in input().split()]
dinheiroNecessario = int((precoBananaOriginal + (precoBananaOriginal * quantidadeBananas)) * (quantidadeBananas / 2))
print(dinheiroNecessario - dinheiro) if dinheiroNecessario > dinheiro else print(0)
