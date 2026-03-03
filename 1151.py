1151
"""Coletar a quantidade de números que serão impressos seguindo a sequência de Fibonnaci"""
qtdNums = int(input())
fibs = [0,1]
while len(fibs) < qtdNums:
    fibs.append(fibs[-1] + fibs[-2])
print(f"{' '.join(str(fibs[i]) for i in range(len(fibs)))}")