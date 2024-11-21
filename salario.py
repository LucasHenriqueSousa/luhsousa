#%%
salarios = [0,0,0]
soma = 0
i = 0
while i < 3:
    
    salarios[i] = float(input('Salario: R$ '))
    soma += salarios[i]
    i += 1
media = soma/3
print(f'Media R${media:.2f}')        
i = 0    
while i < 3:
    if salarios[i] < media:
        print(f'Abaixo da Media: R${salarios[i]:.2f}')
    i += 1    

    
# %%
