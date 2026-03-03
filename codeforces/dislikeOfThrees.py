def gerarLista():
    lista = [] 
    for num in range(1, 1667):
        if (not not num % 3) and (num % 10 != 3):
            lista.append(num)
    return lista

        
def main():
    quantidadeNumeros = int(input())

    lista = gerarLista()
    for _ in range(quantidadeNumeros):
        i = int(input())
        print(lista[i - 1])


main()
