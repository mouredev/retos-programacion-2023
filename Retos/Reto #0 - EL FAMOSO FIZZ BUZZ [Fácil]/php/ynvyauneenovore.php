<?php
/**
 * Reto #0: EL FAMOSO "FIZZ BUZZ"
 *
 * Descripción: Escribe un programa que muestra por consola los números del 1 al 100,
 * sustituyendo múltiplos de 3 por "Fizz", múltiplos de 5 por "Buzz", y múltiplos de ambos por "FizzBuzz".
 *
 * Autor: Yovan Ramon Yaune Enovore
 * Fecha: 05-08-2023
 *
 * Aplicación de Principios SOLID:
 *
 * - Principio de Responsabilidad Única (SRP):
 *   - Las clases `FizzRule`, `BuzzRule` y `FizzBuzz` tienen una única responsabilidad bien definida,
 *     separando la lógica de generación de reglas y resultados.
 *
 * - Principio de Abierto/Cerrado (OCP):
 *   - Las clases de reglas (`FizzRule`, `BuzzRule`) implementan la interfaz `RuleInterface`,
 *     permitiendo agregar nuevas reglas sin modificar el código existente.
 *   - La clase `FizzBuzz` puede extenderse para manejar nuevas reglas sin cambiar su estructura principal.
 *
 * - Principio de Sustitución de Liskov (LSP):
 *   - No se presenta una violación directa del LSP, ya que todas las clases derivadas cumplen
 *     con los contratos definidos en la interfaz `RuleInterface`.
 *
 * - Principio de Segregación de la Interfaz (ISP):
 *   - La interfaz `RuleInterface` es pequeña y cohesiva, conteniendo solo métodos relevantes
 *     para la generación de reglas Fizz y Buzz.
 *   - Las clases `FizzRule` y `BuzzRule` implementan solo los métodos requeridos por la interfaz,
 *     evitando la implementación de métodos innecesarios.
 *
 * - Principio de Inversión de Dependencias (DIP):
 *   - La clase `FizzBuzz` depende de abstracciones (la interfaz `RuleInterface`) en lugar de detalles concretos,
 *     permitiendo la inyección de diferentes reglas sin acoplar el código principal.
 *
 * Notas: Cualquier consulta: yovanuxf@gmail.com
 */

// Define una interfaz para las reglas de Fizz y Buzz
interface RuleInterface {
    public function check(int $number): bool;
    public function getValue(): string;
}

// Implementa la regla para "Fizz"
class FizzRule implements RuleInterface {
    public function check(int $number): bool {
        return $number % 3 === 0;
    }

    public function getValue(): string {
        return 'Fizz';
    }
}

// Implementa la regla para "Buzz"
class BuzzRule implements RuleInterface {
    public function check(int $number): bool {
        return $number % 5 === 0;
    }

    public function getValue(): string {
        return 'Buzz';
    }
}

// Clase principal que genera y muestra los resultados de FizzBuzz
class FizzBuzz {
    private $rules = [];

    // Constructor que recibe un array de reglas
    public function __construct(array $rules) {
        $this->rules = $rules;
    }

    // Genera un array de resultados según las reglas
    public function generate(int $n): array {
        $result = [];
        for ($i = 1; $i <= $n; $i++) {
            $value = '';
            foreach ($this->rules as $rule) {
                if ($rule->check($i)) {
                    $value .= $rule->getValue();
                }
            }
            // Si no se aplica ninguna regla, agrega el número
            $result[] = ($value !== '') ? $value : (string)$i;
        }
        return $result;
    }

    // Muestra los resultados en la consola
    public function printResult(int $n): void {
        $result = $this->generate($n);
        foreach ($result as $item) {
            echo $item . PHP_EOL;
        }
    }
}

// Configura las reglas (puedes agregar o modificar reglas aquí)
$rules = [new FizzRule(), new BuzzRule()];

// Crea una instancia de FizzBuzz con las reglas configuradas
$fizzBuzz = new FizzBuzz($rules);

// Define tus datos aquí
$nombre = 'ynvYauneEnovore';
$fecha = '05-08-2023';

// Imprime el encabezado con tus datos
echo "Reto #0: EL FAMOSO \"FIZZ BUZZ\"\n";
echo "Autor: $nombre\n";
echo "Fecha: $fecha\n\n";

// Define el número máximo para el desafío
$number = 100;

// Muestra los resultados
$fizzBuzz->printResult($number);

?>
