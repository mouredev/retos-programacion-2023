function generarContraseña({longitud,numbers,symbols,uppercase}) {

    if(!longitud>=8 && longitud<=16) return "Longitud incorrecta";


    let caracteres = "abcdefghijklmnopqrstuvwxyz";
    const mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numeros = "0123456789";
    const simbolos = "!@#$%^&*()_+-=[]{}|;':,./<>?";

   
    if(uppercase) caracteres += mayusculas;
    if(numbers) caracteres += numeros;
    if(symbols) caracteres += simbolos;

    let contraseña = "";

    for(let i=0;i<longitud;i++){
        contraseña += caracteres[Math.floor(Math.random() * caracteres.length)]
    }


    return contraseña;


}

console.log(generarContraseña({longitud:8,numbers:true,symbols:true,uppercase:true}))
console.log(generarContraseña({longitud:10,numbers:true,symbols:true,uppercase:false}))
console.log(generarContraseña({longitud:13,numbers:true,symbols:true,uppercase:false}))
console.log(generarContraseña({longitud:16,numbers:true,symbols:true,uppercase:false}))
console.log(generarContraseña({longitud:16,numbers:true,symbols:true,uppercase:false}))
console.log(generarContraseña({longitud:18,numbers:true,symbols:true,uppercase:true}))
