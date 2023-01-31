package com.ejercicios;

import org.json.JSONObject;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


@SpringBootApplication
public class EjerciciosApplication {

    public static void main(String[] args) throws IOException {
        SpringApplication.run(EjerciciosApplication.class, args);
        LenguajeHacker();
    }

    public static void LenguajeHacker() throws IOException {
        BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese el texto:  ");
        String letra = scanner.readLine();

        JSONObject leet = new JSONObject();
        leet.put("a", 4);
        leet.put("b","I3");
        leet.put("c","[");
        leet.put("d",")");
        leet.put("e",3);
        leet.put("f","|=");
        leet.put("g","&");
        leet.put("h","#");
        leet.put("i",1);
        leet.put("j",",_|");
        leet.put("k",">|");
        leet.put("l",1);
        leet.put( "m","/\\/\\");
        leet.put( "n","^/");
        leet.put( "o",0);
        leet.put( "p","|*");
        leet.put( "q","(_,)");
        leet.put( "r","I2");
        leet.put( "s",5);
        leet.put( "t",7);
        leet.put( "u","(_)");
        leet.put(  "v","\\/");
        leet.put(  "w","\\/\\/");
        leet.put(  "x","><");
        leet.put(  "y","j");
        leet.put(  "z",2);
        leet.put(  " "," ");


        Object[] key = leet.keySet().toArray();
        StringBuilder tipografiaLeet = new StringBuilder();


        for (int j = 0; j < letra.length(); j++) {
            String letraString = String.valueOf(letra.charAt(j));
            char letraSpecial =  letra.charAt(j);

            for (int i = 0; i < leet.length(); i++) {
                String keyString = (String) key[i];
                if (keyString.equals(letraString.toLowerCase())){
                    tipografiaLeet.append(leet.get(key[i].toString()));
                    break;
                }else if (!Character.isLetterOrDigit(letraSpecial)) {
                    tipografiaLeet.append(letraSpecial);
                    break;
                }
            }
        }
        System.out.println(tipografiaLeet);
    }
}
