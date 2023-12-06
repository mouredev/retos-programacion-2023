function generarContrasena(longitud, mayusculas = true, numeros = true, simbolos = true) {
    let cadena = 'abcdefghijklmnopqrstuvwxyz';
    if (mayusculas) cadena += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (numeros) cadena += '0123456789';
    if (simbolos) cadena += '!@#$%^&*()_-+=[]{};:,./?';
  
    if (longitud < 8 || longitud > 16) {
      throw new Error("La longitud debe estar entre 8 y 16.");
    }
  
    let pwd = '';
    for (let i = 0; i < longitud; i++) {
      const indiceAleatorio = Math.floor(Math.random() * cadena.length);
      pwd += cadena.charAt(indiceAleatorio);
    }
    return pwd;
  }
  
  function obtenerEntradaUsuario(pregunta) {
    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });
  
    return new Promise((resolve) => {
      readline.question(pregunta, (respuesta) => {
        readline.close();
        resolve(respuesta);
      });
    });
  }
  
  async function main() {
    try {
      const longitud = parseInt(await obtenerEntradaUsuario("Ingrese la longitud deseada para la contraseña (entre 8 y 16): "));
      const mayusculas = (await obtenerEntradaUsuario("Incluir letras mayúsculas? (Sí/No): ")).trim().toLowerCase() === 'si';
      const numeros = (await obtenerEntradaUsuario("Incluir números? (Sí/No): ")).trim().toLowerCase() === 'si';
      const simbolos = (await obtenerEntradaUsuario("Incluir símbolos? (Sí/No): ")).trim().toLowerCase() === 'si';
  
      const contrasenaGenerada = generarContrasena(longitud, mayusculas, numeros, simbolos);
      console.log("Contraseña generada:", contrasenaGenerada);
    } catch (error) {
      console.log("Error:", error.message);
    }
  }
  
  main()