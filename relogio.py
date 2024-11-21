#%%
from time import sleep

def relogio(h, m, s):
    while True:
        h = 0
        while h < 24: 
            m = 0              
            while m < 60:
                s = 0
                while s < 60:
                    print(f'{h:02}:{m:02}:{s:02}')
                            # sleep(1)
                    s+=1
                m+=1        
            h+=1 
h = int(input('insira a hora que deseja\n'))
m = int(input('insira a minuto que deseja\n'))
s = int(input('insira a segundos que deseja\n'))
relogio(h, m, s)
# %%
from time import sleep

def relogio(h, m, s):
    while True:
        if h <= 24:
            while h < 24:
                if m <= 60:
                    while m < 60:
                        if s <= 60:
                            while s < 60:
                                print(f'{h:02}:{m:02}:{s:02}')
                                sleep(00)
                                s += 1
                            m += 1
                        else:
                            s = 0
                            m += 1
                    h += 1
                    m = 0
                else:
                    m = 0
                    h += 1
        else:
            h = 0

h = int(input('Insira a hora que deseja: '))
m = int(input('Insira o minuto que deseja: '))
s = int(input('Insira o segundo que deseja: '))
relogio(h, m, s)  # Chame a função com os valores corretos


# %%
