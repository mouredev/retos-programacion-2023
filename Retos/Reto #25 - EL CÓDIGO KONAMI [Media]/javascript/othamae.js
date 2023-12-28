/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

// ↑ ↑ ↓ ↓ ← → ← → B A

const readline = require('readline')

const KonamiCode = ['u', 'u', 'd', 'd', 'l', 'r', 'l', 'r', 'b', 'a']

const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
    
rl.on('line', (input) => {
        let inputCode = input.trim()
        let code =inputCode.split('')
        if(code.length >= KonamiCode.length){
            if (code.join('') === KonamiCode.join('')){
                console.log('Konami code has been entered correctly')
                rl.close()
            }
        }        
         
    })


    


      
     
    


