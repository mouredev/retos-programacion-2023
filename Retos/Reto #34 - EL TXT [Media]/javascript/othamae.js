/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */


const fs = require('fs') 
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
const filePath = 'text.txt'

fs.access(filePath,fs.constants.F_OK, (err) =>{
    if (err){
       console.log('The file does not exist')
       console.log('Creating file...')
       createFile(filePath) 
    }
    else{
        updateFile(filePath)
    }

})


const createFile = (filePath) => {
    fs.writeFile(filePath, '', (err) =>{
        if (err) {
            console.log('Error creating file')
        }        
        console.log('File created')    
        editFile(filePath)    
    })
}

const readFile = (filePath) => {
    const data = fs.readFileSync(filePath, 'utf8')
    console.log(data)
}

const updateFile = (filePath) => {
    console.log('File content: \n')
    readFile(filePath)
    rl.question('Select what you want to do? (e/w) \n e: Add content to the file \n w: Delete existing content and write new content \n c: Cancel \n', (answer) => {
        answer === 'c' ? rl.close():
        answer !== 'e' && answer !== 'w' ? (console.log('Invalid answer'), updateFile(filePath)):
        answer === 'e' ? editFile(filePath) : changeContent(filePath)
    })
    
}

const editFile = (filePath) => {        
    rl.question('What do you want to add in the file? \n', (answer) => {
        fs.appendFile(filePath, answer + '\n', (err) =>{
            if (err) {
                console.log('Error editing file')
            }
            console.log('File edited, this is the new content: \n')
            readFile(filePath)     
            rl.close()   
        })
    })
        
                   
}

const changeContent = (filePath) => {
    rl.question('What do you want to write in the file? \n', (answer) => {
        fs.writeFile(filePath, answer + '\n', (err) =>{
            if (err) {
                console.log('Error changing content')
            }
            console.log('New content: \n')
            readFile(filePath)  
             rl.close()     
        })
    }
    )
    

}