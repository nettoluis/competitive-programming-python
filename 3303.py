3303
'''Coletar uma palavra e retornar se ela é um palavrão -- se possível dez ou mais caracteres--, ou palavrinha.'''
palavraAnalisada = input()
print('palavrao') if len(palavraAnalisada) >= 10 else print('palavrinha')