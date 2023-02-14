package reto7SombreoSeleccionadorHarryPotter;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Cflorezp {

    public static void main(String[] args){

        introduccion();
        System.out.println(gryffindor());


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

    public static int gryffindor(){
        Map<Integer, String> preguntasGryffindor = new HashMap<>();
        preguntasGryffindor.put(1, "¿Enfrentarias a un enemigo solo? Si/No: ");
        preguntasGryffindor.put(2, "¿Enfrentarias a un enemigo solo? S/N: ");
        preguntasGryffindor.put(3, "¿Enfrentarias a un enemigo solo? s/n: ");
        preguntasGryffindor.put(4, "¿Enfrentarias a un enemigo solo? si:/no: ");
        int count = 0;
        int gryffindor = 0;

        Scanner opcion = new Scanner(System.in);
        do{
            int numero = (int)(Math.random() * preguntasGryffindor.size() + 1);
            System.out.print(preguntasGryffindor.get(numero));
            String respuesta = opcion.nextLine();
            if(respuesta.toUpperCase().equals("S") || respuesta.toUpperCase().equals("SI")){
                gryffindor++;
            }
            count++;
        }while(count < 2);
        return  gryffindor;
    }





}
