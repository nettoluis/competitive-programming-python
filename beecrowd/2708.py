def main():
    turistas, jipes = 0, 0
    while True:
        entrada = input().split()
        if entrada == ['ABEND']: break
        movimento, qtd = entrada[0], int(entrada[1])
        
        if movimento == 'SALIDA':
            turistas += qtd
            jipes += 1
        else:
            turistas -= qtd
            jipes -= 1

    print(turistas)
    print(jipes)
        

main()
