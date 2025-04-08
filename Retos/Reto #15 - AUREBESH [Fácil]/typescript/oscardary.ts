/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

function main() {

    const mapLatinToAurebesh: Map<string, string> = new Map([
        ["A", "Aurek"],
        ["B", "Besh"],
        ["C", "Cresh"],
        ["D", "Dorn"],
        ["E", "Esk"],
        ["F", "Forn"],
        ["G", "Grek"],
        ["H", "Herf"],
        ["I", "Isk"],
        ["J", "Jenth"],
        ["K", "Krill"],
        ["L", "Leth"],
        ["M", "Mern"],
        ["N", "Nern"],
        ["O", "Osk"],
        ["P", "Peth"],
        ["Q", "Qek"],
        ["R", "Resh"],
        ["S", "Senth"],
        ["T", "Trill"],
        ["U", "Usk"],
        ["V", "Vev"],
        ["W", "Wesk"],
        ["X", "Xesh"],
        ["Y", "Yirt"],
        ["Z", "Zerek"],

        // Digraphs (opcional)
        ["CH", "Cherek"],
        ["AE", "Enth"],
        ["EO", "Nen"],
        ["KH", "Orenth"],
        ["SH", "Shen"],
        ["TH", "Thesh"]
    ]);

    function fnLatinoAurebesh(mapLatinToAurebesh: Map<string, string>, texto: string) {
        let textoAurebesh = ""
        for (const caracter of texto.toUpperCase()) {
            textoAurebesh = textoAurebesh + (caracter == " " ? "  " : (mapLatinToAurebesh.get(caracter) || caracter )) + " "
        }
        return textoAurebesh.trim()
    }

    function fnLatinoAurebeshV2(mapLatinToAurebesh: Map<string, string>, texto: string) {
        return texto            //Texto original
            .toUpperCase()      //Convertir a MAYUS
            .split("")          //Separar cada caracter
            .map(char => char == " " ? "  " : (mapLatinToAurebesh.get(char) || char ))
            .join(" ")          //Unir cada fragmento separado por espacio
            .trim()             //Eliminar espacio al final
    }

    console.log(fnLatinoAurebeshV2(mapLatinToAurebesh,"OSCAR DARIO RIVERA LOPEZ"))

}

main()