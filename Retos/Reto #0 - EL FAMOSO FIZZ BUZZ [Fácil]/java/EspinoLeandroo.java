public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        for (int i = 1; i <= 100; i++) {
            boolean isMultipleOf3 = espinoLeandroo.isMultipleOf3(i);
            boolean isMultipleOf5 = espinoLeandroo.isMultipleOf5(i);

            if(isMultipleOf3 && isMultipleOf5){
                System.out.println("fizzbuzz");
            }else if (isMultipleOf3){
                System.out.println("fizz");
            }else if (isMultipleOf5){
                System.out.println("buzz");
            }else{
                System.out.println(i);
            }
        }

    }

    private boolean isMultipleOf3(int num){
        //A number is divisible by 3 if the sum of its digits is a multiple of 3.
        String number = "" + num;
        int sum = 0;
        for(int i = 0; i < number.length(); i++){
            sum += number.charAt(i) - 48;
        }
        return (sum % 3 == 0);
    }
    private boolean isMultipleOf5(int num){
        //A number is divisible by 5 if it ends in 0 or 5.
        String number = "" + num;
        char lastDigit = number.charAt(number.length()-1);
        return (lastDigit == '5' || lastDigit == '0');
    }
}