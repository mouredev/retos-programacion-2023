/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


const urlParameters = ( url: string ): string[] => {

    const params = url.split('?')[1]?.split('&') ?? [];
    return params.reduce( (acc: string[], crv: string) => [ ...acc, crv.split('=')[1] ], [] );

}

console.log( urlParameters( 'https://retosdeprogramacion.com?year=2023&challenge=0' ) );