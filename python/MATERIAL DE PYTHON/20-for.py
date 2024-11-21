gamesList = ['Fifa 24', 'God of war', 'Red Dead 2', 'Uncharted']
# # 1 - Interando valores de uma lista
for game in gamesList:
    print(game)

# # 2 - quando a condicao for atingida, o loop sera encerrado
for game in gamesList:
    if game == 'Red Dead 2':
        break
    print(game)
    
# 3 - Quando a condicao for atendida, o loop vai para a proxima iteracao
for game in gamesList:
    if game == 'Red Dead 2':
        continue
    print(game)
    
    
# 4 - Avaliacao do jogo
gameName = input('Digite o nome do Jogo\n')
gameRating = int(input("Digite quantas avaliacoes deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input('Digite a nota para o jogo\n')) 
    sum += note 
print(f'Media de avaliacao do jogo {gameName} e {sum/gameRating :.2f}')
    