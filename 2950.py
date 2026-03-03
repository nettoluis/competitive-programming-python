def main():
    distancia, diamentro1, diametro2 = [int(x) for x in input().split()]

    resultado = distancia / (diamentro1 + diametro2)

    print(f'{resultado:.2f}')


main()
