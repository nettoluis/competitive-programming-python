'''Coletar uma certa quantidade de melancias e indicar se é possível dividí-la em duas partes pares, independente de ser igual ou não.'''
quantidadeMelancias = int(input())
print('YES') if quantidadeMelancias % 2 == 0 and quantidadeMelancias != 2 else print('NO')
