/*see in stackblitz:
  https://stackblitz.com/edit/stackblitz-starters-q7s3ze?file=src%2Fmain.ts
*/

import 'zone.js/dist/zone';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { bootstrapApplication } from '@angular/platform-browser';
import {squarePiece,iPiece,lPiece,lmPiece,zPiece,nPiece,tPiece, emptyBoard, blankLine } from './pieces';
import {
  fromEvent,
  Subscription,
  timer,
  Observable,
  merge,
  Subject,
} from 'rxjs';
import { take, finalize, filter, map, tap } from 'rxjs/operators';
@Component({
  selector: 'my-app',
  standalone: true,
  imports: [CommonModule],
  template: `
<div class="container">
  <div class="board">
    <div *ngFor="let row of nextPiece.data[rotation]">
      <div
        *ngFor="let cell of row"
        [style.border-width]="cell?1:0"
        [style.background-color]="cell && nextPiece.color"
      ></div>
    </div>
  </div>
  <div class="center">
    <h1>Points: {{points}}</h1>
    <div class="wrapper">
      <div class="board">
        <div *ngFor="let row of board">
          <div
            *ngFor="let cell of row"
            [style.background-color]="cell"
            [style.border-width]="cell?1:0"
          ></div>
        </div>
      </div>
      <div class="label" *ngIf="status==1" (click)="startGame()">
        <h2>Click to start</h2>
      </div>
      <div class="label" *ngIf="status==2" (click)="newGame();startGame()">
        <h2>Game Over</h2>
        (click to new game)
      </div>
    </div>
    <div class="keyboard">
      <button (click)="btSubject.next([(rotation + 7) % 4,posX,posY])">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-arrow-clockwise"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2v1z"
          />
          <path
            d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466z"
          />
        </svg>
      </button>
      <button (click)="btSubject.next([rotation,posX-1,posY])">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-chevron-left"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"
          />
        </svg>
      </button>
      <button (click)="btSubject.next([rotation,posX+1,posY])">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-chevron-right"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"
          />
        </svg>
      </button>
      <button (click)="btSubject.next([rotation,posX,posY+1])">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-chevron-down"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"
          />
        </svg>
      </button>
    </div>
  </div>
</div>
  `,
  styles: [
    `
    h1 {
      margin-bottom: 0;
    }
    h2 {
      margin-top: 3rem;
    }
    .keyboard {
      width: 10rem;
      margin-left: auto;
      display: grid;
      grid-template-columns: repeat(3, 3rem);
      margin-top: 1rem;
    }
    .keyboard button {
      background-color: royalblue;
      color: white;
      outline: 0;
      width: 3rem;
      height: 3rem;
      border-radius: 3rem;
      border: 0;
      margin-bottom: -1rem;
    }
    .keyboard button:nth-child(1) {
      grid-column: 2;
    }
    .keyboard button:nth-child(2) {
      grid-row: 2;
    }
    .keyboard button:nth-child(3) {
      grid-row: 2;
      grid-column: 3;
    }
    .keyboard button:nth-child(4) {
      grid-row: 3;
      grid-column: 2;
    }
    .keyboard button:hover,
    .keyboard button:active {
      background-color: #213a82;
    }
    .label {
      position: absolute;
      z-index: 20;
      top: 0;
      bottom: 0;
      width: 100%;
      background-color: rgba(255, 255, 255, 0.5);
      text-align: center;
      cursor: pointer;
    }
    .center{
      width:20rem;
    }
    .wrapper {
      position: relative;
      margin-left:1rem;
    }
    .board{
      min-width:7rem;
    }
    .board > div div {
      border: 1px solid silver;
      width: 1.2rem;
      height: 1.2rem;
      display: inline-block;
      box-sizing: border-box;
    }
    .board > div {
      height: 1.2rem;
    }
    .board .fill {
      background-color: silver;
    }
    .container{
      display:flex;
      width:22.5rem;
      margin:auto;
      justify-content: flex-start;
    }
      `,
  ],
})
export class App implements OnInit, OnDestroy {
  status: number = 1; //0=Game, 1, Click to start, 2, New game, 3 pause
  points: number = 0;
  timeActual: number = 0;
  interval = 1000;

  //variables de la pieza en movimiento
  rotation = 0;
  posX = 5;
  posY = -10;

  //"tablero"
  board: any[] = [];
  pieces = [squarePiece,iPiece,lPiece,lmPiece,zPiece,nPiece,tPiece];
  piece = this.pieces[Math.floor(this.pieces.length * Math.random())];
  nextPiece = this.pieces[Math.floor(this.pieces.length * Math.random())];

  //Observable y subscripción
  control$!: Observable<any>;
  sub!: Subscription;

  btSubject: Subject<{rotation:number,posX:number,posY:number}> = new Subject<{rotation:number,posX:number,posY:number}>();

  //checkPiece
  checkPiece=0;
  ngOnInit() {
    setTimeout(() => {
      this.newGame();
    });
  }

