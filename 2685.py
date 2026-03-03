def determinaPeriodo(a):
    if 90 > a % 360 >= 0:
        return 'Bom Dia!!'
    elif 180 > a % 360 >= 90:
        return 'Boa Tarde!!'
    elif 270 > a % 360 >= 180:
        return 'Boa Noite!!'
    else:
        return 'De Madrugada!!'
    

def main():
    while True:
        try:
            angulacao = int(input())
            
            saudacao = determinaPeriodo(angulacao)

            print(saudacao)
        except EOFError:
            break


main()
