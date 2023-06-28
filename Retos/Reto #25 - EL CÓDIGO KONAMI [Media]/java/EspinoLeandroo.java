import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class EspinoLeandroo implements KeyListener {
    private static final int[] KONAMI_CODE = {KeyEvent.VK_UP, KeyEvent.VK_UP, KeyEvent.VK_DOWN,
            KeyEvent.VK_DOWN, KeyEvent.VK_LEFT, KeyEvent.VK_RIGHT, KeyEvent.VK_LEFT,
            KeyEvent.VK_RIGHT, KeyEvent.VK_B, KeyEvent.VK_A};

    private int konamiIndex;

    public EspinoLeandroo() {
        konamiIndex = 0;
    }

    public static void main(String[] args) {
        EspinoLeandroo detector = new EspinoLeandroo();
        detector.start();
    }

    public void start() {
        System.out.println("Ingrese el Código Konami:");
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (scanner.hasNext()) {
            int keyCode = convertToKeyCode(scanner.next());
            System.out.println(keyCode);
            if (keyCode == KONAMI_CODE[konamiIndex]) {
                konamiIndex++;
                if (konamiIndex == KONAMI_CODE.length) {
                    System.out.println("¡Código Konami detectado!");
                    konamiIndex = 0;
                }
            } else {
                konamiIndex = 0;
            }
        }
    }

    private int convertToKeyCode(String input) {
        switch (input.toUpperCase()) {
            case "UP":
                return KeyEvent.VK_UP;
            case "DOWN":
                return KeyEvent.VK_DOWN;
            case "LEFT":
                return KeyEvent.VK_LEFT;
            case "RIGHT":
                return KeyEvent.VK_RIGHT;
            case "B":
                return KeyEvent.VK_B;
            case "A":
                return KeyEvent.VK_A;
            default:
                return KeyEvent.VK_UNDEFINED;
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }
}
