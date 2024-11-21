''' QUEUE (FILA) TIPO DE ESTRUTURA DE DADOS.   -> CONCEITO <- FIFO (FIRST IN FIRST OUT) '''

# CARACTERISTICAS DA ESTRUTURA DE DADOS. 

# -> ENQUEUE -> METODO DE ADICIONA NO FINAL DA FILA. 
# -> DEQUEUE ->  METODO DE RETIRA O PRIMEIRO DA FILA. 


class Fila:
    def __init__(self):
        self.itens = []
        
    def esta_vazia(self):
        return len(self.itens) == 0 # <-- esse é o metodo len()
    
    def enfileirar(self, item):
        self.itens.append(item) # <-- esse é o metodo append()
        
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0) # <-- esse é o metodo de pop(0) retirando o primeiro indice da lista
        
    def frente(self):
        if not self.esta_vazia():
            return self.itens[0]
        else:
            return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
    
minha_fila = Fila()

# enfileirando

minha_fila.enfileirar('P')
minha_fila.enfileirar('Y')
minha_fila.enfileirar('T')
minha_fila.enfileirar('H')
minha_fila.enfileirar('O')
minha_fila.enfileirar('N')
print('fila após enfileirar: ', minha_fila, '\n') 

print('elemento na frente da fila: ', minha_fila.frente(), '\n')

#desenfileirando

print('Desenfileirando: ', minha_fila.desenfileirar(), '\n')
print('Verificar status da Fila: ', minha_fila, '\n')
print('Desenfileirando: ', minha_fila.desenfileirar(), '\n')
print('Verificar status da fila: ', minha_fila, '\n')
print('Tamanho da fila: ', minha_fila.tamanho())