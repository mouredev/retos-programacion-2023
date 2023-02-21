import java.util.*;

public class Alvarogtz {

    private static Scanner sc = new Scanner(System.in);
    private enum house {GRYFFINDOR,HUFFLEPUFF,RAVENCLAW,SLYTHERIN};
    private static int gryffindor,hufflepuff,slytherin,ravenclaw = 0;

    private static final Map<house, List> casasHowarts = new HashMap<>(){{
        put(house.GRYFFINDOR, Arrays.asList("Rojo","El poder de la invisibilidad","Sabiduria","Volar en una escoba","Duendes","Espada"));
        put(house.SLYTHERIN, Arrays.asList("Verde","El poder de la fuerza sobrehumana","Poder","Maleficios y hechizos","Trolls","Guardapelo"));
        put(house.HUFFLEPUFF, Arrays.asList("Amarillo","El poder de leer la mente","Amor","Transfiguracion (convertir un objeto en otro objeto)","Centauros","Copa"));
        put(house.RAVENCLAW, Arrays.asList("Azul","El poder de cambiar el pasado","Gloria","Secretos sobre el castillo","Hombres lobo","Diadema"));
    }};

    private static final Map<String, List> questions = new HashMap<>(){{
        put("¿Color favorito?", Arrays.asList("Rojo","Verde","Amarillo","Azul"));
        put("¿Qué poder preferirías tener?", Arrays.asList("El poder de la fuerza sobrehumana", "El poder de la invisibilidad","El poder de cambiar el pasado","El poder de leer la mente"));
        put("¿Qué ansías encontrar en Howarts?", Arrays.asList("Amor","Sabiduria","Poder","Gloria"));
        put("¿Qué es lo que más deseas aprender en Hogwarts?", Arrays.asList("Secretos sobre el castillo","Transfiguracion (convertir un objeto en otro objeto)","Maleficios y hechizos","Volar en una escoba"));
        put("¿Cuál de los siguientes criaturas mágicas te gusta más?", Arrays.asList("Duendes","Trolls","Hombres lobo","Centauros"));
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
                    if(response == 0 || response > options)
                        System.out.println("Opcion incorrecta\n");
                }catch(Exception e){System.out.println("Opcion incorrecta\n");}

            }while(response == 0 || response > options);

            sumaPuntos(valor.get(response -1).toString());
        }
    }

    public static void sumaPuntos(String respuesta){
        house casa = null;
        for(house clave : casasHowarts.keySet()){
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
            case GRYFFINDOR:
                gryffindor++;
                break;
            case SLYTHERIN:
                slytherin++;
                break;
            case RAVENCLAW:
                ravenclaw++;
                break;
            case HUFFLEPUFF:
                hufflepuff++;
                break;
            default:
                break;
        }
    }

    public static void dameGanador (){
        List<house> casasGanadoras = new ArrayList<>();
        for(int i = 3; i >= 2; i--){ // Con 3 puntos ya tengo el ganador
            if(gryffindor == i ) {
                casasGanadoras.add(house.GRYFFINDOR);
                if(i == 3)
                    break;
            }
            if(slytherin == i ) {
                casasGanadoras.add(house.SLYTHERIN);
                if(i == 3)
                    break;
            }
            if(hufflepuff == i) {
                casasGanadoras.add(house.HUFFLEPUFF);
                if(i == 3)
                    break;
            }
            if(ravenclaw == i) {
                casasGanadoras.add(house.RAVENCLAW);
                if(i == 3)
                    break;
            }
        }

        if(casasGanadoras.size() == 1) {
            System.out.println("El sombrero seleccionador te envia a ... ");
            try {
                Thread.sleep(2000);
                System.out.println(casasGanadoras.get(0) + " !!!");
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }else { // Empate
            List result = new ArrayList();
            System.out.println("El sombrero seleccionador no lo tiene claro ... Necesita una ultima respuesta\n");
            for(house ganador : casasGanadoras) {
                result.add(casasHowarts.get(ganador).get(casasHowarts.get(ganador).size()-1).toString());
            }
            Map<String,List> questionDeuce = new HashMap<>(){{
                put("¿Qué objeto te llama más la atención?", result);
            }};
            printMenu(questionDeuce,result.size());
            dameGanador();
        }
    }
}
