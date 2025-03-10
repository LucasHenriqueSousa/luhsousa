fun main() {
    // Exercício 10: Conversão de moeda
    println("Digite quanto dinheiro você tem na carteira (em R$):")
    val dinheiro = readLine()!!.toDouble()
    val cotacaoDolar = 3.45
    println("Você pode comprar ${dinheiro / cotacaoDolar} dólares")
}
