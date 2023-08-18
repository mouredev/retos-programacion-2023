
let shape = [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
let pivot = [0, 0]

function rotate(shape) {
  let newShape = shape.map(elem => [...elem])
  newShape[0][0] = shape[0][2]
  newShape[0][1] = shape[1][2]
  newShape[0][2] = shape[2][2]
  newShape[1][0] = shape[0][1]
  newShape[1][2] = shape[2][1]
  newShape[2][0] = shape[0][0]
  newShape[2][1] = shape[1][0]
  newShape[2][2] = shape[2][0]
  return newShape;
}

const isLeftClear = (shape) =>  shape[0][0] === 0 && shape[1][0] === 0 && shape[2][0] === 0
const isRightClear = (shape) =>  shape[0][2] === 0 && shape[1][2] === 0 && shape[2][2] === 0
const isDownClear = (shape) =>  shape[2].every(cell => cell === 0)

function printBoard() {
  for(let i = 0; i < 10; i++) {
    let line = ''
    for(let h = 0; h < 10; h++) {
      if(i >= pivot[0] && i <= pivot[0] + 2 && h >= pivot[1] && h <= pivot[1] + 2) {
        if(shape[i - pivot[0]][h - pivot[1]] === 0) line += '⬜ '
        else if(shape[i - pivot[0]][h - pivot[1]] === 1) line += '🔳 '
      } else line += '⬜ '
    }
    console.log(line)
  }
}

printBoard()

window.addEventListener('keydown', (e) => {
  if(e.key === 'k' || e.key === 'a' || e.key === 'd' || e.key === 's' || e.key === 'r') {
    if(e.key === 'k') {
      shape = rotate(shape)
      if(pivot[1] >= 8 && !isRightClear(shape)) pivot[1] --
      if(pivot[1] < 0 && !isLeftClear(shape)) pivot[1] ++
      if(pivot[0] >= 8 && !isDownClear(shape)) pivot[0] --
    }
    if(e.key === 'a') (pivot[1] >= 1 || (pivot[1] === 0 && isLeftClear(shape))) && pivot[1]--;
    if(e.key === 'd') (pivot[1] < 7 || (pivot[1] === 7 && isRightClear(shape))) && pivot[1]++;
    if(e.key === 's') (pivot[0] < 7 || (pivot[0] === 7 && isDownClear(shape))) && pivot[0]++;
    if(e.key === 'r') pivot = [0, 0]
    console.clear()
    printBoard()
  }
})
