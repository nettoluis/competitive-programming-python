2162
'''Coletar a quantidade de informações que serão analisadas. Posteriormente, indicar se há uma alternância constante de picos e vales'''
quantidadeInformacoes = int(input())
informacoesAlturas = list(map(int, input().split()))
if quantidadeInformacoes == 1:
    print(1)
else:
    nlogoniaSemelhanca = 1
    for i in range(quantidadeInformacoes - 1):
        if informacoesAlturas[i] == informacoesAlturas[i + 1]:
            nlogoniaSemelhanca = 0
            break
    if nlogoniaSemelhanca == 1:
        for i in range(1, quantidadeInformacoes - 1):
            alturaAnterior = informacoesAlturas[i - 1]
            alturaAtual = informacoesAlturas[i]
            alturaPosterior = informacoesAlturas[i + 1]
            if (alturaAnterior < alturaAtual and alturaAtual < alturaPosterior) or (alturaAnterior > alturaAtual and alturaAtual > alturaPosterior):
                nlogoniaSemelhanca = 0
                break
    print(nlogoniaSemelhanca)