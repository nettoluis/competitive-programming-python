1173
"""Coletar um valor que será armazenado no vetor X[0] e todos os X[i] subsequentes serão o dobro do anterior"""
num, contador = int(input()), 0
while contador < 10:
    print(f'X[{contador}] = {num}')
    num *= 2
    contador += 1