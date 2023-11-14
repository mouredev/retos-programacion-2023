/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - 💚Si no existe, debe crear un fichero llamado "text.txt".
 * - 💚Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - 💚Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - 💚Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */

const fs = require('fs')
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
//Leer archivo
const Read = () =>{
    fs.readFile('text.txt','utf-8', (err,data) => {
        if (err){
            console.error(err)
        }else{
            console.log(data)
        }
        
    })
}

//Crear archivo de texto
const Create = (texto) =>{
    fs.writeFile('text.txt',`${texto}\n`, (err) =>{
        if(err) throw err
        console.log('Se creo archivo')
    })
}
//Añadir texto a archivo existente
const Add = (newTexto) =>{
    fs.appendFile('text.txt',`${newTexto}\n`, (err) =>{
        if (err) throw err
        console.log('Se agrego texto')
    })
}
//Eliminar archivo
const Delete = () =>{
    fs.unlink('text.txt', (err) => {
        if(err) throw err
    })
    return 'archivo eliminado'
}


//Comprobar si esta creado el archivo
fs.access('text.txt', fs.constants.F_OK, (err)=>{
    //si no existe archivo, se crea uno nuevo
    if(err){
        rl.question('Ingrese texto: ',(texto) =>{

            Create(texto)

            rl.close()
        })

    }
    else{
        //si ya existe se agrega mas texto o se elimina
        rl.question('El archivo ya existe, desea agregar(1) o eliminar(2): ',(option) =>{

            if(option==='1'){
                Read()
                rl.question('Ingrese texto para agregar: ',(texto) =>{

                    Add(texto)
        
                    rl.close()
                })
                

            }
            else if(option==='2'){
                const textdeleted = Delete()
                console.log(textdeleted)
                rl.question('Ingrese texto para el nuevo archivo: ',(texto) =>{

                Create(texto)
        
                rl.close()
                })
            }else{
                console.log('Opcion no valida')
                rl.close()
            }
        })
    }
})

