1159
"""O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o matriz da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20."""
while True:
    num = int(input())
    if num == 0:
        break
    else:
        soma,qtdPares = 0,5
        while qtdPares > 0:
            if num % 2 == 0:
                soma += num
                num += 2
                qtdPares -= 1
            else:
                num += 1
        print(soma)