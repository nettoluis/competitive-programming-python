codigo = input()

mensagem = ''
i = 0
while i < len(codigo):
    if codigo[i] == '.':
        mensagem += '0'
        i += 1
    elif codigo[i] == '-':
        if codigo[i + 1] == '.':
            mensagem += '1'
        else:
            mensagem += '2'
        i += 2

print(mensagem)
