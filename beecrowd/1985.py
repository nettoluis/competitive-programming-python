1985
'''Coletar a quantidade de casos testes. Posteriormente, calcular a conta de uma lanchonete'''
qtdItems, contaAPagar = int(input()), 0
for _ in range(qtdItems):
    lanche, quantidade = map(float,input().split())
    contaAPagar += (lanche - 999.50) * quantidade
print(f'{contaAPagar:.2f}')
