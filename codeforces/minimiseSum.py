def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(min(2 * a[0], a[0] + a[1]))


main()
