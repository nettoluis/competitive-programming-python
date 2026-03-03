1160
"""Coletar a quantidade de casos que serão analisados. Posteriormente, coletar a população de A, população de B, taxa de crescimento de A e taxa de crescimento de B. Depois disso, informar quantos anos serão necessários para a população de A ULTRAPASSAR a população de B. Em casos que esse tempo for maior que 100 anos, informar 'Mais de 1 seculo'."""
qtd = int(input())
for _ in range(1, qtd + 1):
    populacaoA, populacaoB, taxaA, taxaB = map(float,input().split())
    populacaoA,populacaoB, taxaA, taxaB, anosNecessarios = int(populacaoA), int(populacaoB), taxaA / 100.00, taxaB / 100.00, 0
    while populacaoA <= populacaoB and anosNecessarios <= 100:
        populacaoA += (populacaoA * taxaA)
        populacaoB += (populacaoB * taxaB)
        populacaoA, populacaoB = int(populacaoA), int(populacaoB)
        anosNecessarios += 1
        if populacaoA > populacaoB or anosNecessarios > 100:
            break
    print(f'{anosNecessarios} anos.') if anosNecessarios <= 100 else print('Mais de 1 seculo.')