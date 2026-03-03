2152
'''Coletar a quantidade de casos teste. Posteriormente, imprimir a hora formatada e indicar se a porta foi aberta ou fechada'''
quantidadeCasos = int(input())
for _ in range(quantidadeCasos):
    hora,minuto,ocorrencia = map(int,input().split())
    minuto,hora = f'0{minuto}' if len(str(minuto)) == 1 else minuto, f'0{hora}' if len(str(hora)) == 1 else hora
    print(f'{hora}:{minuto} - A porta abriu!') if ocorrencia == 1 else print(f'{hora}:{minuto} - A porta fechou!')