meta, quantidade = [int(x) for x in input().split()]
maiorDivisor = int((meta ** 0.5) + 1)
atendem = 0
primos = []

eh_primo = [True] * (meta + 1)
eh_primo[0] = False
eh_primo[1] = False
for primo in range(2, int(meta ** 0.5) + 1):
    if eh_primo[primo]:
        for multiplo in range(primo * primo, meta + 1, primo):
            eh_primo[multiplo] = False
for i in range(2, meta + 1):
    if eh_primo[i]:
        primos.append(i)

for i in range(len(primos) - 1):
    p1 = primos[i]
    p2 = primos[i + 1]

    soma = p1 + p2 + 1

    if soma <= meta and eh_primo[soma]:
        atendem += 1

print('YES') if atendem >= quantidade else print('NO')
