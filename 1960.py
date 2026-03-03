1960
'''Transformar um número de páginas em indoarábico em algarismos romanos'''
numero, transcricaoRomana, traducao = int(input()), {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'tamanhoCifras',400:'CD',500:'D',900:'CM',1000:'M'}, ''
numerosIndoarabicos, simbolosRomanos = list(transcricaoRomana), list(transcricaoRomana.values())
for i in range(12,-1,-1):
    if numero > 0:
        while numero >= numerosIndoarabicos[i]:
            numero -= numerosIndoarabicos[i]
            traducao += simbolosRomanos[i][:]
print(traducao)
