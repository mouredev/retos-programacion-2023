package reto7SombreoSeleccionadorHarryPotter;

import java.util.*;
import java.util.stream.Collectors;

public class Cflorezp {

    public static void main(String[] args){

        introduccion();

        List<Integer> preguntasSeleccionadas = genera6Preguntas();

        Scanner respuesta = new Scanner(System.in);
        List<String> puntos = new ArrayList<>();
        int count = 0;
        do{
            System.out.println(preguntas(preguntasSeleccionadas.get(count)));
            respuestas(preguntasSeleccionadas.get(count)).forEach(System.out::println);
            String opcion = respuesta.nextLine();
            String[] casas = {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"};
            switch (opcion){
                case "1":
                    puntos.add(casas[0]);
                    break;
                case "2":
                    puntos.add(casas[1]);
                    break;
                case "3":
                    puntos.add(casas[2]);
                    break;
                case "4":
                    puntos.add(casas[3]);
                    break;
                default:
                    System.out.println("No escogiste una opcion valida asi que  yo asignare la respuesta por ti.\n");
                    puntos.add(casas[(int)(Math.random() * 4)]) ;
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
                                + " o de " + preResultado.get(1) + " !!!\n");
            System.out.println("Te doy las siguientes opciones:\n 1. Escoges tu\n 2. Escojo yo ");
            String opcion = respuesta.nextLine();
            switch (opcion){
                case "1":
                    System.out.println("De acuerdo entonces dime a quien prefieres:\n 1- " + preResultado.get(0)
                            + "\n 2- " + preResultado.get(1));
                    opcion = respuesta.nextLine();
                    System.out.println("!!!Esta hecho serás de " + preResultado.get(Integer.parseInt(opcion)-1));
                    break;
                case "2":
                    System.out.println("!!!Esta hecho serás de " + preResultado.get((int)(Math.random() * 2)));
                    break;
                default:
                    System.out.println("No escogiste una opcion valida asi que escogere yo.\n");
                    System.out.println("!!!Esta hecho serás de " + preResultado.get((int)(Math.random() * 2)) + "!!!");
            }
        }else{
            System.out.println("!!!Esta hecho serás de " + preResultado.get(0) + "!!!");
        }
    }

    public static void introduccion(){
        System.out.println("\uD834\uDD1E ♪♪♬♬♫♬♪♫♬♪♪♬♬♬♪♫♬♪♪♬♬♪♫♬♪♪♬♫♬♪♪♪♬♬♪♪♬♬♫♬♪♫♪♪♬♬" +
                "♪♫♬♪♪♬♬♫♬♪♬♪♪♬♫♫♬♪♬♪♫♬♪♬♪♫♬♪♪♬♪♬");
        System.out.println(cancion());
        System.out.println("\uD834\uDD1E ♪♫♬♪♫♬♪♪♬♬♪♪♬♬♫♬♪♬♪♬♪♬♪♫♬♪♪♬♪♬♪♪♬♪♪♬♪♫♬♪♪♬♬♪♫♪♬♪♫" +
                "♬♪♪♬♪♬♪♪♬♬♫♬♬♫♫♫♬♪♬♫♬♬♪♫♬♪♪♬♬\n");
        System.out.println("¡¡¡Bienvenido estudiante, responderas unas preguntas para determinar"+
                " a que casa perteneceras!!!\n");
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
        interogaciones.put(1, "¿Si te encuentras en un bosque solo que harias? ");
        interogaciones.put(2, "¿Que preferirias ser en este colegio?");
        interogaciones.put(3, "¿Cual es la situacion mas aterradora para ti?");
        interogaciones.put(4, "¿En qué situaciones estarías dispuesto a mentir?");
        interogaciones.put(5, "¿Que extrañaras mas estando en Hogwarts?");
        interogaciones.put(6, "¿En una batalla como te sentirias mejor?");
        interogaciones.put(7, "¿Que actividad prefiririas?");
        interogaciones.put(8, "¿A quien te gustaria desafiar a un duelo?");
        interogaciones.put(9, "¿Cual seria tu materia preferida en Hogwarts?");
        interogaciones.put(10, "¿Si te enteras que un profesor es un mago maligno que harias?");
        interogaciones.put(11, "¿Cual de las siguientes acciones es la mas correcta para ti?");
        interogaciones.put(12, "¿Que te hace mas feliz?");
        return interogaciones.get(opcion);
    }

    public static List<String> respuestas(int pregunta){
        List<String> opciones = new ArrayList<>();
        switch (pregunta){
            case 1:
                opciones.add("1- Empezaria a recorrerlo para encontrar monstruos y luchar con ellos");
                opciones.add("2- Armaria un campamento y estaria pacientemente alli");
                opciones.add("3- Trataria de averiguar porque estoy alli y cual es mi mision");
                opciones.add("4- Utilizaria todos mis encantos para ser el dueño del bosque");
                break;
            case 2:
                opciones.add("1- Profesor");
                opciones.add("2- Fantasma");
                opciones.add("3- Guardian");
                opciones.add("4- Director");
                break;
            case 3:
                opciones.add("1- Quedarme sin mi varita");
                opciones.add("2- Ser el unico mago sin poderes");
                opciones.add("3- No poder derrotar a un enemigo");
                opciones.add("4- No tener amigos");
                break;
            case 4:
                opciones.add("1- Para ayudar a mis compañeros");
                opciones.add("2- Para evitar una injusticia");
                opciones.add("3- Para vencer a un contrincante");
                opciones.add("4- Para ser el unco lider");
                break;
            case 5:
                opciones.add("1- A mis padres y toda mi familia");
                opciones.add("2- A mis amigos");
                opciones.add("3- Nada");
                opciones.add("4- A mis mascotas");
                break;
            case 6:
                opciones.add("1- Luchando hasta ganar la batalla");
                opciones.add("2- Ayudando a todos mis compañeros a ganar la batalla");
                opciones.add("3- Ideando un plan para ganar la batalla");
                opciones.add("4- Reclutando a mas compañeros para ganar la batalla");
                break;
            case 7:
                opciones.add("1- Nadar en un lago desconocido");
                opciones.add("2- Pescar en un rio");
                opciones.add("3- Acampar en un bosque antiguo");
                opciones.add("4- Salir a cazar animales");
                break;
            case 8:
                opciones.add("1- Al mago mas maligno y peligroso");
                opciones.add("2- Al mago mas poderoso");
                opciones.add("3- A cualquiera que quiera retarme");
                opciones.add("4- Al mago mas debil de Hogwarts");
                break;
            case 9:
                opciones.add("1- Encantamientos y posiciones");
                opciones.add("2- Cuidado de criaturas magicas");
                opciones.add("3 -Historia de la magia");
                opciones.add("4- Transfiguracion");
                break;
            case 10:
                opciones.add("1- Lo confrontaria y retaria");
                opciones.add("2- Lo investigaria para saber quien es en realidad");
                opciones.add("3- Le contaria a mis amigos para que me ayuden a enfrentarlo");
                opciones.add("4- Me uniria a el para aprender mas trucos de magia");
                break;
            case 11:
                opciones.add("1- Decir la verdad siempre aunque esto traiga castigos");
                opciones.add("2- Confiar en las personas");
                opciones.add("3- Entender a las personas sin importar su origen");
                opciones.add("4- Guardar muchos secretos sin importar de quien sean");
                break;
            case 12:
                opciones.add("1- Salir y conocer lugares inexplorados");
                opciones.add("2- Compartir todas mis cosas con mis amigos");
                opciones.add("3- Ganar siempre");
                opciones.add("4- Estudiar mucho para ser el mejor mago");
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
