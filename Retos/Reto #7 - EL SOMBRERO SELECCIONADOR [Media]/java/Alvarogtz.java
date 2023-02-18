import java.util.*;

public class Alvarogtz {

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

    private static int gryffindor,hufflepuff,slytherin,ravenclaw = 0;
    private static Scanner sc = new Scanner(System.in);
    private final static String HOUSE_GRYFFINDOR = "GRYFFINDOR";
    private final static String HOUSE_HUFFLEPUFF = "HUFFLEPUFF";
    private final static String HOUSE_SLYTHERIN = "SLYTHERIN";
    private final static String HOUSE_RAVENCLAW = "RAVENCLAW";

    private static final Map<String, List> casasHowarts = new HashMap<>(){{
        put(HOUSE_GRYFFINDOR, Arrays.asList("Rojo","El poder de la invisibilidad","Sabiduria","Volar en una escoba","Duendes","Espada"));
        put(HOUSE_SLYTHERIN, Arrays.asList("Verde","El poder de la fuerza sobrehumana","Poder","Maleficios y hechizos","Trolls","Guardapelo"));
        put(HOUSE_HUFFLEPUFF, Arrays.asList("Amarillo","El poder de leer la mente","Amor","Transfiguracion (convertir un objeto en otro objeto)","Centauros","Copa"));
        put(HOUSE_RAVENCLAW, Arrays.asList("Azul","El poder de cambiar el pasado","Gloria","Secretos sobre el castillo","Hombres lobo","Diadema"));
    }};

    private static final Map<String, List> questions = new HashMap<>(){{
        put("¿Color favorito?", Arrays.asList("Rojo","Verde","Amarillo","Azul"));
        put("¿Qué poder preferirías tener?", Arrays.asList("El poder de la fuerza sobrehumana", "El poder de la invisibilidad","El poder de cambiar el pasado","El poder de leer la mente"));
        put("¿Qué ansías encontrar en Howarts?", Arrays.asList("Amor","Sabiduria","Poder","Gloria"));
        put("¿Qué es lo que más deseas aprender en Hogwarts?", Arrays.asList("Secretos sobre el castillo","Transfiguracion (convertir un objeto en otro objeto)","Maleficios y hechizos","Volar en una escoba"));
        put("¿Cuál de los siguientes criaturas mágicas te gusta más?", Arrays.asList("Duendes","Trolls","Hombres lobo","Centauros"));
    }};

    private static final Map<String, String> optionsDeuce = new HashMap<>(){{
        put(HOUSE_GRYFFINDOR, "Espada");
        put(HOUSE_SLYTHERIN, "Guardapelo");
        put(HOUSE_HUFFLEPUFF, "Copa");
        put(HOUSE_RAVENCLAW, "Diadema");
    }};

    public static void main(String[] args){
        printMenu(questions,4);
        dameGanador();
    }

    public static void printMenu(Map<String,List> housesQuestions,int options){
        int contador;
        int response = 0;
        for(String clave : housesQuestions.keySet()){
            System.out.println("\n" +clave);
            List valor = housesQuestions.get(clave);
            do {
                contador = 0;
                for(Object option : valor){
                    contador++;
                    System.out.println(contador + " - " + option.toString());
                }
                try {
                    response = Integer.parseInt(sc.nextLine());
                    if(response != 0 && response > options)
                        System.out.println("Opcion incorrecta\n");
                }catch(Exception e){System.out.println("Opcion incorrecta\n");}

            }while(response != 0 && response > options);

            sumaPuntos(valor.get(response -1).toString());
        }
    }

    public static void sumaPuntos(String respuesta){
        String casa = "";
        for(String clave : casasHowarts.keySet()){
            List valor = casasHowarts.get(clave);
            for(int i = 0; i<valor.size();i++){
                String value = valor.get(i).toString();
                if(value.equalsIgnoreCase(respuesta)) {
                    casa = clave;
                    break;
                }
            }
        }

        switch (casa){
            case HOUSE_GRYFFINDOR:
                gryffindor++;
                break;
            case HOUSE_SLYTHERIN:
                slytherin++;
                break;
            case HOUSE_RAVENCLAW:
                ravenclaw++;
                break;
            case HOUSE_HUFFLEPUFF:
                hufflepuff++;
                break;
            default:
                break;
        }
    }

    public static void dameGanador (){
        List<String> casasGanadoras = new ArrayList<>();
        for(int i = 3; i >= 2; i--){ // Con 3 puntos ya tengo el ganador
            if(gryffindor == i ) {
                casasGanadoras.add(HOUSE_GRYFFINDOR);
                if(i == 3)
                    break;
            }
            if(slytherin == i ) {
                casasGanadoras.add(HOUSE_SLYTHERIN);
                if(i == 3)
                    break;
            }
            if(hufflepuff == i) {
                casasGanadoras.add(HOUSE_HUFFLEPUFF);
                if(i == 3)
                    break;
            }
            if(ravenclaw == i) {
                casasGanadoras.add(HOUSE_RAVENCLAW);
                if(i == 3)
                    break;
            }
        }

        if(casasGanadoras.size() == 1) {
            System.out.println("El sombrero seleccionador te envia a ... " + casasGanadoras.get(0) + " !!!");
        }else { // Empate
            List result = new ArrayList();
            System.out.println("El sombrero seleccionador no lo tiene claro ... Necesita una ultima respuesta\n");
            for(String ganador : casasGanadoras) {
                result.add(optionsDeuce.get(ganador).toString());
            }
            Map<String,List> questionDeuce = new HashMap<>(){{
                put("¿Qué objeto te llama más la atención?", result);
            }};
            printMenu(questionDeuce,result.size());
            dameGanador();
        }
    }
}
