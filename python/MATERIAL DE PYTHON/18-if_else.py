name = input('digite o nome do jogo\n')
yearLaunch = int(input('digite o ano de lancamento do jogo\n'))
classification = float(input('digite a nota de classificacao do jogo\n'))

if classification > 8.0 and yearLaunch > 2015:
    print(f"Ojogo {name} e bom. recomendo o jogo-lo")
else: 
    print(f"O jogo {name} ainda nao atingiu uma boa nota. por isso nao recomendo") 
