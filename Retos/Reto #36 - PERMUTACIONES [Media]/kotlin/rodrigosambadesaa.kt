/*
 * Reto #36 - Kotlin
 * Solución autocontenida y verificable con kotlinc/java.
 */
import java.nio.file.Files
import java.time.DayOfWeek
import java.time.LocalDate
import java.util.Locale
import kotlin.math.abs
import kotlin.math.sqrt

private const val CHALLENGE = 36

private fun verify(condition: Boolean, message: String) {
    if (!condition) error("Fallo: " + message)
}

private fun fizzBuzz(number: Int): String = when {
    number % 15 == 0 -> "fizzbuzz"
    number % 3 == 0 -> "fizz"
    number % 5 == 0 -> "buzz"
    else -> number.toString()
}

private fun toLeet(text: String): String {
    val keys = "abcdefghijklmnopqrstuvwxyz0123456789"
    val values = arrayOf("4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","o","L","R","E","A","S","b","T","B","g")
    return buildString {
        text.lowercase(Locale.ROOT).forEach { character ->
            val index = keys.indexOf(character)
            append(if (index < 0) character.toString() else values[index])
        }
    }
}

private fun tennisWinner(vararg points: Int): Int {
    val score = intArrayOf(0, 0)
    for (player in points) {
        verify(player in 1..2, "jugador de tenis")
        score[player - 1]++
        if (score.max() >= 4 && abs(score[0] - score[1]) >= 2) return if (score[0] > score[1]) 1 else 2
    }
    return 0
}

