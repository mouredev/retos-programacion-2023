<?php

// Imprimir "Hola, mundo!"
echo "Hola, mundo!\n";

// Variables de diferentes tipos
$texto = "Hola";
$numeroEntero = 42;
$numeroDecimal = 3.14;
$esVerdad = true;

// Constante
define("CONSTANTE", 10);

// Uso de if, else if y else
if ($numeroEntero > 50) {
  echo "El número es mayor que 50.\n";
} else if ($numeroEntero < 50) {
  echo "El número es menor que 50.\n";
} else {
  echo "El número es igual a 50.\n";
}

// Estructuras de datos
$arreglo = array(1, 2, 3, 4, 5);
$lista = array(10, 20, 30);
$tupla = array("Tupla", 5, 2.5);
$conjunto = array("rojo", "verde", "azul");
$diccionario = array("uno" => 1, "dos" => 2, "tres" => 3);

// Uso de foreach
foreach ($arreglo as $valor) {
  echo $valor . " ";
}
echo "\n";

foreach ($lista as $num) {
  echo $num . " ";
}
echo "\n";

// Uso de while
$contador = 0;
while ($contador < 3) {
  echo $contador . " ";
  $contador++;
}
echo "\n";

// Función para sumar dos números
function suma($a, $b)
{
  return $a + $b;
}

// Llamada a función con retorno
$resultado = suma(7, 8);
echo "Resultado de la suma: " . $resultado . "\n";

// Clase Persona
class Persona
{
  public $nombre;
  public $edad;

  public function __construct($n, $e)
  {
    $this->nombre = $n;
    $this->edad = $e;
  }

  public function saludar()
  {
    echo "Hola, soy " . $this->nombre . " y tengo " . $this->edad . " años.\n";
  }
}

// Creación y uso de objeto de clase Persona
$persona = new Persona("Juan", 25);
$persona->saludar();

// Control de excepciones
try {
  $dividendo = 10;
  $divisor = 0;
  if ($divisor == 0) {
    throw new Exception("Divisor no puede ser cero");
  }
  $resultadoDivision = $dividendo / $divisor;
  echo "Resultado de la división: " . $resultadoDivision . PHP_EOL;
} catch (Exception $e) {
  echo "Error: " . $e->getMessage() . PHP_EOL;
}
