import javax.swing.JOptionPane;

class NamelessReact {
    public void checkNumber(int number) {
        boolean isPrime = true;
        boolean isFibonacci = false;
        boolean isEven = false;
        
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }
        JOptionPane.showMessageDialog(null, isPrime ? "Es un número primo" : "No es un número primo");
        
        
        int firstDifferenceSquare = (int) (Math.sqrt(5 * number * number + 4));
        int secondDifferenceSquare = (int) (Math.sqrt(5 * number * number - 4));
        
        isFibonacci = firstDifferenceSquare * firstDifferenceSquare == (5 * number * number + 4) ||  secondDifferenceSquare * secondDifferenceSquare == (5 * number * number - 4);
        JOptionPane.showMessageDialog(null, isFibonacci ? "Es un número de fibonacci" : "No es un número de fibonacci");
        
        
        
        if (number % 2 == 0) isEven = true;
        JOptionPane.showMessageDialog(null, isEven ? "Es un número par" : "No es un número par");        
    }
}
