def main():
   lista = [] 
   for i in range(10):
       nome = input()
       if i in [2, 6, 8]:
           lista.append(nome)

   for elemento in lista:
       print(elemento)


main()
