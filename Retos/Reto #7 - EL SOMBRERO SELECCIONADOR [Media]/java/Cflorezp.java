package reto7SombreoSeleccionadorHarryPotter;

import java.util.*;
import java.util.stream.Collectors;

public class Cflorezp {

    public static void main(String[] args){

        //introduccion();

        List<Integer> preguntasSeleccionadas = genera6Preguntas();

        Scanner respuesta = new Scanner(System.in);
        List<String> puntos = new ArrayList<>();
        int count = 0;
        do{
            System.out.println(preguntas(preguntasSeleccionadas.get(count)));
            respuestas(preguntasSeleccionadas.get(count)).forEach(System.out::println);
            String opcion = respuesta.nextLine();
            switch (opcion){
                case "1":
                    puntos.add("Gryffindor");
                    break;
                case "2":
                    puntos.add("Hufflepuff");
                    break;
                case "3":
                    puntos.add("Ravenclaw");
                    break;
                case "4":
                    puntos.add("Slytherin");
                    break;
            }
            count++;
        }while(count < 6);

        List<String> preResultado = puntos.stream()
                .collect(Collectors.groupingBy(e -> e))
                .entrySet().stream()
                .filter(el -> el.getValue().size() > 1)
                .map(el -> el.getKey())
                .collect(Collectors.toList());

        if(preResultado.size() > 1) {
            System.out.println("!!! Vaya estoy indeciso podrias ser de " + preResultado.get(0)
                                + " o de " + preResultado.get(1) + " !!!");
            System.out.println("Te doy las siguientes opciones:\n 1. Escoges tu\n 2. Escojo yo ");
            String opcion = respuesta.nextLine();
            if(opcion.equals("1")){
                System.out.println("De acuerdo entonces dime a quien prefieres:\n 1- " + preResultado.get(0)
                        + "\n 2- " + preResultado.get(1));
                opcion = respuesta.nextLine();
                System.out.println("!!!Esta hecho serás de " + preResultado.get(Integer.parseInt(opcion)));
            }
            else{
                System.out.println("!!!Esta hecho serás de " + preResultado.get((int)(Math.random() * 2)));
            }
        }else{
            System.out.println("!!!Esta hecho serás de " + preResultado.get(0));
        }

    }

    public static void introduccion(){
        System.out.println("\uD834\uDD1E ♪♪♬♬♫♬♪♫♬♪♪♬♬♬♪♫♬♪♪♬♬♪♫♬♪♪♬♫♬♪♪♪♬♬♪♪♬♬♫♬♪♫♪♪♬♬" +
                "♪♫♬♪♪♬♬♫♬♪♬♪♪♬♫♫♬♪♬♪♫♬♪♬♪♫♬♪♪♬♪♬");
        System.out.println(cancion());
        System.out.println("\uD834\uDD1E ♪♫♬♪♫♬♪♪♬♬♪♪♬♬♫♬♪♬♪♬♪♬♪♫♬♪♪♬♪♬♪♪♬♪♪♬♪♫♬♪♪♬♬♪♫♪♬♪♫" +
                "♬♪♪♬♪♬♪♪♬♬♫♬♬♫♫♫♬♪♬♫♬♬♪♫♬♪♪♬♬\n");
        System.out.println("¡¡¡Bienvenido estudiante, responderemos unas preguntas para determinar"+
                " a que casa perteneceras!!!");
    }

    public static String cancion(){
        Map<Integer, String> canciones = new HashMap();
        canciones.put(1, "    Oh, podrás pensar que no soy bonito, pero no juzgues por lo que ves.\n" +
                "    Me comeré a mí mismo si puedes encontrar un sombrero más inteligente que yo.\n" +
                "    Puedes tener bombines negros, sombreros altos y elegantes.\n" +
                "    Pero yo soy el Sombrero Seleccionador de Hogwarts y puedo superar a todos.");
        canciones.put(2, "    Hace tal vez mil años que me cortaron, ahormaron y cosieron.\n" +
                "    Había entonces cuatro magos de fama de los que la memoria los nombres guarda:\n" +
                "    El valeroso Gryffindor venía del páramo; La bella Ravenclaw, de la cañada;\n" +
                "    del ancho valle procedía Hufflepuff la suave; y el astuto Slytherin, de los pantanos.");
        canciones.put(3, "    Cuando Hogwarts comenzaba su andadura y yo no tenía ni una sola arruga,\n" +
                "    los fundadores del colegio creían que jamás se separarían.\n" +
                "    Todos tenían el mismo objetivo, un solo deseo compartían:\n" +
                "    crear el mejor colegio mágico del mundo y transmitir su saber a sus alumnos.");
        int numero = (int)(Math.random() * canciones.size() + 1);
        return canciones.get(numero);
    }

