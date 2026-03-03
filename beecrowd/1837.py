1837
'''Coletar dois números inteiros e imprimir o quociente da divisão entre eles e o resto'''
dividendo, divisor = map(int, input().split())
for resto in range(abs(divisor)):
    if ((dividendo - resto) % divisor) == 0:
        quociente = (dividendo - resto) // divisor
        break
print(f'{quociente} {resto}')
