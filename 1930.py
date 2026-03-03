1930
"""Coletar quantas tomadas disponíveis, sabendo que cada uma das anteriores terá uma ocupada para adicionar uma linha de tomada a mais"""
t1, t2, t3, t4 = map(int, input().split())
tomadasDisponiveis = (t1 - 1) + (t2 - 1) + (t3 - 1) + t4
print(tomadasDisponiveis)