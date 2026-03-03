#solução sem list comprehension
palavra, maiusculas, minusculas = input(), [], []
for letra in palavra:
    if letra.isupper():
        maiusculas.append(letra)
    else:
        minusculas.append(letra)
print(palavra.upper()) if len(maiusculas) > len(minusculas) else print(palavra.lower())
#solução com list comprehension
palavra = input()
maiusculas, minusculas = [letra for letra in palavra if letra.isupper()], [letra for letra in palavra if letra.islower()]
print(palavra.upper()) if len(maiusculas) > len(minusculas) else print(palavra.lower())