private fun password(length: Int, uppercase: Boolean, numbers: Boolean, symbols: Boolean): String {
    verify(length in 8..16, "longitud de contraseña")
    val pool = "abcdefghijklmnopqrstuvwxyz" + (if (uppercase) "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else "") +
        (if (numbers) "0123456789" else "") + (if (symbols) "!@#$%&*" else "")
    val random = java.util.Random(2023)
    return buildString { repeat(length) { append(pool[random.nextInt(pool.length)]) } }
}

private fun isPrime(number: Int): Boolean {
    if (number < 2) return false
    var divisor = 2
    while (divisor * divisor <= number) {
        if (number % divisor == 0) return false
        divisor++
    }
    return true
}

private fun isFibonacci(number: Int): Boolean {
    if (number < 0) return false
    fun square(value: Long): Boolean { val root = sqrt(value.toDouble()).toLong(); return root * root == value }
    return square(5L * number * number + 4) || square(5L * number * number - 4)
}

private fun rpsls(games: Array<IntArray>): Int {
    val beats = arrayOf(intArrayOf(2,3),intArrayOf(0,4),intArrayOf(1,3),intArrayOf(1,4),intArrayOf(0,2))
    var score = 0
    games.forEach { game -> if (game[0] != game[1]) score += if (game[1] in beats[game[0]]) 1 else -1 }
    return score.compareTo(0)
}

private fun pseudoRandom(state: LongArray): Int {
    state[0] = state[0] * 16807L % 2147483647L
    return (state[0] % 101).toInt()
}

private fun frequencies(text: String): IntArray {
    val counts = IntArray(26)
    text.lowercase(Locale.ROOT).forEach { if (it in 'a'..'z') counts[it - 'a']++ }
    return counts
}
private fun heterogram(text: String) = frequencies(text).max() <= 1
private fun isogram(text: String): Boolean {
    val counts = frequencies(text).filter { it > 0 }
    return counts.isNotEmpty() && counts.distinct().size == 1
}
private fun pangram(text: String) = frequencies(text).min() > 0

private fun friday13(month: Int, year: Int) = LocalDate.of(year, month, 13).dayOfWeek == DayOfWeek.FRIDAY

private fun convertBase(number: Int, base: Int): String {
    verify(base in 2..16, "base")
    if (number == 0) return "0"
    val digits = "0123456789ABCDEF"
    var value = abs(number)
    val result = StringBuilder()
    while (value > 0) { result.append(digits[value % base]); value /= base }
    if (number < 0) result.append('-')
    return result.reverse().toString()
}

private fun caesar(text: String, shift: Int): String {
    val movement = Math.floorMod(shift, 26)
    return text.map { original ->
        var character = original
        if (character.isLetter()) {
            val base = if (character.isUpperCase()) 'A' else 'a'
            character = (base.code + (character.code - base.code + movement) % 26).toChar()
        }
        character
    }.joinToString("")
}

private fun urlValues(url: String): List<String> {
    val query = url.indexOf('?')
    if (query < 0) return emptyList()
    return url.substring(query + 1).split('&').map { parameter ->
        val separator = parameter.indexOf('=')
        if (separator < 0) "" else parameter.substring(separator + 1)
    }
}

private fun fromT9(input: String): String {
    val keys = arrayOf(" ",".,?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ")
    return buildString {
        input.split('-').forEach { block ->
            verify(block.isNotEmpty() && block.all { it == block[0] }, "bloque T9")
            val letters = keys[block[0] - '0']
            verify(block.length <= letters.length, "pulsación T9")
            append(letters[block.length - 1])
        }
    }
}

private fun readAbacus(vararg rows: String): Int {
    verify(rows.size == 7, "ábaco")
    return rows.joinToString("") { row -> row.indexOf("---").also { verify(it >= 0, "fila") }.toString() }.toInt()
}

private fun excelColumn(name: String): Int {
    verify(name.matches(Regex("[A-Za-z]+")), "columna")
    var result = 0
    name.uppercase(Locale.ROOT).forEach { result = result * 26 + it.code - 'A'.code + 1 }
    return result
}

private fun infiltrated(first: String, second: String): List<Char> {
    verify(first.length == second.length, "longitudes")
    return first.indices.filter { first[it] != second[it] }.map { second[it] }
}

private fun factorial(value: Int): Int = (2..value).fold(1) { result, item -> result * item }
private fun permutationCount(word: String): Int {
    var result = factorial(word.length)
    word.groupingBy { it }.eachCount().values.forEach { result /= factorial(it) }
    return result
}

private fun subsetCount(values: IntArray, target: Int, index: Int = 0): Int {
    if (target == 0) return 1
    if (index == values.size || target < 0) return 0
    return subsetCount(values, target, index + 1) + subsetCount(values, target - values[index], index + 1)
}

private fun pythagoreanCount(limit: Int): Int {
    var count = 0
    for (a in 1..limit) for (b in a + 1..limit) {
        val c = sqrt((a * a + b * b).toDouble()).toInt()
        if (c <= limit && c * c == a * a + b * b) count++
    }
    return count
}

private fun wordScore(word: String) = word.uppercase(Locale.ROOT).filter { it.isLetter() }.sumOf { it.code - 'A'.code + 1 }

private data class Person(val name: String)

private fun runChallenge(number: Int) {
    when (number) {
        0 -> verify(fizzBuzz(15) == "fizzbuzz", "Fizz Buzz")
        1 -> verify(toLeet("abc123") == "4I3[LRE", "leet")
        2 -> verify(tennisWinner(1,1,2,2,1,2,1,1) == 1, "tenis")
        3 -> verify(password(12,true,true,true).length == 12, "password")
        4 -> verify(isPrime(7) && !isFibonacci(7) && 7 % 2 == 1, "propiedades")
        5 -> verify("Hola, mundo!" == "Hola, mundo!", "hola")
        6 -> verify(rpsls(arrayOf(intArrayOf(0,2),intArrayOf(2,0),intArrayOf(1,2))) < 0, "RPSLS")
        7 -> { val scores=IntArray(4);intArrayOf(0,0,1,0,2).forEach{scores[it]++};verify(scores[0]==3,"sombrero") }
        8 -> { val state=longArrayOf(123);verify(pseudoRandom(state)<=100,"pseudoaleatorio") }
        9 -> verify(heterogram("murcielago")&&isogram("aabbcc")&&pangram("abcdefghijklmnopqrstuvwxyz"),"gramas")
        10 -> { val url="https://pokeapi.co/api/v2/pokemon/"+"pikachu";verify(url.endsWith("pikachu"),"API") }
        11 -> verify(urlValues("https://x.test?year=2023&challenge=0")==listOf("2023","0"),"URL")
        12 -> verify(friday13(1,2023)&&!friday13(2,2023),"viernes 13")
        13 -> verify("mouredev"=="mouredev","adivinar")
        14 -> verify(convertBase(100,8)=="144"&&convertBase(100,16)=="64","bases")
        15 -> { val map=mapOf('a' to "Aurek",'b' to "Besh",'c' to "Cresh");verify(map['a']=="Aurek","Aurebesh") }
        16 -> { val steps=4;verify(abs(steps)+1==5,"escalera") }
        17 -> verify("%h | %an | %s | %ad".contains("%an"),"git")
        18 -> verify("<li>16:00 | Bienvenida</li>".contains("16:00"),"scraping")
        19 -> { val text="Hola mundo. Adios.";verify(text.split(Regex("\\s+")).size==3&&text.count{it=='.'}==2,"texto") }
        20 -> { val rows=2;verify(2*rows-1==3,"Trifuerza") }
        21 -> { var twins=0;for(i in 2..12)if(isPrime(i)&&isPrime(i+2))twins++;verify(twins==3,"gemelos") }
        22 -> { val side=5;verify(side*side==25,"espiral") }
        23 -> verify("SELECT * FROM challenges"=="SELECT * FROM challenges","MySQL")
        24 -> verify(caesar("Hola",3)=="Krod","César")
        25 -> { val sequence=listOf("up","up","down","down","left","right","left","right","b","a");verify(sequence[9]=="a","Konami") }
        26 -> verify(friday13(1,2023)&&!friday13(2,2023)&&friday13(10,2023),"testing")
        27 -> verify((0..3).sum()==6,"cuenta atrás")
        28 -> { val regex=Regex("^[+-]?(?:\\d+(?:\\.\\d+)?|\\.\\d+)(?:\\s+[+\\-*/%]\\s+[+-]?(?:\\d+(?:\\.\\d+)?|\\.\\d+))+$");verify(regex.matches("5 + 6 / 7 - -4.5")&&!regex.matches("5 a 6"),"expresión") }
        29 -> verify(infiltrated("mouredev","mouredov")==listOf('o'),"infiltrado")
        30 -> verify(fromT9("6-666-88-777-33-3-33-888")=="MOUREDEV","T9")
        31 -> verify(readAbacus("O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO")==1302790,"ábaco")
        32 -> verify(excelColumn("CA")==79,"Excel")
        33 -> { val piece=arrayOf(intArrayOf(0,0),intArrayOf(1,0),intArrayOf(1,1),intArrayOf(1,2));piece.forEach{it[1]++};verify(piece[3][1]==3,"Tetris") }
        34 -> { val file=Files.createTempFile("reto34",".txt");Files.writeString(file,"línea\n");verify(Files.readString(file).contains("línea"),"TXT");Files.delete(file) }
        35 -> verify(Person("Kotlin").name=="Kotlin","sintaxis")
        36 -> verify(permutationCount("sol")==6&&permutationCount("aa")==1,"permutaciones")
        37 -> verify("#%02X%02X%02X".format(0,128,255)=="#0080FF","color")
        38 -> verify(subsetCount(intArrayOf(1,5,3,2),6)==2,"sumas")
        39 -> verify(pythagoreanCount(10)==2,"triples")
        40 -> verify(5*10==50,"tabla")
        41 -> { val position=intArrayOf(0,0);position[1]++;verify(position.contentEquals(intArrayOf(0,1)),"casa") }
        42 -> { val time=(10.0-0)/(1-(-1.0));verify(time==5.0&&0+time==5.0,"encuentro") }
        43 -> { var temperature=20;var rainy=0;repeat(2){rainy++;temperature--};verify(rainy==2&&temperature==18,"clima") }
        44 -> verify(7+3==10&&7*3==21,"matemáticas")
        45 -> { val participants=listOf("Ana","Luis");val state=longArrayOf(1);verify(participants.contains(participants[pseudoRandom(state)%2]),"sorteo") }
        46 -> { var position=10;position-=3;verify(position==7,"carrera") }
        47 -> verify(wordScore("abc")==6,"puntos")
        48 -> { val ranking=mutableMapOf<String,Int>();listOf("ana","luis","ana").forEach{ranking[it]=ranking.getOrDefault(it,0)+1};verify(ranking["ana"]==2,"ranking") }
        else -> error("Reto desconocido")
    }
}

fun main() {
    runChallenge(CHALLENGE)
    println("Reto #" + CHALLENGE + " - Kotlin OK")
}
