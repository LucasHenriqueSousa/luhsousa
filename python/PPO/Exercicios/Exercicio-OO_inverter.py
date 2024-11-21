class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0 # <-- esse é o metodo .len()
    
    
    def empilhar(self, item):
        self.itens.append(item) # <-- esse é o metodo .append()
    
    def desempilhar_reverter(self):
        contrario = [] 
        while not self.esta_vazia():  # Enquanto a pilha não estiver vazia
            contrario.append(self.itens.pop())  # Remove do topo e coloca no contrário
        return contrario 
    # def desempilhar_reverter(self):
    #     if not self.esta_vazia():
    #         contrario = [] 
    #         for _ in range(len(self.itens)):
    #             for item in self.itens[-1]:
    #                 contrario.append(item)
    #                 self.itens.pop()
    #         return contrario 
        
        # else:
        #     return None  
        
    def topo(self):
            if not self.esta_vazia():
                return self.itens[-1]
            else:
                return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
            
minha_pilha = Pilha()

# empilhando 

minha_pilha.empilhar('N')
minha_pilha.empilhar('O')
minha_pilha.empilhar('H')
minha_pilha.empilhar('T')
minha_pilha.empilhar('Y')
minha_pilha.empilhar('P')
print('pilha após empilhamento: ', minha_pilha)
print('Tamanho da pilha: ', minha_pilha.tamanho())
print('elemento no topo da pilha: ', minha_pilha.topo())

#desempilhando
print('Desemplihando: ', minha_pilha.desempilhar_reverter())
print('Verificar status da pilha: ', minha_pilha)
print('Tamanho da pilha: ', minha_pilha.tamanho())
