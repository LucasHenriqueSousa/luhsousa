fun main() {
    // Exercício 5: Média de notas
    println("Digite a primeira nota:")
    val nota1 = readLine()!!.toDouble()
    println("Digite a segunda nota:")
    val nota2 = readLine()!!.toDouble()
    val media = (nota1 + nota2) / 2
    println("A média entre $nota1 e $nota2 é igual a $media")
}

