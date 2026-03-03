def constroiLinha(texto, largura, indentacao=8, borda='|', preenchimento=' '):     
    restante = largura - (indentacao + len(texto))
    linha = f'{borda}{preenchimento * indentacao}{texto}{preenchimento * restante}{borda}'

    return linha


def main():
    largura = 37
    print('-' * 39)
    
    print(constroiLinha('x = 35', largura, 0))
    print(constroiLinha('', largura))
    print(constroiLinha('x = 35', largura, 15))
    print(constroiLinha('', largura))
    print(constroiLinha('x = 35', largura, 31))

    print('-' * 39)
main()
