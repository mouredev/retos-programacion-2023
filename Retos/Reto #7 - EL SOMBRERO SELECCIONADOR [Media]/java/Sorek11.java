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

 public class Sorek11{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String opcion="";
        int griffindor = 0;
        int hufflepuff = 0;
        int ravenclaw = 0;
        int slytherin = 0;
        System.out.println("Bienvenid@ a Hogwarts! El sombrero seleccionador necesita hacerte unas preguntas para saber a qué casa perteneces.");
        System.out.println("1. ¿Qué rasgo te caracteriza más?");
        System.out.println("a. Valentía");
        System.out.println("b. Lealtad");
        System.out.println("c. Creatividad");
        System.out.println("d. Astucia");
        opcion = sc.nextLine();
        switch(opcion){
            case "a": griffindor++;
            break;
            case "b": hufflepuff++;
            break;
            case "c": ravenclaw++;
            break;
            case "d": slytherin++;
        }
        System.out.println("2. ¿Dónde te gustaría que estuviera tu casa común?");
        System.out.println("a. Mazmorras");
        System.out.println("b. Torre del colegio");
        System.out.println("c. En una sala amplia");
        System.out.println("d. Bodega");
        opcion = sc.nextLine();
        switch(opcion){
            case "a": slytherin++;
            break;
            case "b": griffindor++;
            break;
            case "c": ravenclaw++;
            break;
            case "d": hufflepuff++;
        }
        System.out.println("3. ¿Como actúas ante una injusticia?");
        System.out.println("a. Solo actúas si está involucrado algún amigo o familiar");
        System.out.println("b. Defiendes con valentía lo que crees justo sea quien sea");
        System.out.println("c. Defiendes la justicia pero no haces mucho ruido");
        System.out.println("d. Actúas solo si sacas un beneficio propio");
        opcion = sc.nextLine();
        switch(opcion){
            case "a": ravenclaw++;
            break;
            case "b": griffindor++;
            break;
            case "c": hufflepuff++;
            break;
            case "d": slytherin++;
        }
        System.out.println("4. ¿Qué eligirias de mascota?");
        System.out.println("a. Araña");
        System.out.println("b. Suricato");
        System.out.println("c. Lechuza");
        System.out.println("d. Gato");
        opcion = sc.nextLine();
        switch(opcion){
            case "a": slytherin++;
            break;
            case "b": hufflepuff++;
            break;
            case "c": ravenclaw++;
            break;
            case "d": griffindor++;
        }
        System.out.println("5. ¿Qué clase te interesa más?");
        System.out.println("a. Artes Oscuras");
        System.out.println("b. Adivinación");
        System.out.println("c. Herbolistería");
        System.out.println("d. Transformaciones");
        opcion = sc.nextLine();
        switch(opcion){
            case "a": slytherin++;
            break;
            case "b": ravenclaw++;
            break;
            case "c": hufflepuff++;
            break;
            case "d": griffindor++;
        }
        System.out.println("El sombrero seleccionador está pensando...");
        System.out.println(".");
        System.out.println(".");
        System.out.println(".");
        System.out.println(".");
        System.out.println(".");
        if(griffindor>hufflepuff && griffindor > slytherin && griffindor>ravenclaw){
            System.out.println("GRIFFINDOR!!!!!!!!");
        }
        if(hufflepuff>griffindor && hufflepuff>slytherin && hufflepuff > ravenclaw){
            System.out.println("HUFFLEPUFF!!!!!!!!");
        }
        if(ravenclaw>griffindor && ravenclaw>slytherin && ravenclaw > hufflepuff){
            System.out.println("RAVENCLAW!!!!!!!!");
        }
        if(slytherin>griffindor && slytherin>ravenclaw && slytherin > hufflepuff){
            System.out.println("SSSSSSLYTHERIN!!!!!!!!");
        }
        sc.close();
    }
 }
