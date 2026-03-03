def main():
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    
    print(f'A = {a:.6f}, B = {b:.6f}\nC = {c:.6f}, D = {d:.6f}')
    print(f'A = {a:.1f}, B = {b:.1f}\nC = {c:.1f}, D = {d:.1f}')
    print(f'A = {a:.2f}, B = {b:.2f}\nC = {c:.2f}, D = {d:.2f}')
    print(f'A = {a:.3f}, B = {b:.3f}\nC = {c:.3f}, D = {d:.3f}')
    print(f'A = {a:.3E}, B = {b:.3E}\nC = {c:.3E}, D = {d:.3E}')
    print(f'A = {a:.0f}, B = {b:.0f}\nC = {c:.0f}, D = {d:.0f}')


main()
