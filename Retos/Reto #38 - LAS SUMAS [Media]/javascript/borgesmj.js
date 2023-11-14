    function findCombination(lista, objetivo) {
    let result = []

    function evaluar(restante, combinacionActual, indexInicial) {
        //Si el objetivo fué completado, toma el array 
        //y lo haga push al restult general
        if (restante === 0) {
            result.push([...combinacionActual]);
            return;
        }

        //Si la suma se pasa del objetivo, regresa sin dar 
        //un array
        if (restante < 0) {
            return
        }

        // Mientras el codigo este funcionando
        // el código agrega con push otro item
        //Después de que la función recursiva haya terminado, 
        //el código elimina el último elemento agregado a 
        //combinacionActual utilizando pop(). Esto se hace para retroceder y 
        //probar otras combinaciones sin el elemento actual 
        //que se agregó en la iteración actual.

        for (let i = indexInicial; i < lista.length; i++) {
            combinacionActual.push(lista[i]);
            evaluar(restante - lista[i], combinacionActual, i + 1)
            combinacionActual.pop();
        }
    }
    evaluar(objetivo, [], 0)
    return result
}

console.log(findCombination([1, 5, 3, 2], 6))