/* ******* PASSWORD GENERATION LOGIC ******************/
def upperCaseAlphabet = { 'A'..'Z' }
def baseAlphabet = { 'a'..'z' }
def numberAlphabet = { '0'..'9' }
def symbolAlphabet = {
    def withoutSymbolsAlphabet = generateAlphabet([baseAlphabet, upperCaseAlphabet, numberAlphabet])
    (32..127 as Character[]).findAll { character -> !withoutSymbolsAlphabet.contains(character) }.collect()
}

static def generateAlphabet(List<Closure<Character[]>> alphabetGenerator) {
    alphabetGenerator.findAll { it != null }.collect { it() }.flatten()
}

static def generatePassword(Integer length, List<Character> alphabet) {
    def random = new Random()
    (1..length).collect { alphabet[random.nextInt(0, alphabet.size() - 1)] }.join()
}

/* ******* INPUT VALUES MANAGEMENT FROM STDIN ******************/

class InvalidInputValueException extends RuntimeException {
    InvalidInputValueException(String message) {
        super(message)
    }
}

def retrieveBoolean(String message) {
    print(message as String)
    def input = System.in.newReader().readLine() as String
    if (input.trim().toUpperCase() == 'S') return true
    if (input.trim().toUpperCase() == 'N') return false
    throw new InvalidInputValueException("El valor $input no puede ser convertido a un valor booleano")
}

def retrieveInteger(def message, def validation = { n -> true }) {
    print(message as String)
    def input = System.in.newReader().readLine() as String
    if (!input.trim().isNumber()) {
        throw new InvalidInputValueException("El valor $input no puede ser convertido a un valor numérico")
    }
    def number = Integer.valueOf(input.trim())
    if (!validation(number)) {
        throw new InvalidInputValueException("El valor $input no está dentro del rango de valores permitido")
    }
    return Integer.valueOf(input.trim())
}

/* **************** MAIN ******************/
try {
    def length = retrieveInteger("Introduce la longitud deseada para la contraseña [8-16] : ", { n -> n > 7 && n < 17 })
    def uppercase = retrieveBoolean("Incluir mayusculas (S/N): ")
    def numbers = retrieveBoolean("Incluir números (S/N): ")
    def symbols = retrieveBoolean("Incluir simbolos (S/N): ")

    println("La contraseñe requerida de longitud " +
            "$length ${uppercase ? "con mayúsculas" : ""}" +
            "${numbers ? " con números" : ""}" +
            "${symbols ? " con símbolos" : ""}")

    println(generatePassword(length, generateAlphabet([baseAlphabet, uppercase ? upperCaseAlphabet : null, numbers ? numberAlphabet : null, symbols ? symbolAlphabet : null]) as List<Character>))

} catch (InvalidInputValueException e) {
    println("ERROR!!!!")
    println(e.getMessage())

}
