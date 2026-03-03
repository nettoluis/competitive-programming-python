quantidadeTestes = int(input())

for _ in range(quantidadeTestes):
    inteiro = int(input())
    if not inteiro % 3:
        print('Second')
    else:
        print('First')
