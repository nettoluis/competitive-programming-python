primeiroBimestre, segundoBimestre, terceiroBimestre, quartoBimestre = float(input()), float(input()), float(input()), float(input())
media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre) / 4
conceito = 'A' if media >= 9.0 else 'B' if 9.0 > media >= 7.5 else 'C' if 7.5 > media >= 6.0 else 'D' if 6.0 > media >= 4.0 else 'E'
print(f'Conceito {conceito}.')
