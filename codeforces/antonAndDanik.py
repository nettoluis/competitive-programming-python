quantidadeJogos = int(input())
resultados = input()
vitoriasAnton, vitoriasDanik = [resultado for resultado in resultados if resultado == 'A'], [resultado for resultado in resultados if resultado == 'D']
print('Friendship') if (len(vitoriasAnton) == len(vitoriasDanik)) else print('Anton') if len(vitoriasAnton) > len(vitoriasDanik) else print('Danik')
