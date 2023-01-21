package reto3;

/*
 * Reto #3: EL GENERADOR DE CONTRASEÑAS
 * Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23
 *
 * Enunciado
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 * https://elcodigoascii.com.ar/ Para mirar los códigos ASCI de las letras
 */


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

import static reto3.jitos_dev.Options.*;
import static reto3.jitos_dev.Symbol.*;

public class jitos_dev {

    public static void main(String[] args) {
        String password1 = generatePassword(2, 4, CAN_UPPERCASE, CAN_NUMBERS, CAN_SYMBOLS);
        String password2 = generatePassword(2, 3, CAN_UPPERCASE, CAN_NUMBERS);
        String password3 = generatePassword(8, 16, CAN_NUMBERS, CAN_SYMBOLS);
        String password4 = generatePassword(8, 16);
        String password5 = generatePassword(8, 16, CAN_UPPERCASE);
        System.out.println(password1);
        System.out.println(password2);
        System.out.println(password3);
        System.out.println(password4);
        System.out.println(password5);
    }

    public static String generatePassword(int minLength, int maxLength, Options... options) {
        //Si el mínimo es menor que el máximo o el máximo o el mínimo es menor o igual a 0 devolvemos 0
        if (maxLength < minLength || maxLength <= 0 || minLength <= 0)
            return "0";

        //Lista para todos los códigos ASCI que vamos a utilizar. Incluimos minúsculas directamente
        List<Integer> ASCI_CODES = new ArrayList<>(getLettersLowerCase());

        //Lista con las opciones que nos pasan y que podemos tener para incluir en la contraseña
        List<Options> optionsList = List.of(options);

        if (optionsList.contains(CAN_UPPERCASE))
            ASCI_CODES.addAll(getLettersUpperCase());

        if (optionsList.contains(CAN_NUMBERS))
            ASCI_CODES.addAll(getNumbers());

        if (optionsList.contains(CAN_SYMBOLS))
            ASCI_CODES.addAll(getASCISymbol());

        //Calculamos el tamaño aleatorio de la contraseña en función de los valores que nos pasan
        int lengthPassword = getRandom(minLength, maxLength);

        StringBuilder password = new StringBuilder();
        //Recorremos el bucle tantas veces como la longitud de la contraseña y le asignamos un valor aleatorio cada vez
        for (int i = 0; i < lengthPassword; i++) {
            int valueRandom = getRandom(0, ASCI_CODES.size() - 1);
            int code = ASCI_CODES.get(valueRandom);
            password.append((char) code);
        }

        return password.toString();
    }

    /*Lista con los códigos ASCI de las letras minúsculas. Las minúsculas empiezan en el 65 hasta el 97 incluido*/
    private static List<Integer> getLettersLowerCase() {
        List<Integer> ASCI_List = new ArrayList<>();

        for (int i = 97; i <= 122; i++) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /*Lista con los códigos ASCI de las letras mayúsculas. Las mayúsculas empiezan en el 65 hasta el 97 incluido*/
    private static List<Integer> getLettersUpperCase() {
        List<Integer> ASCI_List = new ArrayList<>();

        for (int i = 65; i <= 90; i++) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /*Lista con los códigos ASCI de los números. Los números empiezan en el 48 hasta el 57 incluido*/
    private static List<Integer> getNumbers() {
        List<Integer> ASCI_List = new ArrayList<>();

        for (int i = 48; i <= 57; i++) {
            ASCI_List.add(i);
        }

        return ASCI_List;
    }

    /* Lista con los códigos ASCI de los símbolos que vamos a poder utilizar. Si añadimos uno nuevo
     * solo lo tenemos que añadir al método getSymbols y este los añade todos*/
    private static List<Integer> getASCISymbol() {
        List<Integer> ASCI_List = new ArrayList<>();
        Symbol[] symbols = getSymbols();

        Arrays.stream(symbols).forEach(symbol -> {
            ASCI_List.add(symbol.ASCI);
        });

        return ASCI_List;
    }

    /*Array con los símbolos que podemos utilizar*/
    private static Symbol[] getSymbols() {
        return new Symbol[]{EXCLAMACION, ALMOHADILLA, DOLLAR, PORCENTAJE, AMPERSAND, ASTERISCO, SUMA, INTERROGACION};
    }

    /*Nos devuelve un entero positivo entre dos valores dados con los propios valores incluidos*/
    private static int getRandom(int start, int end) {
        return ThreadLocalRandom.current().nextInt(start, end + 1);
    }

    /*El número del símbolo corresponde con su código ASCI*/
    public enum Symbol {
        EXCLAMACION(33), ALMOHADILLA(35), DOLLAR(36), PORCENTAJE(37), AMPERSAND(38),
        ASTERISCO(42), SUMA(43), INTERROGACION(63);

        private final int ASCI;
        Symbol(int ASCI) {
            this.ASCI = ASCI;
        }
    }

    public enum Options {
        CAN_UPPERCASE, CAN_NUMBERS, CAN_SYMBOLS;
    }

}
