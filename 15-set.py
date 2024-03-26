gameSet = {'Fifa 23', 'Red Dead 20', 'Star Wars', 'The legend of Zelda',
           'Mario Odyseey', 'Resident Evil 4'}

# - Nao possibilita recuperar valores via fatiamento ou slice

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True  e 1 sao considerados o mesmo valor
exampleSet = {'Fifa 23', True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set

gameSet.update(input('Digite seu jogo\n'))
print(gameSet)

# 4 - remover itens de outro set

gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)