camadasSentimentais, mensagem = int(input()), []
for camada in range(camadasSentimentais):
    if camada % 2 == 0:
        mensagem.append('I hate')
    else:
        mensagem.append('I love')
print(f'{" that ".join(mensagem[i] for i in range(len(mensagem)))} it')
