1150
"""Coletar dois números e indicar quantos números sucessivos o primeiro precisa para superar o segundo"""
A, B = int(input()), int(input())
while B <= A:
    B = int(input())
soma, contagem = A, 1
while soma <= B:
    soma += A + contagem
    contagem += 1
print(contagem)