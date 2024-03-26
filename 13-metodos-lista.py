gamesList = ['Resident Evil 4','Star Wars Jedi Survivor',
             'The Legend of Zelda', 'Red Dead 2', 'Mario Odyssey',
             'LuigisMension 3']

#1 - Tamanho da lista
print(len(gamesList))

#2 - Recuperar um item da lista pelo indice.
print(gamesList.index('Mario Odyssey'))

#3 - Adicionar item ao final da lista
gamesList.append('Gta v')

print(gamesList)

#4 - Ordenar a lista
gamesList.sort()
print(gamesList)

#5- Copiar os itens de uma lista para outra

gameReset = gamesList.copy()
gameReset.remove('Star Wars Jedi Survivor')
print(gameReset)

#6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)