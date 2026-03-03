lado, comprimento, ladoPiso = [int(dado) for dado in input().split()]
quantidadeHorizontal, quantidadeVertical = lado // ladoPiso, comprimento // ladoPiso
quantidadeHorizontal += 1 if lado % ladoPiso != 0 else 0
quantidadeVertical += 1 if comprimento % ladoPiso != 0 else 0
print(f'{quantidadeHorizontal * quantidadeVertical}')
