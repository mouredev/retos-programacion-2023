import javax.swing.*;

import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.HashMap;
import java.util.Map;

public class vandresca {

    JFrame frame = new JFrame("Tetris");
    JPanel panel = new JPanel();
    JLabel welcome = new JLabel();
    JLabel instruction1 = new JLabel();
    JLabel instruction2 = new JLabel();
    JLabel instruction3 = new JLabel();
    JLabel space = new JLabel(" ");
    JPanel grid = new JPanel();
    Map<Integer, JLabel> cards = new HashMap<>();
    Piece piece;

    public vandresca(){
        welcome.setText("Bienvendio al juego del tetris!!");
        instruction1.setText("Mueve la pieza con los cursores");
        instruction2.setText("Rotala con espacio");
        instruction3.setText("Sal de la aplicación con escape.");
        grid.setLayout(new GridLayout(10, 10, 1, 1));
        for( int i=0; i<100; i++){
            JLabel card = new JLabel();
            card.putClientProperty("id", i);
            card.setEnabled(false);
            card.setBackground(Color.LIGHT_GRAY);
            card.setOpaque(true);
            cards.put(i, card);
            grid.add(card);
        }
        BoxLayout panelLayout =new BoxLayout(panel, BoxLayout.Y_AXIS);
        panel.setLayout(panelLayout);
        panel.add(welcome);
        panel.add(instruction1);
        panel.add(instruction2);
        panel.add(instruction3);
        panel.add(space);
        panel.add(grid);
        frame.add(panel);
        frame.setSize(400, 550);
        frame.setVisible(true);
        loadEvents();
        piece = new Piece();
        setPiece(piece);
    }


    public static void main(String[] args) throws Exception {
        SwingUtilities.invokeLater(new Runnable(){

            @Override
            public void run() {
                new  vandresca();
            }

        });
    }

    public void loadEvents(){
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        KeyListener keyListener = new KeyListener() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_UP) {
                    if(piece.isPermitedTop()){
                        piece.setPositionY(piece.getPositionY()-1);
                        resetBackgroundGrid();
                        setPiece(piece);
                    }
                }
                if (e.getKeyCode() == KeyEvent.VK_DOWN) {
                    if(piece.isPermitedDown()){
                        piece.setPositionY(piece.getPositionY()+1);
                        resetBackgroundGrid();
                        setPiece(piece);
                    }
                }
                if (e.getKeyCode() == KeyEvent.VK_LEFT) {
                    if(piece.isPermitedLeft()){
                        piece.setPositionX(piece.getPositionX()-1);
                        resetBackgroundGrid();
                        setPiece(piece);
                    }
                }
                if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
                    if(piece.isPermitedRight()){
                        piece.setPositionX(piece.getPositionX()+1);
                        resetBackgroundGrid();
                        setPiece(piece);
                    }
                }
                if (e.getKeyCode() == KeyEvent.VK_SPACE) {
                    if(piece.isPermitedRotate()){
                        piece.rotate();
                        resetBackgroundGrid();
                        setPiece(piece);
                    }
                }
                if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
                    System.exit(0);
                }
            }
            @Override
            public void keyReleased(KeyEvent e) {
            }

            @Override
            public void keyTyped(KeyEvent e) {
            }
        };

        frame.addKeyListener(keyListener);
    }

    public void setPiece(Piece piece){
        int[][] pValues = piece.getValues();
        int x = piece.getPositionX();
        int y = piece.getPositionY();
        int row, col;
        for (int i = 0; i < pValues.length; i++) {
            for(int j=0; j<pValues[i].length; j++){
                if(pValues[i][j]==1){
                    row = y + i;
                    col = x + j;
                    JLabel cardChoosed = cards.get((row*10)+col);
                    cardChoosed.setBackground(Color.RED);;
                }
            }
        }
    }

    public void resetBackgroundGrid(){
        for(int i=0; i<100; i++){
            JLabel cardChoosed = cards.get(i);
            cardChoosed.setBackground(Color.LIGHT_GRAY);
        }
    }
}


class Piece {

    private int[][] piece;

    private int positionX=0;
    private int positionY=0;

    public Piece() {
        piece = new int[][]{
            {1, 0, 0},
            {1, 1, 1}
        };
    }

    public void rotate() {
        int[][] temp = new int[piece[0].length][piece.length];
        for (int i = 0; i < piece.length; i++) {
            for (int j = 0; j < piece[0].length; j++) {
                temp[j][piece.length - 1 - i] = piece[i][j];
            }
        }
        piece=temp;
    }

    public int[][] getValues(){
        return piece;
    }

    public int getPositionX(){
        return positionX;
    }

    public int getPositionY(){
        return positionY;
    }

    public void setPositionX(int x){
        positionX = x;
    }

    public void setPositionY(int y){
        positionY = y;
    }

    public int getPieceWidth(){
        return piece[0].length;
    }

    public int getPieceHeight(){
        return piece.length;
    }

    public boolean isPermitedTop(){
        return getPositionY()-1 >= 0;
    }

    public boolean isPermitedDown(){
        return (getPieceHeight()+getPositionY()+1)<= 10;
    }

    public boolean isPermitedLeft(){
        return getPositionX()-1 >= 0;
    }

    public boolean isPermitedRight(){
        return (getPieceWidth()+getPositionX()+1)<= 10;
    }

    public boolean isPermitedRotate(){
        if (getPieceWidth()> getPieceHeight()){
            return isPermitedDown();
        }else{
            return isPermitedRight();
        }
    }
}