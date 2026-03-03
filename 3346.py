3346
"""Coletar os dois fatores de flutuação do PIB, e retorna o fator de atualização"""
variacaoUm, variacaoDois = map(float,input().split())
variacaoCombinada = (((100 + variacaoUm) * (100 + variacaoDois)) / 100) - 100.00
print(f'{variacaoCombinada:.6f}')