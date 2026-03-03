quantidadePoliedros, soma = int(input()), 0
for poliedro in range(quantidadePoliedros):
    poliedro = input()
    match poliedro:
        case 'Tetrahedron':
            soma += 4
        case 'Cube':
            soma += 6
        case 'Octahedron':
            soma += 8
        case 'Dodecahedron':
            soma += 12
        case 'Icosahedron':
            soma += 20
print(soma)
