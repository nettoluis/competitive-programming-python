1789
'''Coletar o número de lesmas que serão analisadas e retornar em qual nível de velocidade ela está'''
while True:
    try:
        quantidadeLesmas,velocidadesLesmas = int(input()), list(map(int,input().split()))
        print(3) if max(velocidadesLesmas) >= 20 else print(2) if max(velocidadesLesmas) >= 10 and max(velocidadesLesmas) < 20 else print(1)
    except EOFError:
        break
