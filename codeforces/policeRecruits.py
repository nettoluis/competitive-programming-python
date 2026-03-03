quantidadeEventos = int(input())
crimes = 0
policiais = 0

eventos = [int(x) for x in input().split()]

for evento in eventos:
    if policiais == 0 and evento == -1:    
        crimes += 1
    elif evento >= 1:
        policiais += evento
    elif policiais > 0 and evento == -1:
        policiais -= 1

print(crimes)
