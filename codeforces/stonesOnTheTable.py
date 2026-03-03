quantidadePedras: int = int(input())
sequenciaPedras: str = input()
contador = 0
for i in range(quantidadePedras - 1):
    if sequenciaPedras[i] == sequenciaPedras[i + 1]:
        contador += 1
print(contador)
