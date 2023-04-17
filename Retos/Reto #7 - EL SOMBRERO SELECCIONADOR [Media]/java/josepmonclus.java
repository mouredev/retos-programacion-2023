import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    private int gryffindor = 0;
    private int ravenclaw = 0;
    private int hufflepuff = 0;
    private int slytherin = 0;

    public static void main(String[] args) {
        
        josepmonclus josepmonclus = new josepmonclus();

        josepmonclus.doCuestionario();

        josepmonclus.printCasaAsignada();

    }

    private void doCuestionario() {

        System.out.println("Bienvenido al cuestionario del Sombrero Seleccionador!");
        System.out.println("Deberás ir respondiendo a las preguntas para poder asignarte a una casa de Hogwarts.");

        List<String[]> cuestionario = getCuestionario(5);

        for(String[] pregunta : cuestionario) {
            
            System.out.println("");
            System.out.println(pregunta[0]);
            System.out.println(pregunta[1]);
            System.out.println(pregunta[2]);
            System.out.println(pregunta[3]);
            System.out.println(pregunta[4]);

            boolean respuestaCorrecta = false;
            while(!respuestaCorrecta){
                System.out.println("Indica tu respuesta [1, 2, 3 o 4]");

                String line = entrada.nextLine();

                if(!line.equals("1") && 
                        !line.equals("2") && 
                        !line.equals("3") && 
                        !line.equals("4")) {
                    System.out.println("Respuesta no válida");
                } else {
                    switch (line) {
                        case "1":
                            gryffindor++;
                            break;
                        case "2":
                            ravenclaw++;
                            break;
                        case "3":
                            hufflepuff++;
                            break;
                        case "4":
                            slytherin++;
                            break;
                        default:
                            break;
                    }

                    respuestaCorrecta = true;
                }
            }
        }
    }

    private void printCasaAsignada() {
        System.out.println("---------------------------------");

        if(gryffindor >= hufflepuff && gryffindor >= ravenclaw && gryffindor >= slytherin) {
            System.out.println("Tu casa será..... GRYFFINDOR!!");
        } else if(hufflepuff >= ravenclaw && hufflepuff >= slytherin) {
            System.out.println("Tu casa será..... HUFFLEPUFF!!");
        } else if(ravenclaw >= slytherin) {
            System.out.println("Tu casa será..... RAVENCLAW!!");
        } else {
            System.out.println("Tu casa será..... SLYTHERIN!!");
        }

        System.out.println("---------------------------------");
    }

    private List<String[]> getCuestionario(int size) {
        List<String[]> preguntasRespuestas = new ArrayList<>();
        preguntasRespuestas.add(
            new String[]{"¿Qué criatura mágica te gustaría tener como mascota?",
                "1. Búho", 
                "2. Gato", 
                "3. Rata", 
                "4. Lechuza"});
        preguntasRespuestas.add(
                new String[]{"¿Qué color te atrae más?",
                "1. Rojo", 
                "2. Azul", 
                "3. Amarillo", 
                "4. Verde"});
        preguntasRespuestas.add(
                new String[]{"¿Qué cualidad valoras más en ti mismo?",
                "1. Coraje", 
                "2. Inteligencia", 
                "3. Lealtad", 
                "4. Astucia"});
        preguntasRespuestas.add(
                new String[]{"¿Cuál es tu hechizo favorito?",
                "1. Expecto Patronum", 
                "2. Wingardium Leviosa", 
                "3. Expelliarmus", 
                "4. Lumos"});
        preguntasRespuestas.add(
                new String[]{"¿Qué harías si te enfrentas a un troll?",
                "1. Huir", 
                "2. Atacar", 
                "3. Pedir ayuda",
                "4. Intentar razonar con él"});
        preguntasRespuestas.add(
                new String[]{"¿Cuál es tu asignatura favorita en Hogwarts?",
                "1. Pociones", 
                "2. Transformaciones", 
                "3. Herbología", 
                "4. Defensa contra las Artes Oscuras"});
        preguntasRespuestas.add(
                new String[]{"¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
                "1. La Sala Común de mi casa", 
                "2. El Gran Comedor", 
                "3. La Biblioteca",
                "4. Los terrenos del castillo"});

        Collections.shuffle(preguntasRespuestas);
        return preguntasRespuestas.subList(0, size);
    }
}
