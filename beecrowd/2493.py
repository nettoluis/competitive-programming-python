def constroiDesafio(operandos, resultados):
    operando1, restante = input().split()
    operando1 = int(operando1)
    operando2, resultado = [int(x) for x in restante.split("=")]
    operandos.append(operando1)
    operandos.append(operando2)
    resultados.append(resultado)


def naoPassa(operandos, resultados, index, operacao):
    primeiro, ultimo = (2 * index) - 2, (2 * index) - 1
    match operacao:
        case "+":
            if operandos[primeiro] + operandos[ultimo] != resultados[index - 1]:
                return True
        case "*":
            if operandos[primeiro] * operandos[ultimo] != resultados[index - 1]:
                return True
        case "-":
            if operandos[primeiro] - operandos[ultimo] != resultados[index - 1]:
                return True
        case "I":
            if (
                operandos[primeiro] - operandos[ultimo] == resultados[index - 1]
                or operandos[primeiro] * operandos[ultimo] == resultados[index - 1]
                or operandos[primeiro] + operandos[ultimo] == resultados[index - 1]
            ):
                return True

    return False


def main():
    while True:
        try:
            qtd = int(input())

            operandos, resultados = [], []
            for _ in range(qtd):
                constroiDesafio(operandos, resultados)

            naoPassaram = []
            for _ in range(qtd):
                nome, index, operacao = [x for x in input().split()]
                index = int(index)
                if naoPassa(operandos, resultados, index, operacao):
                    naoPassaram.append(nome)

            if not naoPassaram:
                print("You Shall All Pass!")
            elif len(naoPassaram) == qtd:
                print("None Shall Pass!")
            else:
                print(f'{" ".join(sorted(naoPassaram))}')
        except EOFError:
            break


main()
