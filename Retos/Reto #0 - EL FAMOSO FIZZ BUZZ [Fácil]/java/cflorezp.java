package reto0FizzBuzz;

public class cflorezp {

    public static void main(String[] args) {

        for(int i = 1; i <= 100; i++){
            String print = "";
            print = (i % 3 == 0) ? "fizz" : "";
            print += (i % 5 == 0)? "buzz" : "";
            print = (print.equals("")) ? String.valueOf(i) : print;
            System.out.println(print);
        }


    }
}
