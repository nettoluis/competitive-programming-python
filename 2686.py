def calculaTempo(a):
    segundosTotais = a * 240
    horas = (6 + (segundosTotais // 3600)) % 24 
    segundosTotais -= (segundosTotais // 3600) * 3600

    minutos = segundosTotais // 60
    segundosTotais -= (segundosTotais // 60) * 60

    segundos = segundosTotais

    return int(horas), int(minutos), int(segundos)


def determinaPeriodo(a):
    horas, minutos, segundos = calculaTempo(a)
    if 90 > a % 360 >= 0:
        return 'Bom Dia!!', horas, minutos, segundos
    elif 180 > a % 360 >= 90:
        return 'Boa Tarde!!', horas, minutos, segundos
    elif 270 > a % 360 >= 180:
        return 'Boa Noite!!', horas, minutos, segundos
    else:
        return 'De Madrugada!!', horas, minutos, segundos

    

def main():
    while True:
        try:
            angulacao = float(input())
            
            saudacao, horas, minutos, segundos = determinaPeriodo(angulacao)

            print(saudacao)
            print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')
        except EOFError:
            break


main()
