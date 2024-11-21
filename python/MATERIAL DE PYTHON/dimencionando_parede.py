def calcular_area_parede(altura, largura):
    # Calcula a área da parede
    area = altura * largura * 2  # Multiplica por 2 para considerar ambos os lados da parede
    # Retorna a área da parede
    return area

def calcular_materiais(area, area_placa, parafusos_por_m2, comprimento_perfil):
    # Calcula a quantidade de materiais necessários
    placas = area / area_placa
    parafusos = area * parafusos_por_m2
    perfis = area / comprimento_perfil
    # Retorna a quantidade de materiais
    return placas, parafusos, perfis

# Exemplo de uso das funções
altura1 = float(input("Digite a altura da primeira parede em metros: "))
largura1 = float(input("Digite a largura da primeira parede em metros: "))
altura2 = float(input("Digite a altura da segunda parede em metros: "))
largura2 = float(input("Digite a largura da segunda parede em metros: "))

area1 = calcular_area_parede(altura1, largura1)
area2 = calcular_area_parede(altura2, largura2)
area_total = area1 + area2

area_placa = float(input("Digite a área que uma placa de drywall cobre em metros quadrados: "))
parafusos_por_m2 = float(input("Digite a quantidade de parafusos necessários por metro quadrado: "))
comprimento_perfil = float(input("Digite o comprimento do perfil F530 em metros: "))

placas, parafusos, perfis = calcular_materiais(area_total, area_placa, parafusos_por_m2, comprimento_perfil)

print(f"A área total das paredes de drywall é {area_total} metros quadrados.")
print(f"Você precisará de {placas} placas de drywall, {parafusos} parafusos e {perfis} perfis F530.")
