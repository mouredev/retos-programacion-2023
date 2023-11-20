package facil.reto43;

public class WeatherSimulator {

    public static void main(String[] args) {
        simulate(7, 25, 0.2);
    }

    public static void simulate(int days, double initialTemp, double initialRainProbability){
        double temperature = initialTemp;
        double chanceOfRain = initialRainProbability;
        double tempMax = temperature;
        double tempMin = temperature;
        int rainDays = 0;

        for (int i = 1; i <= days ; i++) {
            // simulate change of temperature
            if (Math.random() < 0.1){
                temperature += Math.random() < 0.5 ? 2 : -2;
            }

            // update rain probability
            if (temperature > 25) chanceOfRain += 0.2;
            else if (temperature < 5) chanceOfRain -= 0.2;

            // set limite to rain probability
            chanceOfRain = Math.min(1, Math.max(0, chanceOfRain));

            // simulate rain
            if (Math.random() < chanceOfRain){
                temperature -= 1;
                rainDays++;
            }

            // update math and min temperature
            tempMax = Math.max(tempMax, temperature);
            tempMin = Math.min(tempMin, temperature);
        }

        String data = String.format("Max temperature %s °C%nMin temperature %s °C%nRaining days %s", tempMax, tempMin, rainDays);

        System.out.println(data);
    }

}
