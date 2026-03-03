def contaTeclasAte(limite):
    teclas = 0
    for i in range(1, 10):
        for j in [1, 11, 111, 1111]:
            numero = i * j
            teclas += len(str(numero))
            if numero == limite:
                return teclas

            
def main():
    qtd = int(input())

    for _ in range(qtd):
        limite = int(input())
        teclas = contaTeclasAte(limite)
        print(teclas)


main()
