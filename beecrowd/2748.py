def constroiLinha(texto, largura, borda='|', indentacao=8, preenchimento=' '):     
    restante = largura - (indentacao + len(texto))
    linha = f'{borda}{preenchimento * indentacao}{texto}{preenchimento * restante}{borda}'

    return linha


def main():
    largura = 37
    print('-' * 39)
    
    print(constroiLinha('Roberto', largura))
    print(constroiLinha('', largura))
    print(constroiLinha('5786', largura))
    print(constroiLinha('', largura))
    print(constroiLinha('UNIFEI', largura))

    print('-' * 39)
main()
