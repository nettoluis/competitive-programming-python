2203
'''Coletar as coordenadas do atacante, do alvo, a velocidade do alvo, o raio de conjuracao e de ataque dos corvos'''
while True:
    try:
        xAtacante, yAtacante, xAlvo, yAlvo, velocidadeAlvo, raioConjuracao, raioCorvos = map(int,input().split())
        distanciaAtacanteAlvo = ((((xAtacante - xAlvo) ** 2) + ((yAtacante - yAlvo) ** 2)) ** 0.5)
        distanciaAtacanteAlvo += velocidadeAlvo * 1.5
        print('Y') if distanciaAtacanteAlvo <= (raioConjuracao + raioCorvos) else print('N')
    except EOFError:
        break