2165
'''Coletar um texto e informar se pode ser um tweet ou não'''
texto = input()
print('TWEET') if len(texto) <= 140 else print('MUTE')