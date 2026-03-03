1983
'''Coletar um número inteiro que indica a quantidade de alunos. Posteriormente, verificar se algum deles atingiu a nota 8, se sim, indicar qual o aluno com maior nota e, se não, indicar que a nota mínima não foi alcançada'''
qtdAlunos,idAlunos, notaAlunos,notaMinima = int(input()), [], [], 0
for _ in range(qtdAlunos):
    idAluno, notaAluno = map(float, input().split())
    idAlunos.append(int(idAluno))
    notaAlunos.append(notaAluno)
for i in range(len(notaAlunos)):
    if notaAlunos[i] < 8:
        notaMinima += 0

    else:
        notaMaxima = notaAlunos.index(max(notaAlunos))
        alunoMaximo = idAlunos[notaMaxima]
        notaMinima += 1
print(alunoMaximo) if notaMinima > 0 else print('Minimum note not reached')

1983.2
'''Coletar um número inteiro que indica a quantidade de alunos. Posteriormente, verificar se algum deles atingiu a nota 8, se sim, indicar qual o aluno com maior nota e, se não, indicar que a nota mínima não foi alcançada'''
qtdAlunos, maiorNota, alunoMaiorNota = int(input()), -1, -1
for _ in range(qtdAlunos):
    idAluno, notaAluno = map(float, input().split())
    if notaAluno >= 8 and notaAluno > maiorNota:
        maiorNota = notaAluno
        alunoMaiorNota = int(idAluno)
if alunoMaiorNota != -1:
    print(alunoMaiorNota)
else:
    print('Minimum note not reached')