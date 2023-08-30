<?php // 8.0
// Punto 1: Hola, mundo!
echo "Hola, mundo!\n";

// Punto 2: Crea una variable de texto o string
$miTexto = "¡Hola desde PHP!\n";

// Punto 3: Crea una variable de número entero
$miEntero = 42;

// Punto 4: Crea una variable de número con decimales
$miDecimal = 3.14;

// Punto 5: Crea una variable de tipo booleano
$miBooleano = true;

// Punto 6: Crea una constante
define("MI_CONSTANTE", 10);

// Punto 7: Usa un if, else if y else
if ($miEntero > 50) {
    echo "El número es mayor que 50\n";
} elseif ($miEntero < 50) {
    echo "El número es menor que 50\n";
} else {
    echo "El número es igual a 50\n";
}

// Punto 8: Crea un Array
$miArray = [1, 2, 3, 4, 5];

// Punto 9: Crea una lista (array en PHP)
$miLista = ["Manzana", "Banana", "Naranja"];

// Punto 10: Crea una tupla (no aplicable en PHP)

// Punto 11: Crea un set (no aplicable en PHP)

// Punto 12: Crea un diccionario (array asociativo en PHP)
$miDiccionario = [
    "clave1" => "valor1",
    "clave2" => "valor2"
];

// Punto 13: Usa un ciclo for
for ($i = 0; $i < count($miArray); $i++) {
    echo $miArray[$i] . "\n";
}

// Punto 14: Usa un ciclo foreach
foreach ($miLista as $elemento) {
    echo $elemento . "\n";
}

// Punto 15: Usa un ciclo while
$contador = 0;
while ($contador < 3) {
    echo "Contador: " . $contador . "\n";
    $contador++;
}

// Punto 16: Crea una función sin parámetros que no retorne nada
function funcionSinParametros() {
    echo "Función sin parámetros\n";
}
funcionSinParametros();

// Punto 17: Crea una función con parámetros que no retorne nada
function funcionConParametros($param1, $param2) {
    echo "Parámetro 1: " . $param1 . "\n";
    echo "Parámetro 2: " . $param2 . "\n";
}
funcionConParametros(1, "dos");

// Punto 18: Crea una función con parámetros que retorne valor
function funcionConRetorno($a, $b) {
    return $a + $b;
}
$resultado = funcionConRetorno(3, 4);
echo "Resultado: " . $resultado . "\n";

// Punto 19: Crea una clase
class Persona {
    public $nombre;
    public $edad;

    function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }
}

// Punto 20: Muestra control de excepciones (try-catch en PHP)
try {
    $division = $miEntero / 0;
    echo $division . "\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
