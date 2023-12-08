/**
 * Create a program that detects if the Konami secuence (↑ ↑ ↓ ↓ ← → ← → B A)
 * has been pressed. The program will read the user input and if the secuence
 * it's detected, it will show a message in the terminal.
 * @author Ivan Ruiz Marcos
 * @version 1.0
 */

 
import static java.awt.event.KeyEvent.VK_A;
import static java.awt.event.KeyEvent.VK_B;
import static java.awt.event.KeyEvent.VK_DOWN;
import static java.awt.event.KeyEvent.VK_LEFT;
import static java.awt.event.KeyEvent.VK_RIGHT;
import static java.awt.event.KeyEvent.VK_SHIFT;
import static java.awt.event.KeyEvent.VK_UP;

import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
 

 public class Ivanrm extends JFrame {

    private JLabel messageLabel;
    private List<Integer> keystrokes = new ArrayList<>();
    private boolean isKonamiCode;

    /**
     * Constructor. It creates the window and adds the key listener.
     */
    public Ivanrm() {
        setTitle("Konami Code Detector");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        messageLabel = new JLabel("Press keys until you get the Konami code!");
        messageLabel.setHorizontalAlignment(SwingConstants.CENTER);
        messageLabel.setVerticalAlignment(SwingConstants.CENTER);
        add(messageLabel);
        setLocationRelativeTo(null);

        MyKeyListener keyListener = new MyKeyListener();
        addKeyListener(keyListener);

        setFocusable(true);
        requestFocus();

        isKonamiCode = false;
    }

    private class MyKeyListener extends KeyAdapter {

        @Override
        public void keyPressed(KeyEvent e) {
            keystrokes.add(e.getKeyCode());
            messageLabel.setText(KeyEvent.getKeyText(e.getKeyCode()));
            if (isKonamiCode(keystrokes)) {
                isKonamiCode = true;
                messageLabel.setText("Congratulations! You have found the Konami code!");
                messageLabel.setForeground(Color.RED);
                setEnabled(false);                      // Disable the keylistener
            }
        }
    }

    public boolean isKonamiCode(List<Integer> keystrokes) {

        // The key constants are defined in the KeyEvent class. Consult:
        // https://docs.oracle.com/javase/8/docs/api/java/awt/event/KeyEvent.html
        final Integer konamiCode[] = {
                                    VK_UP, VK_UP,
                                    VK_DOWN, VK_DOWN,
                                    VK_LEFT, VK_RIGHT,
                                    VK_LEFT, VK_RIGHT,
                                    VK_SHIFT, VK_B,
                                    VK_SHIFT, VK_A
                                    };
        for (int i = keystrokes.size() - 1, j = konamiCode.length - 1;
             (i >= keystrokes.size() - konamiCode.length) && j >= 0;
              i--, j--) {
            if (keystrokes.get(i) != konamiCode[j]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Ivanrm konamiGame = new Ivanrm();
        konamiGame.setVisible(true);

        while(!konamiGame.isKonamiCode);
        
    }
 }