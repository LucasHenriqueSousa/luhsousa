#%%
gameFifa = ["Fifa 23", 2022, 90.50, True]
print(gameFifa)

gamesList = ['Resident Evil 4','Star Wars Jedi Survivor',
             'The Legend of Zelda', 'Red Dead 2', 'Mario Odyssey']
print(gamesList)

#1 - Buscar os dois primeiros itens da lista
print(gamesList[:2])

#2 - Buscar o ultimo item da lista
print(gamesList[-1])

#3 - buscar jogos ate uma determinada posicao
print(gamesList[:3])

#4 - Buscar jogos de posicao em diante
print(gamesList[1:4])

# %%
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':2, 'two':1}:
    print(key)
for char in "123":
    print(char)
# for line in open("myfile.txt"):
    # print(line, end='')
# %%