def converteHexa(num):
    letras = {
        1 : 'A',
        2 : 'B',
        3 : 'C',
        4 : 'D',
        5 : 'E',
        6 : 'F',
}

    if num < 10:
        return str(num)
    else:
        return letras[num % 9]


def converteOctal(num):
    if num < 8:
        return str(num)
    else:
        return f'{num // 8}{num % 8}'
            

def criaLinha(texto, largura, indentacao=8, meio=False, resultados = False, borda='|', preenchimento=' '):     
    restante = largura - (indentacao + len(texto))
    if not resultados:
        linha = f'{borda}{preenchimento * indentacao}{texto}{preenchimento * restante}{borda}' if meio else f'{preenchimento * indentacao}{texto}{preenchimento * restante}'
    else:    
        linha = f'{borda}{preenchimento * restante}{texto}{preenchimento * indentacao}{borda}' if meio else f'{preenchimento * restante}{texto}{preenchimento * indentacao}'

    return linha


def main():
    largura = 37
    cabecalho = '-' * 39
    print(cabecalho) 
    print(criaLinha(criaLinha('decimal', 11, 2) + criaLinha('octal', 9, 2, True) + criaLinha('Hexadecimal', 15, 2), largura, 0, True))
    print(cabecalho)
    for num in range(16):
        print(criaLinha(criaLinha(str(num), 11, 4, False, True) + criaLinha(f'{converteOctal(num)}', 9, 4, True, True) + criaLinha(f'{converteHexa(num)}', 15, 7, False, True), largura, 0, True))

    print(cabecalho)
main()
