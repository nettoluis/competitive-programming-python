3342
'''Coletar a ordem de um tabuleiro de xadrez e indicar a quantidade de casas brancas e casas pretas'''
ordemTabuleiro = int(input())
print(f'{1 + (ordemTabuleiro**2//2)} casas brancas e {(ordemTabuleiro**2//2)} casas pretas') if ordemTabuleiro % 2 != 0 else print(f'{(ordemTabuleiro**2//2)} casas brancas e {(ordemTabuleiro**2//2)} casas pretas')