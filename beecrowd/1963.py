1963
'''Coletar os dois valores do ingresso e retornar a porcentagem de aumento'''
valorAntigo, valorNovo = map(float,input().split())
print(f'{((valorNovo/valorAntigo) - 1) * 100:.2f}%')
