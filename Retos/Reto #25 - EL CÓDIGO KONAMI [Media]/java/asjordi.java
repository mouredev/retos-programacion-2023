import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;

public class KonamiCode extends JFrame{

    private final ArrayList<Integer> keys = new ArrayList<>();
    private final JLabel l;

    public static void main(String[] args) {
        KonamiCode kc = new KonamiCode();
        kc.setVisible(true);
    }

    public KonamiCode(){
        setTitle("Konami Code");
        setSize(300, 300);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        l = new JLabel("Type the Konami code");
        l.setHorizontalAlignment(SwingConstants.CENTER);
        l.setVerticalAlignment(SwingConstants.CENTER);
        add(l);

        setLocationRelativeTo(null);
        setVisible(false);
        setFocusable(true);
        requestFocus();

        addKeyListener(new KonamiKeyListener());
    }

    private class KonamiKeyListener extends KeyAdapter{

        private int index = 0;

        public void keyPressed(KeyEvent e){

            ArrayList<Integer> code = getKonamiCode();
            List<Integer> subList;
            int keyCode = e.getKeyCode();

            if (e.getKeyCode() == KeyEvent.VK_ESCAPE) System.exit(0);

            if (code.contains(keyCode)){

                if (keyCode == KeyEvent.VK_UP) keys.add(KeyEvent.VK_UP);
                if (keyCode == KeyEvent.VK_DOWN) keys.add(KeyEvent.VK_DOWN);
                if (keyCode == KeyEvent.VK_RIGHT) keys.add(KeyEvent.VK_RIGHT);
                if (keyCode == KeyEvent.VK_LEFT) keys.add(KeyEvent.VK_LEFT);
                if (keyCode == KeyEvent.VK_B) keys.add(KeyEvent.VK_B);
                if (keyCode == KeyEvent.VK_A) keys.add(KeyEvent.VK_A);

                if (keys.size() >= code.size()){
                    subList = keys.subList(this.index, keys.size());
                    if (code.equals(subList)){
                        l.setText("Konami code detected!");
                    } else {
                        this.index++;
                    }
                }
            }
        }

        private ArrayList<Integer> getKonamiCode(){
            ArrayList<Integer> konamiCode = new ArrayList<>();

            konamiCode.add(KeyEvent.VK_UP);
            konamiCode.add(KeyEvent.VK_UP);
            konamiCode.add(KeyEvent.VK_DOWN);
            konamiCode.add(KeyEvent.VK_DOWN);
            konamiCode.add(KeyEvent.VK_LEFT);
            konamiCode.add(KeyEvent.VK_RIGHT);
            konamiCode.add(KeyEvent.VK_LEFT);
            konamiCode.add(KeyEvent.VK_RIGHT);
            konamiCode.add(KeyEvent.VK_B);
            konamiCode.add(KeyEvent.VK_A);

            return konamiCode;
        }

        @Override
        public void keyTyped(KeyEvent e) {}

        @Override
        public void keyReleased(KeyEvent e) {}
    }
}
