qtd = int(input())

for _ in range(qtd):
    rating = int(input())
    division = 1 if rating >= 1900 else 2 if rating >= 1600 else 3 if rating >= 1400 else 4
    print(f'Division {division}')
