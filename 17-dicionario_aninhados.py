import pprint
gamesDict = {
    "resident evil 4":{
        "yearLaunch": 2024,
        "classification": 9.8,
        "genre": ["acao", "aventura"]
    },
    "mario odyssey": {
        "yaerLaunch": 2017,
        "Classification": 10,
        "genre": ["aventura", "3D"]
    },
    "Donkey Kong country": {
        "yearLaunch": 1995,
        "Classification": 9.5,
        "genre": ["Aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - buscar informacao dentro deum dicionario aninhado

print(gamesDict["mario odyssey"]["genre"])

# 2 - Adiconar um novo item 
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dionario
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)