/*              Exercícios de Algoritmos e lógica de programação.



3 Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma
mensagem.
Ex:
Nome do Funcionário: Maria do Carmo Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em junho. */

//Resposta

fun main(){
    println("Digite seu nome")
    val name:String = readln()
    println("Digite seu Salário")
    var money = readln().toDouble()
    var SalFormat = String.format("%.2f", money).toString()

    println("Nome do Funcionário: $name Salário: $SalFormat\n" +
            "O funcionário $name tem um salário de $SalFormat, em junho.")

}