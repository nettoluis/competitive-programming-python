def main():
    x, y = 234.345, 45.698

    print(f'{x:.6f} - {y:.6f}')
    print(f'{x:.0f} - {y:.0f}')
    print(f'{x:.1f} - {y:.1f}')
    print(f'{x:.2f} - {y:.2f}')
    print(f'{x:.3f} - {y:.3f}')
    print(f'{x / 100:.6f}e+02 - {y / 10:.6f}e+01')
    print(f'{x / 100:.6f}E+02 - {y / 10:.6f}E+01')
    print(f'{x:.3f} - {y:.3f}')
    print(f'{x:.3f} - {y:.3f}')

main()
