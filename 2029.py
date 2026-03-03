2029
'''Coletar o volume de mel produzido e o diâmetro da base de um cilindro e informar a área da base do cilindro e a altura'''
while True:
    try:
        volumeProduzido, diametroBase = float(input()), float(input())
        areaBase = (((diametroBase/ 2) ** 2) * 3.14)
        print(f'ALTURA = {volumeProduzido/areaBase:.2f}\nAREA = {areaBase:.2f}')
    except EOFError:
        break