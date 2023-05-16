<?php
//reto 19
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */


$Texto = "La Fiscalía Provincial de Medio Ambiente y Urbanismo de Girona ha denunciado penalmente a la Junta de Gobierno Local de Begur (Girona) e investiga si el ayuntamiento ha cometido alguna irregularidad urbanística en la zona del Puig Montcal. Ecologistas en Acción, SOS Costa Brava y Salvem Begur presentaron una denuncia ante Fiscalía en la que acusaban al Consistorio de haber cometido delitos de prevaricación urbanística y delitos contra la ordenación del territorio relacionados con la urbanización Montcal-2, en la zona de Aiguablava.";

// Inicializar variables
$totalPalabras = 0;
$longitudTotal = 0;
$numOraciones = 0;
$palabraMasLarga = "";

// Separar el texto en palabras utilizando el espacio como delimitador
$palabras = explode(" ", $texto);

// Recorrer cada palabra
foreach ($palabras as $palabra) {
    // Eliminar cualquier puntuación al final de la palabra (punto, coma, etc.) para no contar el caracter como
    // parte del string
    $palabra = rtrim($palabra, ".,;:!?");

    // Contar el número de palabras
    if (!empty($palabra)) {
        $totalPalabras++;

        // Calcular la longitud de la palabra y agregarla al total
        $longitudPalabra = strlen($palabra);
        $longitudTotal += $longitudPalabra; 

        // Verificar si la palabra es la más larga hasta ahora
        if ($longitudPalabra > strlen($palabraMasLarga)) {
            $palabraMasLarga = $palabra;
        }
    }

    // Contar el número de oraciones
    if (strpos($palabra, ".") !== false) {
        $numOraciones++;
    }
}

// Calcular la longitud media de las palabras
$longitudMedia = $longitudTotal / $totalPalabras;

// Imprimir los resultados
echo "Número total de palabras: " . $totalPalabras . "<br>";
echo "Longitud media de las palabras: " . $longitudMedia . "<br>";
echo "Número de oraciones: " . $numOraciones . "<br>";
echo "Palabra más larga: " . $palabraMasLarga . "<br>";
?>