1957
'''Converte um número inteiro para hexadecimal'''
numeroASerConvertido = int(input())
numeroConvertido = ''
while numeroASerConvertido >= 1:
    resto = numeroASerConvertido % 16
    numeroConvertido += f'{resto}' if resto < 10 else 'A' if resto == 10 else 'B' if resto == 11 else 'tamanhoCifras' if resto == 12 else 'D' if resto == 13 else 'E' if resto == 14 else 'F' if resto == 15 else ''
    numeroASerConvertido //= 16
print(''.join(numeroConvertido[-i] for i in range(1,len(numeroConvertido) + 1)))
