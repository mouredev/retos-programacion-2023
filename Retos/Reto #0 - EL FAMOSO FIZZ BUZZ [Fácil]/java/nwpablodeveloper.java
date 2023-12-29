public class nwpablodeveloper {
    public static void main(String[] args) {
          
        for(int i = 1; i <=100; i++){
            String palabra = (i % 3 == 0 && i % 5 == 0) ? "fizzbuzz" 
                            :(i % 5 == 0 ) ? "buzz"
                            :(i % 3 == 0 ) ? "buzz" : String.valueOf(i);
            System.out.println(i + "\t" + palabra);
        }
        
    }

}
