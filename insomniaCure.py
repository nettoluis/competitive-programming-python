divisores, abatidos = [], 0
for divisor in range(4):
    divisor = int(input())
    divisores.append(divisor)
dragoes = int(input())
for dragao in range(1,dragoes + 1):
    for divisor in divisores:
        if dragao % divisor == 0:
            abatidos += 1
            break
        else:
            continue
print(abatidos)
