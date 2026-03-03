2486
'''Indicar se a pessoa ultrapassou o recomendado de vitamina c ou faltou'''
alimentosRicos = {
'suco de laranja' : 120,
'morango fresco' : 85,
'mamao' : 85,
'goiaba vermelha' : 70,
'manga': 56,
'laranja' : 50,
'brocolis' : 34
}
while True:
    quantidadeAlimentos, quantidadeVitaminaC = int(input()), 0
    if quantidadeAlimentos == 0:
        break
    else:
        for _ in range(quantidadeAlimentos):
            quantidade, alimento = input().split(' ', 1)
            quantidadeVitaminaC += int(quantidade) * alimentosRicos[alimento]
        print(f'{quantidadeVitaminaC} mg') if 110 <= quantidadeVitaminaC <= 130 else print(f'Mais {110 - quantidadeVitaminaC} mg') if quantidadeVitaminaC < 110 else print(f'Menos {quantidadeVitaminaC - 130} mg')
