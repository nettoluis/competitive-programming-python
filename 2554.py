2554
'''Coletar a quantidade de amigos e de datas possíveis. Posteriormente, indicar em qual dia é possível todos os amigos se reunirem'''
while True:
    try:
        quantidadeAmigos, quantidadeDatas = [int(x) for x in input().split()]
        ocorrencia = 0
        for data in range(quantidadeDatas):
            dataAnalisada, presencaAmigos = [x for x in input().split(' ', 1)]
            if '0' not in presencaAmigos and ocorrencia == 0:
                dataPossivel = dataAnalisada
                ocorrencia += 1
        print(dataPossivel) if ocorrencia == 1 else print('Pizza antes de FdI')
    except EOFError:
        break
