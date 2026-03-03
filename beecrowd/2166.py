2166
'''Coletar a quantidade de repetições da fração para adicionar acurácia ao resultado da raiz de 2'''
quantidadeFracoesPeriodicasContinuadas, resultadoFracionario = int(input()), 0
for _ in range(quantidadeFracoesPeriodicasContinuadas):
    resultadoParcial = 1/ (2 + resultadoFracionario)
    resultadoFracionario = resultadoParcial
print(f'{1 + resultadoFracionario:.10f}')
