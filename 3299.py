3299
'''Coletar um número e dizer se é de má sorte ou não. Sabendo que pra ser de má sorte tem que ter um 1 seguido de um 3.'''
numeroAnalisado = input()
print(f'{numeroAnalisado} es de Mala Suerte') if '13' in numeroAnalisado else print(f'{numeroAnalisado} NO es de Mala Suerte')