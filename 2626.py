def verificaBatalhaIndividual(ganhaJokenpo, p1, p2):
    if p2 in ganhaJokenpo[p1]:
        return 1
    
    return 0

def quemGanha(p1, p2, p3):
    ganhaJokenpo = {
        'pedra' : 'tesoura',
        'tesoura' : 'papel',
        'papel' : 'pedra', 
    }
    vitoriasP1, vitoriasP2, vitoriasP3 = 0, 0, 0

    vitoriasP1 += verificaBatalhaIndividual(ganhaJokenpo, p1, p2) + verificaBatalhaIndividual(ganhaJokenpo, p1, p3)
    vitoriasP2 += verificaBatalhaIndividual(ganhaJokenpo, p2, p1) + verificaBatalhaIndividual(ganhaJokenpo, p2, p3)
    vitoriasP3 += verificaBatalhaIndividual(ganhaJokenpo, p3, p2) + verificaBatalhaIndividual(ganhaJokenpo, p3, p1)

    if vitoriasP1 > vitoriasP2 and vitoriasP1 > vitoriasP3:
        return "Os atributos dos monstros vao ser inteligencia, sabedoria..."
    if vitoriasP2 > vitoriasP1 and vitoriasP2 > vitoriasP3:
        return "Iron Maiden's gonna get you, no matter how far!" 
    if vitoriasP3 > vitoriasP1 and vitoriasP3 > vitoriasP2:
        return "Urano perdeu algo muito precioso..."
    else:
        return "Putz vei, o Leo ta demorando muito pra jogar..."

def main():
    while True:
        try:
            dodo, leo, pepper = input().split()

            mensagemVitoria = quemGanha(dodo, leo, pepper)

            print(mensagemVitoria)
        except EOFError:
            break

main()
