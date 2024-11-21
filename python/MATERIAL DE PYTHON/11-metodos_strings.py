gameName = "Fifa 24"
gameDescription = """
            Fifa 23 é um jogo de futebol,
            desenvolvido, pela EA Sports,
            e que possibilita, Jogar 
            Localmente ou online.
"""

print(gameName.upper()) # Retornar string em maiusculo
print(gameName.lower()) # Retornar string em minusculo
print(gameName.capitalize()) # apenas a primeira letra em maiusculo
print(gameName.title()) #  apenas a primeira letra em maiusculo
print(gameName.center(11, '-')) # Retorna a string centralizada com caracteres de preenchimento
print(gameName.find("i")) # retorna a posicao de um determinado caractere.
print(gameDescription.count("a")) # conta a qauntidade do mesmo caractere na string
print(gameDescription.replace("Fifa","Pes")) # Altera um elemento por outro
print(gameDescription.split(','))