numeroDeCasosDeTeste = int(input())
while numeroDeCasosDeTeste > 0:
    comprimentoDaString = int(input())
    frequenciasDosCaracteres = [0] * 26
    primeiroCaractere = ''
    ultimoCaractere = ''
    string = input()
    for i in range(comprimentoDaString):
        caractereAtual = string[i]
        if i == 0:
            primeiroCaractere = caractereAtual
        elif i == comprimentoDaString - 1:
            ultimoCaractere = caractereAtual
        else:
            frequenciasDosCaracteres[ord(caractereAtual) - ord('a')] += 1
        ehPossivel = False
    for i in range(26):
        if frequenciasDosCaracteres[i] >= 1 and (i == (ord(primeiroCaractere) - ord('a')) or i == (ord(ultimoCaractere) - ord('a'))):
            ehPossivel = True
            break
        if frequenciasDosCaracteres[i] >= 2:
            ehPossivel = True
            break
    if ehPossivel:
        print("Yes")
    else:
        print("No")
    numeroDeCasosDeTeste -= 1
