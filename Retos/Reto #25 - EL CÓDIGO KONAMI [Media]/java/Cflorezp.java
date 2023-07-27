package reto25codigoKonami;

import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;

/*
 * Crea un programa que detecte cuando el famoso "Código Konami (↑ ↑ ↓ ↓ ← → ← → B A)"
 * se ha introducido correctamente desde el teclado. Si sucede esto, debe notificarse
 * mostrando un mensaje en la terminal.
 */
public class Cflorezp extends JFrame {

    private JLabel mensajeLabel;
    private List<String> teclas = new ArrayList<>();

    public Cflorezp() {
        setTitle("Detectar Tecla Pulsada");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mensajeLabel = new JLabel("Presiona una tecla");
        mensajeLabel.setHorizontalAlignment(SwingConstants.CENTER);
        mensajeLabel.setVerticalAlignment(SwingConstants.CENTER);
        add(mensajeLabel);
        setLocationRelativeTo(null);

        addKeyListener(new MiKeyListener());

        setFocusable(true);
        requestFocus();
    }

    private class MiKeyListener extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            int tecla = e.getKeyCode();
            switch (tecla) {
                case KeyEvent.VK_UP:
                    teclas.add("U");
                    mensajeLabel.setText("Se presiono: ↑");
                    break;
                case KeyEvent.VK_DOWN:
                    teclas.add("D");
                    mensajeLabel.setText("Se presiono: ↓");
                    break;
                case KeyEvent.VK_LEFT:
                    teclas.add("L");
                    mensajeLabel.setText("Se presiono: ←");
                    break;
                case KeyEvent.VK_RIGHT:
                    teclas.add("R");
                    mensajeLabel.setText("Se presiono: →");
                    break;
                case KeyEvent.VK_B:
                    teclas.add("B");
                    mensajeLabel.setText("Se presiono: B");
                    break;
                case KeyEvent.VK_A:
                    teclas.add("A");
                    mensajeLabel.setText("Se presiono: A");
                    break;
                default:
                    teclas.add("X");
                    mensajeLabel.setText("Se presiono: " + e.getKeyChar());
            }

            if (e.getKeyChar() == 'a' || e.getKeyChar() == 'A' && teclas.size() >= 10) {
                String secuenciaCadena = String.join("", teclas);
                String secuenciaEvaluar = secuenciaCadena.substring(secuenciaCadena.length() - 10);
                if (secuenciaEvaluar.equalsIgnoreCase("uuddlrlrba")) {
                    mensajeLabel.setText("¡CODIGO KONAMI ENCONTRADO!   ↑ ↑ ↓ ↓ ← → ← → B A ");
                }
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Cflorezp konami = new Cflorezp();
            konami.setVisible(true);
        });
    }
}
