anoEscolhido = int(input()) + 1
def caracteresDistintos(ano):
    while True:
        string = str(ano)
        if len(set(string)) == len(string):
            print(ano)
            break
        else:
            ano += 1
caracteresDistintos(anoEscolhido)   
