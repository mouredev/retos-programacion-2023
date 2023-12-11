package lcozatl;

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.TimeUnit;

public class lcozatl {

    private static final char OBSTACLE_SYMBOL = '|';
    private static final char AUTO_SYMBOL = '<';
    private static final char CRASH_SYMBOL = '*';
    private static final char WIN_SYMBOL = '$';

    private static final int SHIFT_DELAY_SECONDS = 1;
    private static final int MIN_MOVE = 1;
    private static final int MAX_MOVE = 3;
    private static final int NUMBER_OF_CARS = 2;
    private static final int POSITIONS = 10;
    private static final int MIN_GAP_BETWEEN_TREES = 3;

    public static void main(String[] args) {
        race();
    }
    
    public static void race(){
        HashMap<Integer, Track> circuits = new HashMap<>();
        if (NUMBER_OF_CARS <= 0) {
            System.out.println("Imposible ejecutar sin autos");
        }
        
        lcozatl mainClass = new lcozatl();

        System.out.println("/* /* /* /* Circuito inicial");
        for (int i = 0; i < NUMBER_OF_CARS; i++) {
            circuits.put(i, mainClass.new Track());
            System.out.println(circuits.get(i).getTrack() + " - > Auto " + (i+1));
        }

        boolean noCarWon = true;
        int shift = 0;
        List<Integer> winners = new ArrayList<Integer>();
        while(noCarWon){
            try {
                TimeUnit.SECONDS.sleep(SHIFT_DELAY_SECONDS);
            } catch (InterruptedException e) {
            }
            shift++;
            System.out.println("/* /* /* /* Turno: " + shift);
            for (int car : circuits.keySet()) {
                Track currentTrack = circuits.get(car);
                int positions = howManyAdvance();
                String advance = "";
                if (!currentTrack.moveCar(positions)) {
                    advance = " No avanzó debido al choque con un obstaculo";
                }else{
                    advance = " avanzo: " + positions + " posiciones";
                }
                System.out.println(currentTrack.getTrack() + " - > El auto " + (car+1) + advance);
                if (currentTrack.carWon) {
                    winners.add(car+1);
                    noCarWon = false;
                }
            }
        }
        if (winners.size()>1) {
            System.out.println("Carrera terminada, empate de los autos: " + winners.toString());
        }else{
            System.out.println("Carrera terminada, gana el auto: " + winners.get(0));
        }
    }
    
    public static int howManyAdvance() {
        Random random = new Random();

        int randomNumber = random.nextInt(MAX_MOVE) + MIN_MOVE;

        return randomNumber;
    }

    public class Track{
        private int positions = POSITIONS;
        private int carPosition = POSITIONS + 1;
        private boolean carLocked;
        private StringBuilder track = new StringBuilder();
        private boolean carWon = false;

        public Track(){
            generateTrack();
            addRandomTrees();
        }

        private void generateTrack(){
            
            this.track.append("#");
            for (int i = 0; i <= positions; i++) {
                this.track.append("_");
            }

        }

        private void addRandomTrees() {
            Random random = new Random();
            
            int maxTrees = POSITIONS / 2;
            int numbOfTrees = random.nextInt(maxTrees) + 1;
            
            if (numbOfTrees <= 0) {
                return;
            }
            
            int length = this.track.length() -1;
            
            for (int i = 1; i < POSITIONS && numbOfTrees > 0; i++) {
                boolean placeTree = false;
                placeTree = (random.nextInt(length)+1) % 2 != 0;
                if (placeTree) {
                    this.track.setCharAt(i, OBSTACLE_SYMBOL);
                    i += MIN_GAP_BETWEEN_TREES;
                }

            }

        }
        
        public boolean moveCar(int positions){
            if (carLocked) {
                return carLocked = false;
            }

            this.carPosition = this.carPosition - positions; 

            if (carPosition >= 0 && this.track.charAt(carPosition) == OBSTACLE_SYMBOL) {
                carLocked = true;
            }

            return true;
        }
        
        public String getTrack(){
            StringBuilder tempTrack = new StringBuilder(this.track);
            char carSymbol = AUTO_SYMBOL;
            if (carLocked) {
                carSymbol = CRASH_SYMBOL;
            }
            if (this.carPosition <= 0) {
                carSymbol = WIN_SYMBOL;
                carWon = true;
                this.carPosition = 0;
            }
            tempTrack.setCharAt(this.carPosition, carSymbol);
            return tempTrack.toString();
        }

    }

}