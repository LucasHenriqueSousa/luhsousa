fun main() {
    // Exercício 11: Área da parede e tinta necessária
    println("Digite a largura da parede:")
    val largura = readLine()!!.toDouble()
    println("Digite a altura da parede:")
    val altura = readLine()!!.toDouble()
    val area = largura * altura
    println("Área total: $area metros quadrados")
    println("Quantidade de tinta necessária: ${area / 2} litros")
}
