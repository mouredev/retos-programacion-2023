package reto3.kotlin

import java.util.*
import java.util.concurrent.ThreadLocalRandom

fun main(){
    val jitosDev = jitos_dev()
    val password1 = jitosDev.generatePassword(2, 4, jitos_dev.Options.CAN_UPPERCASE, jitos_dev.Options.CAN_NUMBERS, jitos_dev.Options.CAN_SYMBOLS);
    val password2 = jitosDev.generatePassword(2, 3, jitos_dev.Options.CAN_UPPERCASE, jitos_dev.Options.CAN_NUMBERS);
    val password3 = jitosDev.generatePassword(8, 16, jitos_dev.Options.CAN_NUMBERS, jitos_dev.Options.CAN_SYMBOLS);
    val password4 = jitosDev.generatePassword(8, 16);
    val password5 = jitosDev.generatePassword(8, 16, jitos_dev.Options.CAN_UPPERCASE);
    println(password1);
    println(password2);
    println(password3);
    println(password4);
    println(password5);
}

class jitos_dev {

     fun generatePassword(minLength:Int, maxLength:Int, vararg options: Options): String {
        //Si el mínimo es menor que el máximo o el máximo o el mínimo es menor o igual a 0 devolvemos 0
        if (maxLength < minLength || maxLength <= 0 || minLength <= 0)
            return "0";

        //Lista para todos los códigos ASCI que vamos a utilizar. Incluimos minúsculas directamente
        val ASCI_CODES: ArrayList<Int> = ArrayList(getLettersLowerCase()) //(getLettersLowerCase());

        //Lista con las opciones que nos pasan y que podemos tener para incluir en la contraseña
        val optionsList: List<Options> = options.toList()

        if (optionsList.contains(Options.CAN_UPPERCASE))
            ASCI_CODES.addAll(getLettersUpperCase())

        if (optionsList.contains(Options.CAN_NUMBERS))
            ASCI_CODES.addAll(getNumbers())

        if (optionsList.contains(Options.CAN_SYMBOLS))
            ASCI_CODES.addAll(getASCISymbol())

        //Calculamos el tamaño aleatorio de la contraseña en función de los valores que nos pasan
        val lengthPassword:Int = getRandom(minLength, maxLength)

        val password: StringBuilder = StringBuilder()
        //Recorremos el bucle tantas veces como la longitud de la contraseña y le asignamos un valor aleatorio cada vez
        for (i in 0..lengthPassword) {
            val valueRandom: Int = getRandom(0, ASCI_CODES.size - 1);
            val code: Int = ASCI_CODES.get(valueRandom);
            password.append(code.toChar());
        }

        return password.toString();
    }

    /*Lista con los códigos ASCI de las letras minúsculas. Las minúsculas empiezan en el 97 hasta el 122 incluido*/
    private fun getLettersLowerCase(): ArrayList<Int> {
        val ASCI_List: ArrayList<Int> = ArrayList()

        for (i in 97..122) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /*Lista con los códigos ASCI de las letras mayúsculas. Las mayúsculas empiezan en el 65 hasta el 97 incluido*/
    private fun getLettersUpperCase(): ArrayList<Int> {
        val ASCI_List = ArrayList<Int>()

        for (i in 65..90) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /*Lista con los códigos ASCI de los números. Los números empiezan en el 48 hasta el 57 incluido*/
    private fun getNumbers(): ArrayList<Int> {
        val ASCI_List = ArrayList<Int>()

        for (i in 48..57) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /* Lista con los códigos ASCI de los símbolos que vamos a poder utilizar. Si añadimos uno nuevo
    * solo lo tenemos que añadir al método getSymbols y este los añade todos*/
    private fun getASCISymbol(): ArrayList<Int> {
        val ASCI_List = ArrayList<Int>()
        val symbols: Array<Symbol> = getSymbols()

        Arrays.stream(symbols).forEach{ symbol: Symbol  ->
            ASCI_List.add(symbol.ASCI);
        }

        return ASCI_List;
    }

    /*Array con los símbolos que podemos utilizar*/
    private fun getSymbols(): Array<Symbol> {
        return arrayOf(Symbol.EXCLAMACION, Symbol.ALMOHADILLA, Symbol.DOLLAR, Symbol.PORCENTAJE, Symbol.AMPERSAND,
                Symbol.ASTERISCO, Symbol.SUMA, Symbol.INTERROGACION)
    }

    /*Nos devuelve un entero positivo entre dos valores dados con los propios valores incluidos*/
    private fun getRandom(start: Int, end: Int): Int {
        return ThreadLocalRandom.current().nextInt(start, end + 1);
    }

    /*El número del símbolo corresponde con su código ASCI*/
    enum class Symbol(var ASCI: Int) {
        EXCLAMACION(33), ALMOHADILLA(35), DOLLAR(36), PORCENTAJE(37), AMPERSAND(38),
        ASTERISCO(42), SUMA(43), INTERROGACION(63);
    }

    enum class Options {
        CAN_UPPERCASE, CAN_NUMBERS, CAN_SYMBOLS;
    }
}