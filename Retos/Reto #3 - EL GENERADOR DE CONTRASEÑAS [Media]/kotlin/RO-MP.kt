import kotlin.random.Random


fun main() {
    // Params definition
    val length = 16
    val containCapitals = true
    val containNumbers = true
    val containSymbols = true

    if (length in 8..16) {
        val password = getPassword(length, containCapitals, containNumbers, containSymbols)
        println(password)
    } else{
        println("Introduce a correct length")
    }
}


fun getPassword(length: Int, containCapitals: Boolean, containNumbers: Boolean, containSymbols: Boolean): String {
    val letters = listOf("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    val numbers = listOf("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    val symbols = listOf("!", "#", "$", "%", "&", "/", "+", "^", "*", "~", "?")

    // Lambda to get a random String from any List of letters, numbers or symbols
    val nextCharacterFromList: (List<String>) -> String = { list ->
        list[Random.nextInt(0,(list.size))]
    }

    // Define which lists will be used
    val possibleLists = mutableListOf(letters)
    if (containNumbers) possibleLists.add(numbers)
    if (containSymbols) possibleLists.add(symbols)

    var password = ""
    repeat(length){
        val randomListIndex = Random.nextInt(0,(possibleLists.size))
        // Return random list from the selected lists
        val list = possibleLists[randomListIndex]

        var nextCharacter = nextCharacterFromList(list)

        // Change just letter to upperCase with a random selection
        if (randomListIndex == 0  && containCapitals){
            if (Random.nextBoolean()) nextCharacter = nextCharacter.toUpperCase()
        }

        // Concatenate password
        password = "$password$nextCharacter"
    }

    return password
}

