#Primeira resolução com set()
nome = input()
caracteresDistintos = set(nome)
print('CHAT WITH HER!') if len(caracteresDistintos) % 2 == 0 else print('IGNORE HIM!')
#Segunda resolução com lista e append -- Mais eficiente que o insert na primeira posição.
nome: str = input()
caracteresDistintos: list[str] = []
for char in nome:
    if char in caracteresDistintos:
        continue
    caracteresDistintos.append(char)
print('CHAT WITH HER!') if len(caracteresDistintos) % 2 == 0 else print('IGNORE HIM!')
