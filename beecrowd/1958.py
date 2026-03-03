1958
#
# numeroDecimal, numeroEmNotacao, expoente = float(input()), [], 0
# numeroEmNotacao.append('+') if numeroDecimal > 0 else ('-')
# numeroDecimal = abs(numeroDecimal)
# if numeroDecimal >= 10:
#     while numeroDecimal >= 10:
#         numeroDecimal /= 10
#         expoente += 1
# elif numeroDecimal < 1:
#     while numeroDecimal < 1:
#         numeroDecimal *= 10
#         expoente -= 1
# numeroEmNotacao.append(f'{numeroDecimal:.4f}')
# numeroEmNotacao.append('E')
# numeroEmNotacao.append('+') if expoente >= 0 else numeroEmNotacao.append('-')
# numeroEmNotacao.append(abs(expoente)) if abs(expoente) >= 10 else numeroEmNotacao.append('0' + str(abs(expoente)))
# print(f'{"".join(str(numeroEmNotacao[i]) for i in range(len(numeroEmNotacao)))}')
1958
'''Coletar um número decimal e imprimir ele em formato de notação científica'''
numeroDecimal = float(input())
numeroEmNotacao = "{:+.4E}".format(numeroDecimal) if numeroDecimal >= 0 else "{:-.4E}".format(numeroDecimal)
print(numeroEmNotacao)