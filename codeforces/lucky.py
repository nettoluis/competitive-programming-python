quantidadeTickets = int(input())

for _ in range(quantidadeTickets):
    ticket = input()
    primeiraMetade = ticket[0:3]
    segundaMetade = ticket[3:]
    primeiraSoma = 0
    segundaSoma = 0
    for i in range(3):
        primeiraSoma += int(primeiraMetade[i])
        segundaSoma += int(segundaMetade[i])
    print('YES') if primeiraSoma == segundaSoma else print('NO')
        
