def wellcome():
    print('Hello World')
    
wellcome()

# 2 - Funcao para dois numeros 

def sum():
    # print(5 + 4)
    return 5 + 4
print(sum())

# 3 - Funcao para cadastrar um jogo

def creater_game():
    name = input("Digite o nome do jogo\n")
    yaerLaunch = int(input("digite o ano de lancamento do jogo\n"))
    gamePrice = float(input("DIGITE O valor do jogo\n"))
    noteRating = float(input("Digite a nota de avaliacao\n"))
    
    print(f'{name} - R$ {gamePrice}')
    
creater_game()
creater_game()