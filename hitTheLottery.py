def contabilizadorNotas(qtd):
    notas, contador = [100, 20, 10, 5, 1], 0
    for nota in notas:
        while qtd >= nota:
            qtd -= nota
            contador += 1
        else:
            continue
    return contador
def main():
    dinheiro = int(input())

    print(contabilizadorNotas(dinheiro))
main()    
