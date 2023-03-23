/* Changing a little bit this formula (character - ¨altccode¨ % 26) that i learned on
 * https://cs50.harvard.edu/x/2020/psets/2/caesar/ the solution to this challenge was easy peasy
 */
var text = "abcd"
var hackerAlphabet = arrayOf("4","|3","[",")","3","|=","&","#","1",
    ",_|","|<","|_","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)",
    "\\/","\\/\\/","><","j","2")
var result:String = ""

print("Ingresa el texto a encriptar: ")
text = readLine()!!.toLowerCase()

for (i in text){
    /* With the formula inside the index we know the position in the alphabet from 0 to 25, with that info
     * we know wich charater take from hackerAlphabet and add it to Result
     */
        result += if (i == ' ') " " else hackerAlphabet[i.toByte().toInt() - 'a'.toInt()]
}

println("Tu texto en alfabeto \"Si quieres hacer del mundo un lugar mejor mirate al espejo y haz un cambio\" Hacker es: " + result)