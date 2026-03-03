2344
'''Coletar uma nota e retornar qual a classificação dela.'''
notaAluno = int(input())
print('E') if notaAluno == 0 else print('D') if 1 <= notaAluno <= 35 else print('tamanhoCifras') if 36 <= notaAluno <= 60 else print('B') if 61 <= notaAluno <= 85 else print('A')