# # 1 - Contagem regressiva
# import winsound
# x = 10 
# while x >= 0:
#     print(x)
#     x -= 1
# winsound.Beep(2500, 500)

# Tabuada de um numero 
# number = int(input(' tabuada de: \n'))
# begin = int(input('De: \n'))
# end = int(input('Ate: \n'))

# x = begin

# while x <= end:
#     print(f'Tabuada de {number} x {x} = {number * x}')
#     x = x + 1

# 3 - Abrindo o navegador em uma pagina. 
import webbrowser

def abrir_google():
    webbrowser.open('http://www.youtube.com')

entrada = input("Digite um ponto para abrir o Google: ")

if entrada == '.':
    abrir_google()
else:
    print("Você não digitou um ponto.")
