public class Alvarogtz {
    private static  void main(String[] args){
        for(int i = 1; i< 101; i++){
            if(i%3 == 0){
                System.out.println("flizz");
            }else if(i%5 == 0){
                System.out.println("buzz");
            }else {
                System.out.println(i);
            }
        }
    }
}
