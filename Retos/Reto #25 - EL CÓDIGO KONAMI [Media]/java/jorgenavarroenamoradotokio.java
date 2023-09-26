package com.retos.ej25;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

public class jorgenavarroenamoradotokio {

	private static final int[] KONAMI_CODE = { KeyEvent.VK_UP, KeyEvent.VK_UP, KeyEvent.VK_DOWN, KeyEvent.VK_DOWN,
			KeyEvent.VK_LEFT, KeyEvent.VK_RIGHT, KeyEvent.VK_LEFT, KeyEvent.VK_RIGHT, KeyEvent.VK_B, KeyEvent.VK_A };

	private static int keyPosition = 0;
	private static int lastKey = KeyEvent.VK_ESCAPE;

	public static void main(String[] args) {
		JFrame frame = new JFrame("Konami Code Detector");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.addKeyListener(new KeyListener() {
			@Override
			public void keyTyped(KeyEvent e) {
				// No se utiliza en este ejemplo
			}

			@Override
			public void keyPressed(KeyEvent e) {
				int key = e.getKeyCode();

				if (key == KeyEvent.VK_ESCAPE) {
					System.out.println("Exit");
					System.exit(0);
				}

				if (key == KONAMI_CODE[keyPosition]) {
					keyPosition++;
				} else if (key == KONAMI_CODE[0]) {
					if (lastKey == KONAMI_CODE[0]) {
						keyPosition = 2;
					} else {
						keyPosition = 1;
					}
				} else {
					keyPosition = 0;
				}

				if (keyPosition == KONAMI_CODE.length) {
					System.out.println("\n" + "╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗\n" + "╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║║╣\n"
							+ "╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝\n" + "\n");
					System.exit(0);
				}

				lastKey = key;
			}

			@Override
			public void keyReleased(KeyEvent e) {
				// No se utiliza en este ejemplo
			}
		});

		frame.setSize(200, 200);
		frame.setVisible(true);
	}
}
