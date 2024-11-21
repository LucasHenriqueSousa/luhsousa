# %%
def casa_branca():
    print(2 * ' ', end='')

def casa_preta():
    print(2 * chr(9608), end='')

def criar_tabuleiro(n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            if (i + j) % 2 == 0:
                casa_branca()
            else:
                casa_preta()
            j += 1
        print()  
        i += 1

n = int(input('Insira o tamanho do tabuleiro'))
criar_tabuleiro(n)
