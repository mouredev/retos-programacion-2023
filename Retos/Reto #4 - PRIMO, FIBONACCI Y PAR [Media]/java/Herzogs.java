package reto04;

import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.IntStream;

public class Herzogs {

    static class RetoSemanal {
        private final Integer number;

        public RetoSemanal(Integer num) {
            this.number = num;
        }

        public Boolean esPar() {return this.number % 2 == 0;}

        public Boolean esPrimo() {
            if (this.number > 0) {
                AtomicReference<Integer> cantPrimos = new AtomicReference<>(0);
                IntStream.rangeClosed(1,this.number).forEach(i -> cantPrimos.updateAndGet(v -> v + (this.number % i == 0 ? 1 : 0)));
                return cantPrimos.get().equals(2);
            }
            return false;
        }

        public Boolean pertenceFibonacci() {
            Integer num1 = 0, num2 = 1, term = 0;
            do {
                if (number > term)
                    term = num1 + num2;
                num1 = num2;
                num2 = term;
            } while (number > term);
            return number.equals(term);
        }

        public Integer getNum() {
            return this.number;
        }
    }

    public static void main(String[] args) {
        RetoSemanal nuevoReto = new RetoSemanal(4);
        System.out.printf("El numero %d",nuevoReto.getNum());
        System.out.printf("\n%s",nuevoReto.esPar()?"Es par":"Es impar");
        System.out.printf("\n%s",nuevoReto.esPrimo()? "Es Primo":"No es Primo");
        System.out.printf("\n%s", nuevoReto.pertenceFibonacci() ? "Incluido en Fibonnaci" : "No incluido a Fibonnaci");
    }
}
