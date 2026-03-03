x = sorted([int(xn) for xn in input().split()])

abc = max(x)
y1,y2,y3 = abc - x[0], abc - x[1], abc - x[2]

print(y1, y2, y3)
