import { writeFile, readFile, access, constants } from 'fs/promises'
import * as readline from 'node:readline/promises'
import { stdin as input, stdout as output } from 'node:process'

const rl = readline.createInterface({ input, output })
const path = './files/text.txt'

/* ingresa una nueva linea en el archivo, o borra el contenido previo e ingresa la nueva linea */
function writeFileLine(path, data, mode) {
  writeFile(path, data + '\n', { encoding: 'utf-8', flag: mode })
    .then(() => console.log('new line writed succesfully, awaiting for another line...'))
    .catch(err => console.log(`error writing new line! : ${err}`))
}

/* verifica la existencia del archivo y de los permisos de lectura y escritura */
function existsFile(path) {
  return new Promise(async(res) => {
    await access(path, constants.R_OK && constants.W_OK) 
      .then(() => res(true))
      .catch(() => res(false))
  })
}

/* obtiene el contenido del archivo */
async function getFileContent(path) {
  try {
    return await readFile(path, { encoding: 'utf-8' })
  } catch (err) {
    console.log('error reading file content')
  }
}

console.log('Write a new line for the file...')

/* al recibir una nueva linea por consola */
rl.on('line', async(input) => {
  console.clear()
  const exists = await existsFile(path)
  if(exists) {
    let answer;
    do {
      console.clear()
      answer = await rl.question('file already exists, do you want to append the new line? (y/n)')
    } while(answer !== 'y' && answer !== 'n')
    console.clear()
    if(answer === 'y') {
      console.log('previous content:')
      let content = await getFileContent(path)
      content = content.split('\n')
      content.forEach(line => console.log(line))
      writeFileLine(path, input, 'a+')
    }
    if(answer === 'n') {
      console.log('previous content deleted!\n')
      writeFileLine(path, input, 'w')
    }
  } else writeFileLine(path, input, 'w')
})