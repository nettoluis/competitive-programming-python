2126
'''Coletar uma sequencia e depois imprimir quantas vezes aquela primeira sequencia está presente na segunda e onde está a posição da segunda'''
caso = 1
while True:
    try:
        primeiraSequencia = input()
        segundaSequencia = input()

        contador = segundaSequencia.count(primeiraSequencia)

        if contador > 0:
            ultimaPosicao = segundaSequencia.rfind(primeiraSequencia)
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {contador}")
            print(f"Pos: {ultimaPosicao + 1}")
        else:
            print(f"Caso #{caso}:")
            print("Nao existe subsequencia")
        print()
        caso += 1
    except EOFError:
        break