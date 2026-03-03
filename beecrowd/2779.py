def main():
    total = int(input())

    compradas = []
    for _ in range(int(input())):
        compradas.append(int(input()))    

    print(total - len(set(compradas)))


main()
