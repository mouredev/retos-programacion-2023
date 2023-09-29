"""
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 *   
 *
 * Autor: Víctor Andrés
 * Fecha: 18-8-2023
 * Instrucciones: 
 *      - Instala la libreria tkinter ->  brew install python-tk@3.11
 * Mueve la pieza con las flechas y rotla con la tecla de espacio
 * Para salir de la aplicación utiliza la tecla Ctrl
 """

import tkinter as tk
import sys

class Piece:
    piece = []

    positionX=0;
    positionY=0;

    def __init__(self):
        self.piece = [[1, 0, 0],[1, 1, 1]]

    def rotate(self):
        self.piece = list(zip(*self.piece))[::-1]
                
    def getValues(self) ->[]:
        return self.piece
    
    def getPositionX(self)->int:
        return self.positionX
    
    def getPositionY(self) -> int:
        return self.positionY;
    
    def setPositionX(self, x):
        self.positionX = x;
    
    def setPositionY(self, y):
        self.positionY = y;

    def getPieceWidth(self)->int:
        return len(self.piece[0]);

    def getPieceHeight(self)->int:
        return len(self.piece);
    
    def isPermitedTop(self)->bool:
        return self.getPositionY()-1 >= 0;
    
    def isPermitedDown(self)->bool:
        return (self.getPieceHeight()+self.getPositionY()+1)<= 10;
    
    def isPermitedLeft(self)->bool:
        return self.getPositionX()-1 >= 0;
    
    def isPermitedRight(self)->bool:
        return (self.getPieceWidth()+self.getPositionX()+1)<= 10;
    
    def isPermitedRotate(self)->bool:
        if (self.getPieceWidth()> self.getPieceHeight()):
            return self.isPermitedDown()
        else:
            return self.isPermitedRight()
 

def on_press(event):
    global piece
    global paned_window
    if event.keysym == "Down":
        if(piece.isPermitedDown()):
            piece.setPositionY(piece.getPositionY()+1);
            resetGrid(paned_window)
            setPiece(paned_window, piece)
    elif event.keysym == "Up":
        if(piece.isPermitedTop()):
            piece.setPositionY(piece.getPositionY()-1);
            resetGrid(paned_window)
            setPiece(paned_window, piece)
    elif event.keysym == "Left":
        if(piece.isPermitedLeft()):
            piece.setPositionX(piece.getPositionX()-1);
            resetGrid(paned_window)
            setPiece(paned_window, piece)
    elif event.keysym == "Right":
        if(piece.isPermitedRight()):
            piece.setPositionX(piece.getPositionX()+1);
            resetGrid(paned_window)
            setPiece(paned_window, piece)
    elif event.keysym == "space":
       if(piece.isPermitedRotate()):
            piece.rotate();
            resetGrid(paned_window)
            setPiece(paned_window, piece)
    elif event.keysym == "Escape":
        sys.exit()

def resetGrid(paned_window):       
    for i in range(1,101):
        if i == 1:
            card = ''
        else:
            card = i
        label_by_id = paned_window.nametowidget(f".!panedwindow.!label{card}")
        label_by_id.config(background="#ffffff")
    
def setPiece(paned_window, piece):
    pValues = piece.getValues();
    x = piece.getPositionX();
    y = piece.getPositionY();
    for i in range(0, len(pValues)):
        for j in range(0, len(pValues[i])):
            if pValues[i][j]==1 :
                row = y + i
                col = x + j
                position = (row*10)+col + 1
                if position == 1:
                    card = ''
                else:
                    card = position
                label_by_id = paned_window.nametowidget(f".!panedwindow.!label{card}")
                label_by_id.config(background="#ff0000")

if __name__ == "__main__":
    window = tk.Tk()
    window.wm_title("Tetris")
    window.geometry("370x460")
    label = tk.Label(window, text="Bienvenido al juego del Tetris!!")
    label.pack()
    label = tk.Label(window, text="Mueve la pieza con los cursores")
    label.pack()
    label = tk.Label(window, text="Rota la pieza con la tecla espacio")
    label.pack()
    label = tk.Label(window, text="Sal de la aplicación con la tecla escape")
    label.pack()
    paned_window = tk.PanedWindow(window)
    paned_window.pack()
    for i in range(10):
        for j in range(10):
            card = tk.Label(paned_window, text="", borderwidth=1, relief="solid", background="#FFFFFF", width=3, height=2)
            card.grid(row=i, column=j)
            card.id = f"label-{i}-{j}"

    end = False
    piece = Piece()
    resetGrid(paned_window)
    setPiece(paned_window, piece)

    window.bind("<Up>", on_press)
    window.bind("<Down>", on_press)
    window.bind("<Left>", on_press)
    window.bind("<Right>", on_press)
    window.bind("<space>", on_press)
    window.bind("<Escape>", on_press)

    window.mainloop()

