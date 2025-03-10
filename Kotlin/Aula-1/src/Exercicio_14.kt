fun main() {
    // Exercício 14: Aumento de salário
    println("Digite o salário do funcionário:")
    val salario = readLine()!!.toDouble()
    val aumento = salario * 0.15
    println("O novo salário é ${salario + aumento}")
}
