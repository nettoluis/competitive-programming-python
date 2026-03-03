def formaNovasPalavras(palavras):
    novasPalavras = ''
    for i in range(len(palavras)):
        caractere = palavras[i]
        if i == 4: 
            caractere = palavras[0]       
        if i == 0: 
            caractere = palavras[4]
        novasPalavras += caractere

    return novasPalavras


def main():
    quantidadeEntradas = int(input())
    
    for _ in range(quantidadeEntradas):
        palavras = input()
        novasPalavras = formaNovasPalavras(palavras)
        print(novasPalavras)


main()
