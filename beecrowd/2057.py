2057
'''Coletar o horário de saída, duração da viagem e fuso horário e indicar o horário de chegada'''
horarioSaida, tempoViagem, fusoHorario = map(int,input().split())
soma = horarioSaida + tempoViagem + fusoHorario
print(f'{soma}') if (0 <= soma and soma < 24) else print(f'{soma - 24}') if (soma >= 24) else print(f'{soma + 24}')
