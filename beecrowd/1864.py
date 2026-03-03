1864
"""Coletar a quantidade de letras da citação de Soren Kierkegaard 'Life is not a problem to be solved'."""
quantidadeLetras,citacaoKierkegaard = int(input()), 'LIFE IS NOT A PROBLEM TO BE SOLVED.'
print(f"{''.join(str(citacaoKierkegaard[i]) for i in range(quantidadeLetras))}")