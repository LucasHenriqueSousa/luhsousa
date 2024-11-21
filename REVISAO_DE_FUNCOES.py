# REVISAO DE FUNCAO
def cumprimentar(nome):
    print(f'Ola, {nome}!!')

def futebol(time):
    print(f'{time} NAO tem mundial')

cumprimentar("Lucas Henrique")
futebol('PALMEIRAS')

#%%
def somar_numeros(a,b):
    return a+b
def subtrair_numeros(a,b):
    return a-b
def dividir_numeros(a,b):
    return a/b
def mult_numeros(a,b):
    return a*b


resultado_sub = subtrair_numeros(2,5)
resultado_soma = somar_numeros(5,10)

print(f'a subtracao e {resultado_sub}')
print(f'A soma e {resultado_soma}')

# %%
def calcular_area(base,altura):
    return (base*altura)/2

print(f'Area 1 =', calcular_area(10,3))

area_tri = calcular_area(5,4)

print(f'area 2 = {area_tri}')
# %%
#ASSUNTO NOVO COM FUNCOES

def somar_num(*args):
    total = 0 
    for num in args:
        total += num
    return total
print(F'soma com 2 argumentos: {somar_num(1,3)}')
print(F'soma com 4 argumentos: {somar_num(1,3,5,8)}')
print(F'soma com 10 argumentos: {somar_num(1,3,4,5,5,5,5,5,5,5)}')




# %%
