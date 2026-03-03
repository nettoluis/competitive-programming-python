def bubbleSort(sequencia, tamanhoSequencia):
    mudancas = 0
    for i in range(tamanhoSequencia - 1):
        if sequencia[i] > sequencia[i + 1]:
            swap(sequencia, i, i + 1)
            mudancas += 1
    
    if mudancas > 0:
        bubbleSort(sequencia, tamanhoSequencia - 1)

            
def swap(sequencia, i1, i2):
     temp = sequencia[i1]
     sequencia[i1] = sequencia[i2]
     sequencia[i2] = temp

def testes():
    lista = [30, 30, 40, 250, 100, 15]
    bubbleSort(lista, len(lista))
    assert lista == [15, 30, 30, 40, 100, 250]

if __name__ == '__main__':
    testes()
