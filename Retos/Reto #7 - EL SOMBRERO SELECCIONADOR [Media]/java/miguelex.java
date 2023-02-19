import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;
import java.util.Map;

public class miguelex {

    public static void main(String[] args) {
        System.out.println("¡Felicidades! Según tus respuestas, perteneces a la casa de " + HogwartsHatSelector());
    }

    public static String HogwartsHatSelector() {
        System.out.println("Bienvenido al Test de Clasificación de Casas de Hogwarts!");
        System.out.println("Responde las siguientes preguntas para saber a qué casa pertenecerías:");

        String[] preguntas = {
                "1. ¿Qué cualidad valoras más en ti mismo?",
                "2. ¿Qué criatura mágica te gustaría tener como mascota?",
                "3. ¿Cuál es tu asignatura favorita en Hogwarts?",
                "4. ¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
                "5. ¿Cuál es tu hechizo favorito?",
                "6. ¿Qué objeto mágico te gustaría poseer?",
                "7. ¿Cuál es tu personaje favorito de Harry Potter?",
                "8. ¿Qué harías si te enfrentas a un troll?",
                "9. ¿Qué tipo de clima prefieres?",
                "10. ¿Cuál es tu forma preferida de transporte mágico?",
                "11. ¿Qué color te atrae más?",
                "12. ¿Qué criatura mágica te da más miedo?",
                "13. ¿Cuál es tu golosina mágica favorita?",
                "14. ¿Cuál es tu asignatura menos favorita en Hogwarts?",
                "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"
        };

        String[][] opciones = {
                { "a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia" },
                { "a. Búho", "b. Gato", "c. Rata", "d. Lechuza" },
                { "a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras" },
                { "a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca",
                        "d. Los terrenos del castillo" },
                { "a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos" },
                { "a. La Capa de Invisibilidad", "b. La Varita de Saúco",
                        "c. El Giratiempo", "d. La Piedra Filosofal" },
                { "a. Harry Potter", "b. Hermione Granger",
                        "c. Ron Weasley", "d. Neville Longbottom" },
                { "a. Huir", "b. Atacar", "c. Pedir ayuda",
                        "d. Intentar razonar con él" },
                { "a. Sol", "b. Lluvia", "c. Nieve", "d. Viento" },
                { "a. Escoba voladora", "b. El Autobús Noctámbulo",
                        "c. El Tren Hogwarts Express", "d. Aparición" },
                { "a. Rojo", "b. Azul", "c. Amarillo", "d. Verde" },
                { "a. Dementor", "b. El Basilisco",
                        "c. El Hombre Lobo", "d. Las Arpías" },
                { "a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott",
                        "c. Pastel de Calabaza", "d. Caramelos de Menta" },
                { "a. Historia de la Magia", "b. Adivinación",
                        "c. Estudio de los Muggles", "d. Runas Antiguas" },
                { "a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca",
                        "d. Pasar tiempo con amigos" }
        };

        Random rand = new Random();
        int[] randomQuestions = rand.ints(0, preguntas.length).distinct().limit(4).toArray();

        Scanner scanner = new Scanner(System.in);

        String[] respuestas = new String[4];
        for (int i = 0; i < randomQuestions.length; i++) {
            int idx = randomQuestions[i];
            System.out.println(preguntas[idx]);
            for (String opcion : opciones[idx]) {
                System.out.println(opcion);
            }
            System.out.print("Elige una opción (a, b, c o d): ");
            respuestas[i] = scanner.nextLine();
        }

        Map<String, Integer> puntuaciones = new HashMap<String, Integer>();
        puntuaciones.put("Gryffindor", 0);
        puntuaciones.put("Ravenclaw", 0);
        puntuaciones.put("Hufflepuff", 0);
        puntuaciones.put("Slytherin", 0);

        for (String respuesta : respuestas) {
            switch (respuesta) {
                case "a":
                    puntuaciones.put("Gryffindor", puntuaciones.get("Gryffindor") + 1);
                    break;
                case "b":
                    puntuaciones.put("Ravenclaw", puntuaciones.get("Ravenclaw") + 1);
                    break;
                case "c":
                    puntuaciones.put("Hufflepuff", puntuaciones.get("Hufflepuff") + 1);
                    break;
                case "d":
                    puntuaciones.put("Slytherin", puntuaciones.get("Slytherin") + 1);
                    break;
            }
        }

        String casa = "";
        int maxPuntuacion = 0;
        for (Map.Entry<String, Integer> entry : puntuaciones.entrySet()) {
            if (entry.getValue() > maxPuntuacion) {
                casa = entry.getKey();
                maxPuntuacion = entry.getValue();
            }
        }
        return casa;
    }
}
