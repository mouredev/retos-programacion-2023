/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package matriz;


import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import javax.swing.JOptionPane;

/**
 *
 * @author Nameless-react
 */
public class CreateQuestions {
    public String question;
    public String[][] answer;

    public CreateQuestions() {}
    
    public CreateQuestions(String question, String[][] answer) {
        this.question = question;
        this.answer = answer;
    }
   
    public void selectionHouse() {
        JOptionPane.showMessageDialog(null, "Bienvenido(a) yo soy el sombrero seleccionador, a continuación voy a hacer unas preguntas para saber a que casa perteneces");

        CreateQuestions[] hatQuestions = {new CreateQuestions("¿Cómo te definirías?", new String[][] {
                                {"1. Valiente", "gryffindor"},
                                {"2. Leal", "hufflepuff"},
                                {"3. Sabio", "ravenclaw"},
                                {"4. Ambicioso", "slytherin"}}),
                     new CreateQuestions("¿Cuál es tu clase favorita?", new String[][]{
                                {"1. Vuelo", "gryffindor"},
                                {"2. Pociones", "ravenclaw"},
                                {"3. Defensa contra las artes oscuras", "slytherin"},
                                {"4. Animales fantásticos", "hufflepuff"}}),
                     new CreateQuestions("¿Dónde pasarías más tiempo?", new String[][]{
                                {"1. Invernadero", "hufflepuff"},
                                {"2. Biblioteca", "ravenclaw"},
                                {"3. En la sala común", "slytherin"},
                                {"4. Explorando", "gryffindor"}}),
                     new CreateQuestions("¿Cuál es tu color favorito?", new String[][]{
                                {"1. Rojo", "gryffindor"},
                                {"2. Azul", "ravenclaw"},
                                {"3. Verde", "slytherin"},
                                {"4. Amarillo", "hufflepuff"}}),
                     new CreateQuestions("¿Cuál es tu mascota?", new String [][]{
                                {"1. Sapo", "ravenclaw"},
                                {"2. Lechuza", "gryffindor"},
                                {"3. Gato", "hufflepuff"},
                                {"4. Serpiente", "slytherin"}})
          };
        Map<String, Integer> houses = new HashMap<>() {{
            put("gryffindor", 0);
            put("hufflepuff", 0);
            put("ravenclaw", 0);
            put("slytherin", 0);
        }};



        for (CreateQuestions createQuestion : hatQuestions) {
            int selection = 0;

            do {
                String text = String.join("\n", Arrays.asList(createQuestion.answer).stream().map(option -> option[0]).collect(Collectors.toList()));
                
                selection = Integer.parseInt(JOptionPane.showInputDialog(null, createQuestion.question + "\n" + text));
            } while (selection > 4 || selection <= 0);
            
            
            for (int i = 0; i < createQuestion.answer.length; i++) {
                String houseKey = createQuestion.answer[selection - 1][1];
                int houseValue = houses.get(houseKey);
                

                if ((i + 1) == selection) houses.replace(houseKey, houseValue + 1);
            }
        }         
        
        
        
        
        System.out.println("Hmmmmm....");
        System.out.println("Creo...");
        System.out.println("Que podrias encajar en....");
        Integer houseMaxScore = Collections.max(houses.values());
        String house = "";
        
        
        for (String key : houses.keySet()) {
            if (houses.get(key).equals(houseMaxScore)) {
                house = " " + key + " ";
                break;
            }
        }
        
        System.out.println("\n" + "#".repeat(20) + house + "#".repeat(20));
   
    }
}
