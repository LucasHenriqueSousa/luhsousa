fun main() {
    // Exercício 16: Cálculo de salário por dias trabalhados
    println("Digite o número de dias trabalhados:")
    val diasTrabalhados = readLine()!!.toInt()
    val salarioTotal = diasTrabalhados * 8 * 25
    println("O salário do funcionário é R$ $salarioTotal")
}