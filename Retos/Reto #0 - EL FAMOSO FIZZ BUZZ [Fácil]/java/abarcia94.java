class Main {
    public static void main(String[] args) {
        fizzBuzz();
    }

    public static void fizzBuzz() {
	for (int i = 0 ; i <= 100 ; i++ ){
		if( i % 3 == 0 && i % 5 == 0 ){
			System.out.println("fizzbuzz\n");
		} else if( i % 3 == 0  ){
				System.out.println("fizz\n");
			} else if( i % 5 == 0  ){
					System.out.println("buzz\n");
			} else {
				System.out.println(i + "\n");
			}
		}
	} 
}
