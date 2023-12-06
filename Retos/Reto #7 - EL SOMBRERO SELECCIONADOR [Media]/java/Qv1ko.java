import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Qv1ko {
    
    public static void main(String[] args) {
        sortingHat();
    }//main

    private static void sortingHat() {
        Map<String,Integer> houses=new HashMap<String, Integer>();
        houses.put("gryffindor", 0);
        houses.put("hufflepuff", 0);
        houses.put("ravenclaw", 0);
        houses.put("slytherin", 0);
        int maxPoints=0;
        String selectedHouse="";
        for(int i=0;i<5;i++) {
            System.out.println(questions(i));
            switch(getAnswer()){
                case 1 -> houses.put("slytherin",houses.get("slytherin")+1);
                case 2 -> houses.put("ravenclaw",houses.get("ravenclaw")+1);
                case 3 -> houses.put("hufflepuff",houses.get("hufflepuff")+1);
                case 4 -> houses.put("gryffindor",houses.get("gryffindor")+1);
            }
        }
        for(Map.Entry<String,Integer> house:houses.entrySet()) {
            if(house.getValue()>maxPoints) {
                selectedHouse=house.getKey();
                maxPoints=house.getValue();
            } else if(house.getValue()==maxPoints) {
                selectedHouse="muggle";
            }
        }
        System.out.println((selectedHouse.equalsIgnoreCase("muggle"))? "You are a "+selectedHouse:"Your house is "+selectedHouse.toUpperCase()+"!");
    }//sortingHat

    private static String questions(int number) {
        String[] questions={"How would you define your personality?","What is the biggest challenge you've faced?","What are your greatest achievements?","How would you behave in a difficult situation?","How would you solve a complex problem?"};
        String[] slytherinAnswers={"1. Ambitious, astute, perceptive and secretive","1. Leveraging my skills to achieve my ambitions without affecting others","1. Achieve my goals, use my cunning to get where I want to go and be a leader","1. I would behave shrewdly, trying to find the best way to emerge victorious from the situation","1. I would use deception and cunning to find an effective solution"};
        String[] ravenclawAnswers={"2. Intelligent, curious, wise and creative","2. Find ways to solve complex problems","2. Learning new things, using my intelligence to solve problems, and developing my skills","2. I would behave intelligently, seeking to understand the situation from all angles","2. I would use my intelligence and knowledge to find a solution"};
        String[] hufflepuffAnswers={"3. Patient, kind, loyal and hardworking","3. Work hard to achieve my goals without losing kindness","3. Being true to my principles, working hard and helping others","3. I would behave with kindness, trying to find solutions that are equitable for everyone","3. I would work hard to find a creative solution"};
        String[] gryffindorAnswers={"4. Determined, brave, direct and loyal","4. Overcoming my fears in order to face difficult situations","4. Achieving great things for others, overcoming my fears, and making difficult decisions","4. I would behave courageously, speaking out and fighting for what I believe is right","4. I would face the problem with courage and determination"};
        return "\n"+questions[number]+"\n\s"+slytherinAnswers[number]+"\n\s"+ravenclawAnswers[number]+"\n\s"+hufflepuffAnswers[number]+"\n\s"+gryffindorAnswers[number];
    }//questions

    private static int getAnswer() {
        String answer="";
        Scanner sc=new Scanner(System.in);
        System.out.print("Seleccione 1, 2, 3 o 4: ");
        answer=sc.nextLine();
        if(answer.equals("1")||answer.equals("2")||answer.equals("3")||answer.equals("4")) {
            return Integer.parseInt(answer);
        }
        return getAnswer();
    }//getAnswer

}//class