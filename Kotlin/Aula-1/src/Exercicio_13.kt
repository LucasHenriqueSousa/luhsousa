fun main() {
    // Exercício 13: Desconto de 5%
    println("Digite o preço do produto:")
    val preco = readLine()!!.toDouble()
    val desconto = preco * 0.05
    println("O preço promocional é ${preco - desconto}")
}
