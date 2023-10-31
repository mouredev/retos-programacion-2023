public class patricioleono {

    public static void main(String[] args){
     int total = 100;
     for(int i = 0; i <= total; i++){
         if(i % 2 == 0){
             System.out.println("Fizz");
             if(i % 3 == 0){
                 System.out.println("FizzBuzz");
             }
         }else if(i % 3 == 0){
             System.out.println("Buzz");
         }else{
             System.out.println(i);
         }
     }
   }

}
