import { stdout } from "node:process";

const BOARD_WIDTH = 10;
const BOARD_HEIGHT = 10;

type Actions = "derecha" | "izquierda" | "abajo" | "rotar";
type Board = Cell[][];
type Cell = "🔲" | "🔳";
type Piece = Point[];
type Point = [number, number];

const translateX = (point: Point, direction: "pos" | "neg"): Point => {
  if (direction === "pos") return [point[0] + 1, point[1]];
  if (direction === "neg") return [point[0] - 1, point[1]];
  return [...point];
};

const translateY = (point: Point): Point => [point[0], point[1] + 1];

const rotate90Degrees = (point: Point, rotationPoint: Point): Point => {
  const translatedPoint: Point = [
    point[0] - rotationPoint[0],
    point[1] - rotationPoint[1],
  ];

  const rotated90DegPoint: Point = [translatedPoint[1], -translatedPoint[0]];

  return [
    rotated90DegPoint[0] + rotationPoint[0],
    rotated90DegPoint[1] + rotationPoint[1],
  ];
};

const isValidPiece = (piece: Piece): boolean => {
  const flattenPiece = piece.flat();
  return flattenPiece.every((number) => number >= 0 && number <= 9);
};

const movePiece = (piece: Piece, action: Actions): Piece => {
  let newPiece: Piece = [];

  if (action === "derecha")
    newPiece = piece.map((point) => translateX(point, "pos"));

  if (action === "izquierda")
    newPiece = piece.map((point) => translateX(point, "neg"));

  if (action === "abajo") newPiece = piece.map((point) => translateY(point));

  if (action === "rotar") {
    const rotationPoint = piece[piece.length - 1];
    newPiece = piece.map((point) => rotate90Degrees(point, rotationPoint));
  }

  printBoard(isValidPiece(newPiece) ? newPiece : piece);
  return isValidPiece(newPiece) ? newPiece : piece;
};

const printBoard = (piece: Piece) => {
  const board: Board = Array(BOARD_HEIGHT)
    .fill([])
    .map(() => Array(BOARD_WIDTH).fill("🔲"));
  piece.forEach((point) => (board[point[1]][point[0]] = "🔳"));

  board.forEach((row) => {
    row.forEach((col) => stdout.write(col));
    stdout.write("\n");
  });
  stdout.write("\n");
};

let piece: Piece = [
  [0, 0],
  [0, 1],
  [1, 1],
  [2, 1],
];

printBoard(piece);
piece = movePiece(piece, "abajo");
piece = movePiece(piece, "abajo");
piece = movePiece(piece, "abajo");
piece = movePiece(piece, "abajo");
piece = movePiece(piece, "abajo");
piece = movePiece(piece, "derecha");
piece = movePiece(piece, "derecha");
piece = movePiece(piece, "derecha");
piece = movePiece(piece, "derecha");
piece = movePiece(piece, "rotar");
piece = movePiece(piece, "rotar");
piece = movePiece(piece, "rotar");
piece = movePiece(piece, "rotar");
