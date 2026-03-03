2235
'''Coletar os três créditos de viagem no tempo e indicar se é possível ir no futuro e voltar para o presente fazendo, pelo menos, uma viagem e, no máximo, três'''
listaCreditos = sorted(int(x) for x in input().split())
a, b, c = listaCreditos[0], listaCreditos[1], listaCreditos[2]
print('S') if a == b or b == c or a + b == c else print('N')