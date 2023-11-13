package reto_43;

/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
public class JesusWay69 {

    public static void main(String[] args) {

        weatherStation(31, 24, 20);

    }

    public static void weatherStation(int days, int temperature , double percRain) {
        int tempMax = temperature;
        int tempMin = temperature;
        double rainProbAcc = 0.0;
        int rainyDays = 0;
        for (int i = 1; i < days + 1; i++) {
            double rainProb = Math.random() + rainProbAcc;
            double twoDegreesUp = Math.random();
            double twoDegreesDown = Math.random();
            if (rainProb < (percRain/100)) {
                System.out.print("el día " + i + " sí llovió");
                System.out.println(" y la temperatura fue de " + temperature + " grados");
                temperature--;
                rainyDays++;
            } else {
                System.out.print("el día " + i + " no llovió");
                System.out.println(" y la temperatura fue de " + temperature + " grados");
            }
            if (twoDegreesUp > 0.9)  temperature += 2;
            if (twoDegreesDown < 0.1) temperature -= 2;
            if (temperature > 25) rainProbAcc -= 0.2;
            if (temperature < 5) rainProbAcc += 0.2;
            if (temperature < tempMin) tempMin=temperature;
            if (temperature > tempMax) tempMax=temperature;

        }
        System.out.println("\nLlovió un total de " + rainyDays + " días");
        System.out.println("\nLa temperatura máxima fue de " + tempMax + " grados");
        System.out.println("\nLa temperatura mínima fue de " + tempMin + " grados");    }

}
