'''Coletar a quantidade de termos da sequência de Fibonacci ao contrário'''
quantidadeTermos = int(input())
Fib = [1,1]
for ciclo in range(quantidadeTermos - 2):
    Fib.append(Fib[-1] + Fib[-2])
print(' '.join(str(Fib[i]) for i in range(len(quantidadeTermos) - 1, -1, -1)))
