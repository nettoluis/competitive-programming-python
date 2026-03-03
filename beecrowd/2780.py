def main():
    distancia = int(input())

    pontuacao = 0
    if distancia <= 800:
        pontuacao = 1
    elif 800 < distancia <= 1400:
        pontuacao = 2
    else:
        pontuacao = 3

    print(pontuacao)
        

main()