  newGame() {
    this.board = emptyBoard.map((x) => [...x]);
  }
  getObservable():Observable<{rotation:number,posX:number,posY:number}>
  {
    //Observable botones
    const buttons$ = this.btSubject as Observable<{rotation:number,posX:number,posY:number}>;

    //Observable teclado
    const keyboard$ = fromEvent(document, 'keydown').pipe(
      filter((x: any) => x.keyCode >= 37 && x.keyCode <= 40),
      map((x: any) => {
        const code = x.keyCode;
        if (code == 37) return {rotation:this.rotation,posX:this.posX - 1, posY:this.posY};
        if (code == 39) return {rotation:this.rotation, posX:this.posX + 1, posY:this.posY};
        if (code == 40) return {rotation:this.rotation, posX:this.posX, posY:this.posY + 1};
        const rotation = (this.rotation + 7) % 4;
        return {rotation:rotation, posX:this.posX, posY:this.posY};
      })
    );
    //Observable de tiempo
    const timer$ = timer(0, this.interval).pipe(
      map((_) => ({rotation:this.rotation, posX:this.posX, posY:this.posY + 1})),
    );
    return merge(timer$, buttons$, keyboard$);
  }
  
  startGame() {
    this.status = 0;
    this.points = 0;
    this.interval=1000;
    this.newPiece();

  }
  subscribe(){
    this.sub && this.sub.unsubscribe();
    //Nos subscribimos al observable
    this.sub = this.getObservable().subscribe(
      ({rotation, posX, posY}) => {
        if (this.status) return;
        this.removeBoard(); //limpiamos el "board" con la pieza en el estado actual
        if (this.check(rotation, posX, posY)) {
          //si se permite el movimiento
          this.rotation = rotation; //cambiamos los valores
          this.posX = posX;
          this.posY = posY;
          this.fillBoard(); //rellenamos el "board" con los nuevos valores
        } else {
          this.fillBoard(); //rellenamos el board con los valores anteriores
          if (this.posY < posY)
            //si hemos estado bajando
            this.checkDeleteLines(); //comprobamos las líneas a borrar
        }
      }
    );
  }

  //check si la pieza se puede mover a la posición indicada
  private check(rotation: number, posX: number, posY: number) {
    for (let i = 0; i < this.piece.data[rotation].length; i++) {
        for (let j = 0; j < this.piece.data[rotation][i].length; j++) {
          if (this.piece.data[rotation][i][j] && (!this.board[posY + i] || this.board[posY + i][posX + j]))
            return false;
        }
    }
    return true;
  }

  private checkDeleteLines() {
    this.points += 10;

    //En deleteLines tenemos las filas completas
    const deleteLines = this.piece.data[this.rotation]
      .map((_, i: number) => {
        return this.board[this.posY + i] && this.board[this.posY + i].find((x: any) => !x) === null
          ? -1
          : this.board[this.posY + i] && this.board[this.posY + i][1] != 'silver'
          ? this.posY + i
          : -1;
      })
      .filter((x: number) => x > -1);

    //Si hay lineas completas
    if (deleteLines.length) {
      this.status = 4;
      deleteLines.forEach((x) => {
        this.board[x] = this.board[x].map(
          (c: any) =>
            (c = c == 'silver' ? 'silver' : c == 'blue' ? 'gray' : 'blue')
        );
      });
      timer(0, 100)
        .pipe(
          take(10),
          finalize(() => {
            //cuando haya acabado la animación
            this.board = this.board.filter(
              (_, i) => !deleteLines.find((x) => x == i)
            );
            deleteLines.forEach((_) => {
              this.points += 90;
              this.board.unshift([...blankLine]);
            });
            this.points += 10 * deleteLines.length;

            this.status = 0;
            this.newPiece(); //creamos una nueva línea
          })
        )
        .subscribe((_) => {
          //hacemos una pequeña animación
          deleteLines.forEach((x) => {
            this.board[x] = this.board[x].map(
              (c: any) =>
                (c = c == 'silver' ? 'silver' : c == 'blue' ? 'gray' : 'blue')
            );
          });
        });
    } else this.newPiece(); //si no hay lineas para borrar también creamos una nueva pieza
  }

  private newPiece() {
    this.interval -= 10;
    if (this.interval < 100) this.interval = 100;

    this.piece = this.nextPiece;
    this.nextPiece =
      this.pieces[Math.floor(this.pieces.length * Math.random())];
    this.posX = 5+this.piece.posIni[0];
    this.posY = this.piece.posIni[1];
    this.rotation = 0;
    if (!this.check(this.rotation, this.posX, this.posY)) {
      this.sub && this.sub.unsubscribe();
      this.status = 2;
    } else {
      this.fillBoard();
      this.subscribe()
    }
  }

  private fillBoard() {
    this.piece.data[this.rotation].forEach((row: number[], i: number) => {
      row.forEach((x: number, j: number) => {
        if (x && this.board[this.posY + i]) this.board[this.posY + i][this.posX + j] = this.piece.color;
      });
    });
  }

  private removeBoard() {
    this.piece.data[this.rotation].forEach((row: number[], i: number) => {
      row.forEach((x: number, j: number) => {

        if (x && this.board[this.posY + i]) this.board[this.posY + i][this.posX + j] = null;
      });
    });
  }

  ngOnDestroy() {
    this.sub && this.sub.unsubscribe();
  }
}

bootstrapApplication(App);
