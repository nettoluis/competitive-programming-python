2006
chaTipo, quantidadeAcertos = int(input()), 0
chasEscolhidos = list(map(int,input().split()))
for i in range(5):
    quantidadeAcertos += 1 if chasEscolhidos[i] == chaTipo else 0
print(f'{quantidadeAcertos}')