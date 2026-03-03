def diaPermitido(digito):
    dias = {
        (1, 2) : 'MONDAY',
        (3, 4) : 'TUESDAY',
        (5, 6) : 'WEDNESDAY',
        (7, 8) : 'THURSDAY',
        (9, 0) : 'FRIDAY',
}
    for par in dias:
        if int(digito) in par:
            return dias[par]

        
def formatoValido(placa):
    if len(placa) != 8 or ord(placa[3]) != 45:
        return False
    for i in range(3):
        if not (65 <= ord(placa[i]) <= 90):
            return False
    for i in range(4, 8):
        if not (48 <= ord(placa[i]) <= 57):
            return False

    return True


def main():
    qtd = int(input())

    for _ in range(qtd):
        placa = input()
        if not formatoValido(placa):
            print('FAILURE')
        else:
            print(diaPermitido(placa[-1]))


main()
