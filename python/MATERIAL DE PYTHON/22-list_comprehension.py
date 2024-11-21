# for i in range(10):
#     if i < 4:
#         print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Mario odyssey", "Dk Country",
            'Luigis Mansion', 'Kirby']

# 2 - Jogos que pussuem letra a 

newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que zerei 

gamesFinished = [x for x in gamesList if x != 'Kirby']
print(gamesFinished)
