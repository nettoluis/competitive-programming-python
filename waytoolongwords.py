quantidadePalavras = int(input())
for palavra in range(quantidadePalavras):
    palavra = input()
    if len(palavra) <= 10:
        print(palavra)
    else:
        print(f'{palavra[0]}{len(palavra) - 2}{palavra[-1]}')
