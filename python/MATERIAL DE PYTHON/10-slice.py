gameName = "FIfa 24"
gameDescription = """
            Fifa 23 é um jogo de futebol
            desenvolvido pela EA Sports
            e que possibilita Jogar 
            Localmente ou online.
"""


# strings[Inicio:fim] - indice comeca na posicao 0 | indice -1

# 1- Busque toda string a partir da primeira posicao.

print(gameName[0:]) 

# 2 - Busque toda string ate a ultima posicao

print(gameName[:7])

#Busque toda string da terceira ate a ultima posicao

print(gameName[2:])
"""
strings[Inicio:fim:passo] - indice comeca na posicao 0 | indice -1
passo - determina o incremento. Por padrao esse numero e o 1.
"""

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - busque toda string nos indices impares 
print(gameName[1::2])

# 6 - inverter uma string de frente para tras.

print(gameName[::-1])