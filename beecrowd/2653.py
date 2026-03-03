def main():
    joias = []
    while True:
        try:
            joia = input()
            joias.append(joia)
        except EOFError:
            break
    print(len(set(joias)))

main()
