def encontraPontosMaisProximos(cx, x0, largura, cy, y0, altura):
    if cx < x0:
        menorX = x0
    elif cx > x0 + largura:
        menorX = x0 + largura
    elif x0 <= cx <= x0 + largura:
        menorX = cx

    if cy < y0:
        menorY = y0
    elif cy > y0 + altura:
        menorY = y0 + altura
    elif y0 <= cy <= y0 + altura:
        menorY = cy

    return menorX, menorY


def distancia(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def verificaColisao(largura, altura, x0, y0, magia, nivel, cx, cy):
    raios = {
        "fire": [20, 30, 50],
        "water": [10, 25, 40],
        "earth": [25, 55, 70],
        "air": [18, 38, 60],
    }
    raio = raios[magia][nivel - 1]
    menorX, menorY = encontraPontosMaisProximos(cx, x0, largura, cy, y0, altura)

    return distancia(menorX, menorY, cx, cy) <= raio


def calculaDano(magia):
    danos = {
        "fire": 200,
        "water": 300,
        "earth": 400,
        "air": 100,
    }

    return danos[magia]


def main():
    qtd = int(input())

    for _ in range(qtd):
        dano = 0
        larguraR, alturaR, x0, y0 = [int(x) for x in input().split()]
        magia, nivel, cx, cy = [int(x) if x.isnumeric() else x for x in input().split()]
        bateu = verificaColisao(larguraR, alturaR, x0, y0, magia, nivel, cx, cy)
        if bateu:
            dano = calculaDano(magia)

        print(dano)


main()