    public static String preguntas(int opcion){
        Map<Integer, String> interogaciones = new HashMap<>();
        interogaciones.put(1, "PREGUNTA 1 ");
        interogaciones.put(2, "PREGUNTA 2 ");
        interogaciones.put(3, "PREGUNTA 3 ");
        interogaciones.put(4, "PREGUNTA 4 ");
        interogaciones.put(5, "PREGUNTA 5 ");
        interogaciones.put(6, "PREGUNTA 6 ");
        interogaciones.put(7, "PREGUNTA 7 ");
        interogaciones.put(8, "PREGUNTA 8 ");
        interogaciones.put(9, "PREGUNTA 9 ");
        interogaciones.put(10, "PREGUNTA 10 ");
        interogaciones.put(11, "PREGUNTA 11 ");
        interogaciones.put(12, "PREGUNTA 12 ");
        return interogaciones.get(opcion);
    }

    public static List<String> respuestas(int pregunta){
        List<String> opciones = new ArrayList<>();
        switch (pregunta){
            case 1:
                opciones.add("opcion 1 de 1");
                opciones.add("opcion 2 de 1");
                opciones.add("opcion 3 de 1");
                opciones.add("opcion 4 de 1");
                break;
            case 2:
                opciones.add("opcion 1 de 2");
                opciones.add("opcion 2 de 2");
                opciones.add("opcion 3 de 2");
                opciones.add("opcion 4 de 2");
                break;
            case 3:
                opciones.add("opcion 1 de 3");
                opciones.add("opcion 2 de 3");
                opciones.add("opcion 3 de 3");
                opciones.add("opcion 4 de 3");
                break;
            case 4:
                opciones.add("opcion 1 de 4");
                opciones.add("opcion 2 de 4");
                opciones.add("opcion 3 de 4");
                opciones.add("opcion 4 de 4");
                break;
            case 5:
                opciones.add("opcion 1 de 5");
                opciones.add("opcion 2 de 5");
                opciones.add("opcion 3 de 5");
                opciones.add("opcion 4 de 5");
                break;
            case 6:
                opciones.add("opcion 1 de 6");
                opciones.add("opcion 2 de 6");
                opciones.add("opcion 3 de 6");
                opciones.add("opcion 4 de 6");
                break;
            case 7:
                opciones.add("opcion 1 de 7");
                opciones.add("opcion 2 de 7");
                opciones.add("opcion 3 de 7");
                opciones.add("opcion 4 de 7");
                break;
            case 8:
                opciones.add("opcion 1 de 8");
                opciones.add("opcion 2 de 8");
                opciones.add("opcion 3 de 8");
                opciones.add("opcion 4 de 8");
                break;
            case 9:
                opciones.add("opcion 1 de 9");
                opciones.add("opcion 2 de 9");
                opciones.add("opcion 3 de 9");
                opciones.add("opcion 4 de 9");
                break;
            case 10:
                opciones.add("opcion 1 de 10");
                opciones.add("opcion 2 de 10");
                opciones.add("opcion 3 de 10");
                opciones.add("opcion 4 de 10");
                break;
            case 11:
                opciones.add("opcion 1 de 11");
                opciones.add("opcion 2 de 11");
                opciones.add("opcion 3 de 11");
                opciones.add("opcion 4 de 11");
                break;
            case 12:
                opciones.add("opcion 1 de 12");
                opciones.add("opcion 2 de 12");
                opciones.add("opcion 3 de 12");
                opciones.add("opcion 4 de 12");
                break;
        }
        return opciones;
    }

    public static List<Integer> genera6Preguntas(){
        Set<Integer> numerosPreguntas = new HashSet<>();
        do{
            int numero = (int)(Math.random() * 12 + 1);
            numerosPreguntas.add(numero);
        }while(numerosPreguntas.size() < 6);
        List<Integer> seisPreguntas = new ArrayList<>(numerosPreguntas);
        return seisPreguntas;
    }







}
