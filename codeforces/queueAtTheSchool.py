quantidadeAlunos, tempoDecorrido = [int(dado) for dado in input().split()]
organizacaoFila = [genero for genero in input()]
for troca in range(tempoDecorrido):
    i = 0
    while i < (quantidadeAlunos-1):
        if organizacaoFila[i] == 'B' and organizacaoFila[i + 1] == 'G':
            organizacaoFila[i], organizacaoFila[i + 1] = 'G', 'B'
            i += 2
        else:
            i += 1
print(''.join(organizacaoFila))
