class Qv1ko {

    public static void main(String[] args) {
        weather(9, 92, 7);
    }

    private static void weather(int temperature, int rainProbability, int days) {

        rainProbability = Math.abs(rainProbability);
        days = Math.abs(days);

        boolean rain = (int)(Math.random() * 100) < rainProbability;
        int maxTemperature = temperature, minTemperature = temperature;
        int rainyDays = 0;
        int possibilities = 0;

        for (int i = 0; i < days; i++) {

            System.out.println("\nDay " + (i + 1) + ":\n Temperature: " + temperature + (rain ? "\n It rains" : "\n No rain"));

            if (temperature > maxTemperature) {
                maxTemperature = temperature;
            } else if (temperature < minTemperature) {
                minTemperature = temperature;
            }
            rainyDays += rain ? 1 : 0;

            possibilities = (int)(Math.random() * 10);

            temperature += (possibilities == 1) ? 2 : (possibilities == 2) ? -2 : 0;
            rainProbability += (temperature > 25) ? 20 : (temperature < 5) ? -20 : 0;

            if (rainProbability >= 100) {
                temperature--;
                rainProbability = 100;
            } else if (rainProbability <= 0) {
                temperature++;
                rainProbability = 0;
            }
            
            rain = (int)(Math.random() * 100) < rainProbability;

        }

        System.out.println("\nMaximum temperature: " + maxTemperature + "\nMinimum temperature: " + minTemperature + "\nRainy days: " + rainyDays);

    }

}
