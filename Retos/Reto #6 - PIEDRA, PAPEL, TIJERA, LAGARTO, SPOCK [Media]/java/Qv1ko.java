public class Qv1ko {

    public static void main(String[] args) {
        game(new String[]{"🗿","✂️","✂️","🗿","📄","✂️"});
    }//main

    private static void game(String[] combinations) {
        int p1=0,p2=0;
        if(combinations.length%2==0) {
            for(int i=0;i<combinations.length-1;i+=2) {
                if(combinations[i].equals(combinations[i+1])) {
                    continue;
                }
                if(combinations[i].equals("🗿")) {
                    p1+=(combinations[i+1].equals("✂️")||combinations[i+1].equals("🦎"))? 1:0;
                    p2+=(combinations[i+1].equals("📄")||combinations[i+1].equals("🖖"))? 1:0;
                }
                if(combinations[i].equals("📄")) {
                    p1+=(combinations[i+1].equals("🗿")||combinations[i+1].equals("🖖"))? 1:0;
                    p2+=(combinations[i+1].equals("✂️")||combinations[i+1].equals("🦎"))? 1:0;
                }
                if(combinations[i].equals("✂️")) {
                    p1+=(combinations[i+1].equals("📄")||combinations[i+1].equals("🦎"))? 1:0;
                    p2+=(combinations[i+1].equals("🗿")||combinations[i+1].equals("🖖"))? 1:0;
                }
                if(combinations[i].equals("🦎")) {
                    p1+=(combinations[i+1].equals("📄")||combinations[i+1].equals("🖖"))? 1:0;
                    p2+=(combinations[i+1].equals("🗿")||combinations[i+1].equals("✂️"))? 1:0;
                }
                if(combinations[i].equals("🖖")) {
                    p1+=(combinations[i+1].equals("🗿")||combinations[i+1].equals("✂️"))? 1:0;
                    p2+=(combinations[i+1].equals("📄")||combinations[i+1].equals("🦎"))? 1:0;
                }
            }
            System.out.println((p1==p2)? "Tie":(p1>p2)? "Player 1":"Player 2");
        } else {
            System.out.println("Invalid input");
        }
    }//game

}//class