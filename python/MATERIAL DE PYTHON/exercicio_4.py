# distance = float(input('Digite a distancia a percorrer\n'))
# if distance  <= 200:
#     ticket = 0.5 * distance
# else:
#     ticket = 0.35 * distance
# print(f'Preco da passagem e: {ticket:.2f}')



# Aumento de salario do funcionario
salary = float(input('Digite o seu salario \n'))
perc_increase = 0.15

if salary > 1250:
    perc_increase = 0.10
increase = salary * perc_increase
print(f'Seu aumento e {increase:.2f}')
print(f'Passara a receber:', (increase + salary))

