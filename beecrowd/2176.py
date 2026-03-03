2176
'''Coletar uma mensagem binária. Posteriormente, adicionar o número 1 a ela se a quantidade de 1's for ímpar ou adicionar um 0 se a quantidade de 1's for par'''
mensagem = input()
print(f'{mensagem}0') if mensagem.count('1') % 2 == 0 else print(f'{mensagem}1')
