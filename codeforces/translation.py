berlandishWord, birlandishWord, traducao = input(), input(), True
if berlandishWord != birlandishWord[::-1]:
    traducao = False
print('YES') if traducao else print('NO')
