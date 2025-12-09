
public class Flashborne{

public static void main(String args[]){

    for(int i = 1; i <= 100; i++){
        switch((Object) i){
            case Integer n when n % 3 == 0 && n % 5 == 0 
            -> System.out.println("fizzbuzz");
            case Integer n when n % 3 == 0
            -> System.out.println("fizz");
            case Integer n when n % 5 == 0
            -> System.out.println("buzz");
            default -> System.out.println(i);
        }
    }
}
}