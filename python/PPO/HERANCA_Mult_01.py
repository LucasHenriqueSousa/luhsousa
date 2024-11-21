
class Veiculo:
    def __init__(self,nome):
        self.nome = nome

    def dirigir(self):
        print (f'{self.nome} está dirigindo.')
        
class voador:
    def __init__(self, nome):
        self.nome = nome
        
    def voar(self):
        print(f'{self.nome} está voando.')
    
class flutuante:
    def __init__(self, nome):
        self.nome = nome
        
    def flutuar(self):
        print(f'{self.nome} está flutuando.')

# sub-classe das classes principais ou 'Super classes'   
class veiculo_anfibio(Veiculo,voador,flutuante):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)
        voador.__init__(self, nome)
        flutuante.__init__(self, nome)
        
carro_anfibio = veiculo_anfibio('Criando meu Transforme')
carro_anfibio.dirigir()
carro_anfibio.flutuar()
carro_anfibio.voar()
