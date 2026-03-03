2180
'''Coletar a quantidade de combustível que um foguete pode armazenar. Depois, somar os dez primos posteriores a essa quantidade, indicando a velocidade máxima, e depois indicar o tempo de viagem em horas e em dias daqui até Marte, sabendo que são 60 milhões de quilômetros'''
quantidadeCombustivel = int(input())
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
dezProximosPrimos, numeroVerificado = [], quantidadeCombustivel
while len(dezProximosPrimos) < 10:
    if eh_primo(numeroVerificado):
        dezProximosPrimos.append(numeroVerificado)
    numeroVerificado += 1
velocidadeMaxima = sum(dezProximosPrimos)
tempoHoras = 60000000 // velocidadeMaxima
tempoDias = tempoHoras // 24
print(f'{velocidadeMaxima} km/h\n{tempoHoras} h / {tempoDias} d')