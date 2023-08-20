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
  <div class="wrapper-piece" >
  <div class="piece">
    <ng-container *ngFor="let row of nextPiece.data[rotation]">
      <div
        *ngFor="let cell of row"
        [style.border-width]="cell?1:0"
        [style.background-color]="cell && nextPiece.color"
      ></div>
    </ng-container>
  </div>
</div>
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
      margin: auto;
      padding-left: 10rem;
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
    .board *,
    .piece * {
      box-sizing: border-box;
    }
    .wrapper {
      position: relative;
      width: 18rem;
      margin: auto;
      overflow: hidden;
    }
    .board > div div {
      border: 1px solid silver;
      width: 1.5rem;
      height: 1.5rem;
      display: inline-block;
    }
    .board > div {
      height: 1.5rem;
    }
    .board .fill {
      background-color: silver;
    }
    .wrapper-piece {
      position: absolute;
      top: 1rem;
      left: 50%;
      margin-left: -17.5rem;
      z-index:1000;
    }
    .piece {
      position: absolute;
      z-index: -1;
      display: flex;
      width: 7.5rem;
      flex-wrap: wrap;
    }
    .piece div {
      border: 1px solid silver;
      width: 1.5rem;
      height: 1.5rem;
      display: inline-block;
    }
    .piece div.fill {
      background-color: red;
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

  btSubject: Subject<number[]> = new Subject<any>();

  ngOnInit() {
    //Todos los observables devuelven un array con los nuevos valores de [rotation,posX,posY]

    //Observable botones
    const buttons$ = this.btSubject as Observable<number[]>;

    //Observable teclado
    const keyboard$ = fromEvent(document, 'keydown').pipe(
      filter((x: any) => x.keyCode >= 37 && x.keyCode <= 40),
      map((x: any) => {
        const code = x.keyCode;
        if (code == 37) return [this.rotation, this.posX - 1, this.posY];
        if (code == 39) return [this.rotation, this.posX + 1, this.posY];
        if (code == 40) return [this.rotation, this.posX, this.posY + 1];
        const rotation = (this.rotation + 7) % 4;
        return [rotation, this.posX, this.posY];
      })
    );
    //Observable de tiempo
    const timer$ = timer(0, 100).pipe(
      filter(
        (_) =>
          this.interval == 0 ||
          new Date().getTime() - this.timeActual > this.interval
      ),
      map((_) => [this.rotation, this.posX, this.posY + 1]),
      tap((_) => {
        this.timeActual = new Date().getTime();
      })
    );
      
    //Un único observable que devuelve caso de que pase cualquiera de los tres casos anteriores
    this.control$ = merge(timer$, buttons$, keyboard$);
    
    //Iniciamos el juego
    setTimeout(() => {
      this.newGame();
    });
  }

  newGame() {
    this.board = emptyBoard.map((x) => [...x]);
  }

  startGame() {
    this.newPiece();
    this.status = 0;
    this.points = 0;
    this.interval = 1000;

    this.sub && this.sub.unsubscribe();
    this.timeActual = new Date().getTime();

    //Nos subscribimos al observable
    this.sub = this.control$.subscribe(
      ([rotation, posX, posY]: [number, number, number]) => {
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
    if (this.interval < 0) this.interval = 0;

    this.piece = this.nextPiece;
    this.nextPiece =
      this.pieces[Math.floor(this.pieces.length * Math.random())];
    this.posX = 5+this.piece.posIni[0];
    this.posY = this.piece.posIni[1];
    this.rotation = 0;
    console.log(this.check(this.rotation, this.posX, this.posY))
    if (!this.check(this.rotation, this.posX, this.posY)) {
      this.sub && this.sub.unsubscribe();
      this.status = 2;
    } else {
      this.fillBoard();
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
