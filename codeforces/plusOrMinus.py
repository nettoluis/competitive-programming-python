quantidadeTestes = int(input())

for _ in range(quantidadeTestes):
    fatorUm, fatorDois, resultado = [int(x) for x in input().split()]
    print('+') if fatorUm + fatorDois == resultado else print('-')
