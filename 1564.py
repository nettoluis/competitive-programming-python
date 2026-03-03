1564
while True:
    try:
        reclamacao = int(input())
        print('vai ter copa!') if reclamacao == 0 else print('vai ter duas!')
    except EOFError:
        break