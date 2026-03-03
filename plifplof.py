#Solução utilizando funções
fatorUm, fatorDois, fatorTres = int(input()), int(input()), int(input())
def divisivel3(a = fatorUm, b = fatorDois, c = fatorTres):
    return (a + b + c) % 3 == 0:
def divisivel5(a = fatorUm, b = fatorDois, c = fatorTres):
    return (a + b + c) % 5 == 0:
print('plifplof') if divisivel3() and divisivel5() else print('plif') if divisivel3() else print('plof') if divisivel5() else print('')
#Solução mais simples
a, b, c = int(input()), int(input()), int(input())
soma, mensagem = a + b + c, ''
mensagem += 'plifplof' if (soma % 3 == 0) and (soma % 5 == 0) else 'plif' if soma % 3 == 0 else 'plof' if soma % 5 == 0 else 'Não é divisível nem por 3 nem por 5'
print(mensagem)
