2313
'''Coletar os lados de um triangulo. Posteriormente, indicar se ele é válido, se sim, indicar qual a classificação quanto à congruência de seus lados e, por fim, indicar se ele é retângulo ou não'''
listaLados = sorted(list(map(int,input().split())))
a,b,c = listaLados[-3], listaLados[-2], listaLados[-1]
if a + b <= c:
    print('Invalido')
else:
    if a == b and b == c and c == a:
        print('Valido-Equilatero')
    elif a == b or b == c or c == a:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')
    if c ** 2 == (b ** 2) + (a ** 2):
        print('Retangulo: S')
    else:
        print('Retangulo: N')