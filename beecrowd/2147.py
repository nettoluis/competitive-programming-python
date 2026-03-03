2147
'''Coletar a quantidade de casos testes. Posteriormente, coletar a quantidade de letras de uma palavra e retornar a quantidade de tempo que demorou para ser digitada sabendo que cada letra demora cerca de um centesimo de segundo para ser teclada'''
quantidadeCasos = int(input())
for _ in range(quantidadeCasos):
    palavra = input()
    print(f'{len(palavra)/100:.2f}')