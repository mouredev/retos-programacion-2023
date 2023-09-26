public static void main(String[] args){

public void mostrarNum(){
        for (int i = 0; i < 100; i++) {
            if(i%3==0 && i%5!=0){
                System.out.println("N°: " + "fizz");
            } else if(i%5==0 && i%3!=0){
                System.out.println("N°: " + "buzz");
            } else if (i%3==0 && i%5==0){
                System.out.println("N°: " + "fizzbuzz");
            }else{
                System.out.println("N°: " + i);
            }   
        }
    }
  mostrarNum();
}
