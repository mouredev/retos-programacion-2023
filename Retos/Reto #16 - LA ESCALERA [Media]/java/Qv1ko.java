public class Qv1ko {
    
    public static void main(String[] args) {
        stairs(3);
    }//main

    private static void stairs(int num) {
        String spaces="";
        if(num>0) {
            for(int i=0;i<num;i++) {
                spaces+="  ";
            }
            System.out.println(spaces+"_");
            for(int i=0;i<num;i++) {
                spaces=spaces.substring(0,spaces.length()-2);
                System.out.println(spaces+"_|");
            }
        } else if(num<0) {
            System.out.println(spaces+"_");
            for(int i=num;i<0;i++) {
                spaces+=(i==num)? " ":"  ";
                System.out.println(spaces+"|_");
            }
        } else {
            System.out.println("__");
        }
    }//stairs

}//class
