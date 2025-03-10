fun main() {
    // Exercício 15: Aluguel de carro
    println("Digite a quantidade de Km percorridos:")
    val km = readLine()!!.toDouble()
    println("Digite a quantidade de dias de aluguel:")
    val dias = readLine()!!.toInt()
    val precoTotal = (dias * 90) + (km * 0.20)
    println("O total a pagar é R$ $precoTotal")
}
