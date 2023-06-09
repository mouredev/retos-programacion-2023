/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

/**
 * Clase que genera números pseudoaleatorios utilizando el algoritmo de congruencia lineal
 * Contiene un metodo estático que devuelve un número pseudoaleatorio entre un rango de valores
 *
 */
class CustomRandom{

    /**
     * Genera una semilla para el algoritmo de congruencia lineal
     */
    private get_seed(): number{

        const multiplier:number = 1103515245;
        const increment = 12345;
        const bits = 2 ** 32;

        return (multiplier * this.getTime() + increment) % bits


   }

    /**
     * Genera un retraso de tiempo para que el algoritmo de congruencia lineal funcione correctamente
     */
    delaySync(ms: number) {
        const start = new Date().getTime();
        while (new Date().getTime() < start + ms) {
            // Consumir tiempo de CPU
        }

    }

    /**
     * Devuelve el tiempo actual en milisegundos
     */
    getTime(): number {
        this.delaySync(10);
        return new Date().getTime();
    }

    /**
     * Devuelve un número pseudoaleatorio entre un rango de valores
     * @param min
     * @param max
     */
    public static random(min: number, max: number): number{
        const customRandom = new CustomRandom();
        let seed = customRandom.get_seed();
        return Math.floor(min+(seed%max))
    }
}


/**
 * Código de prueba.Genera 10 números pseudoaleatorios entre 1 y 100
 */
for(let i = 0; i < 10; i++) {
    console.log(CustomRandom.random(1, 100))
}