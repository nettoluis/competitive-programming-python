def endancamentoDaSentenca(sentenca):
    sentencaDancante = ''
    anteriorMaiuscula = False
    for i in range(len(sentenca)):
        atual = sentenca[i]
        if atual != ' ' and not anteriorMaiuscula:
            sentencaDancante += atual.upper()
            anteriorMaiuscula = True
        else:
            sentencaDancante += atual
            if atual != ' ': anteriorMaiuscula = False

    return sentencaDancante


def main():
    while True:
        try:
            sentenca = input().lower()
            
            dancante = endancamentoDaSentenca(sentenca)

            print(dancante)
        except EOFError:
            break


main()
