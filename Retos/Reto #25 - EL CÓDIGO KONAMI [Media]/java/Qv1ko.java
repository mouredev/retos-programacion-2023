import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;

import javax.swing.JFrame;

public class Qv1ko implements KeyListener {

    private final int[] KONAMICODE = { KeyEvent.VK_UP, KeyEvent.VK_DOWN, KeyEvent.VK_UP, KeyEvent.VK_DOWN, KeyEvent.VK_LEFT, KeyEvent.VK_RIGHT, KeyEvent.VK_LEFT, KeyEvent.VK_RIGHT, KeyEvent.VK_B, KeyEvent.VK_A };
    private ArrayList<Integer> userInput = new ArrayList<Integer>();

    public static void main(String[] args) {
        Qv1ko detector = new Qv1ko();
        JFrame frame = new JFrame("Konami Detector");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.addKeyListener(detector);
        frame.setFocusable(true);
        frame.requestFocus();
        frame.setSize(10, 10);
        frame.setVisible(true);
    }

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if (key != KeyEvent.VK_ENTER) {
            userInput.add(key);
        } else {
            checkKonamiCode();
        }
    }

    private void checkKonamiCode() {
        if (userInput.size() == KONAMICODE.length) {
            boolean correctCode = true;
            for (int i = 0; i < KONAMICODE.length; i++) {
                if (userInput.get(i) != KONAMICODE[i]) {
                    correctCode = false;
                    break;
                }
            }
            if (correctCode) {
                System.out.println("Konami code entered correctly!");
            }
        }
        userInput.clear();
    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyReleased(KeyEvent e) {
    }

}
