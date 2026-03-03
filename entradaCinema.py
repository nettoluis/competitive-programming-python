anoAtual, anoNascimento = int(input('Ano atual?')), int(input('Ano de nascimento?'))
idade = anoAtual - anoNascimento
if 14 <= idade < 16:
    acompanhado = input('Com os pais?')
    if acompanhado == 's':
        acompanhado = True
    else:
        acompanhado = False
print(f'Idade calculada: {idade} anos')
if idade >= 16 or (14 <= idade < 16 and acompanhado):
    print('Entrada permitida')
elif 14 <= idade < 16 and not acompanhado:
    print('Entrada proibida para menores de 16 anos sem os pais')
else:
    print('Entrada proibida para menores de 14 anos')

    
