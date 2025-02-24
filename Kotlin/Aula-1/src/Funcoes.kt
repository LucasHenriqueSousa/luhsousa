
fun main() {
    val carro = Carro()
    carro.cor = "Azul"
    carro.altura = 1.65
    carro.largura = 2.56
    println("${carro.cor}\n${carro.altura}\n${carro.largura}\n")
    println("${carro.primeiraMarcha()}\n")

    fun parOuImpar(a: Int): String {
        return if (a % 2 == 0) "par" else ("impar")
    }
    println("${parOuImpar(2)}\n${parOuImpar(5)}")

    fun printMessage(message: String, newline: Boolean = true) {
        if (newline) {
            println(message)
        } else {
            print(message)
        }
    }
    printMessage("Hello, world!") // imprime "Hello, world!" seguido de uma nova linha
    printMessage("Hello, world!", newline = false) // imprime "Hello, world!" sem uma nova linha
}
