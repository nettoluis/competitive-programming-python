quantidadeOpinioes = int(input())
opinioes = set([int(x) for x in input().split()])
print('HARD') if 1 in opinioes else print('EASY')
