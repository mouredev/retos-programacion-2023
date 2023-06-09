fun main() {

    /*
    * Reto #9 27/02/2023
    *
    * Crea 3 funciones, cada una encargada de detectar si una cadena de
    * texto es un heterograma, un isograma o un pangrama.
    * - Debes buscar la definición de cada uno de estos términos.
    *
    */

    print("Introce la palabra a analizar:")
    val texto = readLine()!!

    val analizador = Analizador(texto)
    if (analizador.isHeterograma()) println("Es heterograma") else println("NO es heterograma")
    if (analizador.isIsograma()) println("Es isograma") else println("NO es isograma")
    if (analizador.isPangrama()) println("Es pangrama") else println("NO es pangrama")

    println( analizador.showOcurrencias())

}

class Analizador(var texto : String){

    private var alfabeto = mutableListOf<Char>()
    private val ocurrencias = mutableListOf<Pair<Char, Int>>()

    private var isHeterograma = false
    private var isIsograma = false
    private var isPangrama = false

    init {
        // Creo un array con el alfabeto
        ('a' ..  'z').forEach{
            alfabeto.add(it)
        }
        alfabeto.add('ñ')


        // Preparo el array el que va a guardar las coincidencias
        var indice: Int?
        var valor: Int
        this.texto.lowercase().forEach { letra ->

            if (letra in alfabeto){
                indice = null
                valor = 0

                ocurrencias.forEachIndexed { index, pair ->

                    if (pair.first == letra) {
                        indice = index
                        valor = pair.second
                    }

                }
                if (indice == null){
                    ocurrencias.add(Pair(letra, 1))
                } else {
                    ocurrencias[indice!!]=Pair(letra, valor+1)
                }
            }

        }

        // Ahora compruebo cada uno de los posibles casos
        isHeterograma = analizeIsHeterograma()
        isIsograma = analizeIsIsograma()
        isPangrama = analizeisPangrama()
    }



    fun analizeIsHeterograma():Boolean{
        // Es una palabra o frase que no contiene ninguna letra repetida.
        var isHeterograma = true
        this.ocurrencias.forEach{
            if (it.second > 1){
                isHeterograma = false
            }
        }
        return isHeterograma
    }
    fun isHeterograma():Boolean{
        return this.isHeterograma
    }

    fun analizeIsIsograma():Boolean{
        // Es una palabra o frase en la que cada letra aparece el mismo número de veces.
        // Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isograma de segundo orden y así sucesivamente.

        var isIsograma = true
        val numOcurrencias = ocurrencias[0].second
        this.ocurrencias.forEach{
            if (it.second != numOcurrencias){
                isIsograma = false
            }
        }
        return isIsograma
    }
    fun isIsograma():Boolean{
        return this.isIsograma
    }


    fun analizeisPangrama():Boolean{
        // https://es.wikipedia.org/wiki/Pangrama
        // Un pangrama  o frase holoalfabética es un texto que usa todas las letras posibles del alfabeto de un idioma.
        // Los pangramas perfectos son los pangramas que son también heterogramas, es decir en los que no se repite ninguna de las letras.

        //    Ejemplos de pangramas en español (con y sin marcas diacríticas) son:
        //
        //    (Simple y con sentido) Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.
        //    (De dos narraciones) Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.
        //    (De una sola narración) Jovencillo emponzoñado de whisky: ¡qué figurota exhibe!
        //    Es de notar que, además de ser un pangrama memorable y eficiente, presenta ligaduras de interés para el habla hispana.
        //    (De dos narraciones) José compró en Perú una vieja zampoña. Excusándose, Sofía tiró su whisky al desagüe de la banqueta.
        //    (De dos narraciones) El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja. (Este es usado para mostrar los estilos de letra en el sistema operativo

        var isPangrama = true
        var existe : Boolean
        alfabeto.forEach { letra ->

            existe = false
            ocurrencias.forEachIndexed { index, pair ->
                if (pair.first == letra){
                    existe = true
                }
            }
            if (!existe)
                isPangrama = false
        }

        return isPangrama
    }

    fun isPangrama():Boolean{
        return this.isPangrama
    }


    fun showOcurrencias(){
        println(this.ocurrencias)
    }
}





