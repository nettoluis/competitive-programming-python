def descobreLetra(codigo, alfabeto):
    pontos, posicao = len(codigo[0]), len(codigo)
    return alfabeto[posicao][pontos - 1]


def main():
    alfabeto = {
        1 : 'abc',
        2 : 'def',
        3 : 'ghi',
        4 : 'jkl',
        5 : 'mno',
        6 : 'pqr',
        7 : 'stu',
        8 : 'vwx',
        9 : 'yz',
}
    while True:
        try:
            qtd = int(input())

            for _ in range(qtd):
                codigo = input().split()
                
                letra = descobreLetra(codigo, alfabeto)

                print(letra)
        except EOFError:
            break


main()
