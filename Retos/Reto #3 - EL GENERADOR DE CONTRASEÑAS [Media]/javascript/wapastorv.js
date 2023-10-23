function generarContrasena(longitud){

    const caracteres = [
        ...Array.from({ length: 26 }, (_, i) => String.fromCharCode(65 + i)), // Mayúsculas A-Z
        ...Array.from({ length: 26 }, (_, i) => String.fromCharCode(97 + i)), // Minúsculas a-z
        ...Array.from({ length: 10 }, (_, i) => String(i)), // Números 0-9
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?', '`', '~'
      ];

    let contrasena ='';

    const caracteresLen = caracteres.length;

    if (longitud < 8 || longitud > 16) {
        console.error('La longitud de la contraseña debe estar entre 8 y 16 caracteres.');
        return null;
      }

    // for(let i= 0; i< caracteres.length; i++){
    //      const contrasenaAleatoria = caracteres[Math.floor(Math.random() * caracteres.length)];
    //      contrasena += contrasenaAleatoria
              
    // }
    // console.log(contrasena);  

    for (let i = 0; i < longitud; i++) {
        const caracterAleatorio = caracteres[Math.floor(Math.random() * caracteresLen)];
        contrasena += caracterAleatorio;
      }
      return contrasena;
 } 


const longitudAleatoria = Math.floor(Math.random() * 9) + 8;
const contrasenaGenerada = generarContrasena(longitudAleatoria);

if (contrasenaGenerada) {
  console.log(`Contraseña generada: ${contrasenaGenerada}`);
}



