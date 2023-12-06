import java.util.*;

public class SelectionHat {

    public static void main(String[] args) {
        sortingHat();
    }

    private static void sortingHat() {
        Map<String,Integer> houses = new HashMap<>();
        houses.put("gryffindor", 0);
        houses.put("hufflepuff", 0);
        houses.put("ravenclaw", 0);
        houses.put("slytherin", 0);

        int maxPoints = 0;
        String selectedHouse = "";

        System.out.println("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.");

        for(int i = 0; i < 5; i++) {
            System.out.println(questions(i));
            switch(getAnswer()){
                case 1 -> houses.put("gryffindor", houses.get("gryffindor") + 1);
                case 2 -> houses.put("hufflepuff", houses.get("hufflepuff") + 1);
                case 3 -> houses.put("ravenclaw", houses.get("ravenclaw") + 1);
                case 4 -> houses.put("slytherin", houses.get("slytherin") + 1);
            }
        }

        for(Map.Entry<String,Integer> house : houses.entrySet()) {
            if(house.getValue() > maxPoints) {
                selectedHouse = house.getKey();
                maxPoints = house.getValue();
            }
        }

        System.out.println("\nPerteneces a " + selectedHouse.toUpperCase() + "!");
    }

    private static String questions(int number) {
        List<String> questions = new ArrayList<>(Arrays.asList(
                "¿Cómo te definirías?",
                "¿Cuál es tu clase favorita?",
                "¿Dónde pasarías más tiempo?",
                "¿Cuál es tu color favorito?",
                "¿Cuál es tu mascota?"
        ));

        List<String> gryffindorAnswers = new ArrayList<>(Arrays.asList(
                "1. Valiente",
                "1. Vuelo",
                "1. Explorando",
                "1. Rojo",
                "1. Lechuza"
        ));

        List<String> hufflepuffAnswers = new ArrayList<>(Arrays.asList(
                "2. Leal",
                "2. Animales fantásticos",
                "2. Invernadero",
                "2. Amarillo",
                "2. Gato"
        ));

        List<String> ravenclawAnswers = new ArrayList<>(Arrays.asList(
                "3. Sabio",
                "3. Pociones",
                "3. Biblioteca",
                "3. Azul",
                "3. Sapo"
        ));

        List<String> slytherinAnswers = new ArrayList<>(Arrays.asList(
                "4. Ambicioso",
                "4. Defensa contra las artes oscuras",
                "4. En la sala común",
                "4. Verde",
                "4. Serpiente"
        ));

        return String.format("%n%s%n%s%n%s%n%s%n%s",
                questions.get(number),
                gryffindorAnswers.get(number),
                hufflepuffAnswers.get(number),
                ravenclawAnswers.get(number),
                slytherinAnswers.get(number)
        );
    }

    private static int getAnswer() {
        int answer;
        Scanner sc = new Scanner(System.in);

        System.out.print("\nSeleccionar -> 1, 2, 3 o 4: ");
        answer = Integer.parseInt(sc.nextLine());

        if (answer > 0 && answer < 5) return answer;

        return getAnswer();
    }

}
