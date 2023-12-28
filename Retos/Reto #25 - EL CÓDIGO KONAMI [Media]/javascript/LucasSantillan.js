/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido
 * correctamente desde el teclado. 
 * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 * 
 * ESTE ES UN SCRIPT QUE DEBE INSERTARSE EN UN DOCUMENTO HTML
*/
let tecla = '';
let caracter = '';
document.write('<h1>Comienza a escribir, y haber si encuentras el código oculto:</h1><p id="escribir" style="font-size:24px;"></p>');

window.addEventListener("keydown", function(event) {
  tecla += event.which;
  if (tecla === '38' ||
      tecla === '3838' ||
      tecla === '383840' ||
      tecla === '38384040' ||
      tecla === '3838404037' ||
      tecla === '383840403739' ||
      tecla === '38384040373937' ||
      tecla === '3838404037393739' ||
      tecla === '383840403739373966' ||
      tecla === '38384040373937396665'
    ){
      if (tecla === '38384040373937396665')
        alert('¡Re Grox, has introducido el "Código Konami" 🥚');  
  } else {
    if ((event.which >= 48 && event.which <= 90) ||
        (event.which >= 96 && event.which <= 111) ||
        (event.which >= 186 && event.which <= 222) ||
        event.which == 32 || event.which == 226
    ){
      if((event.ctrlKey && event.altKey && event.which == 186) || (event.ctrlKey && event.altKey && event.which == 222)) {
        caracter += event.key;
      } else if (event.which != 186 && event.which != 222) {
        caracter += event.key;
      }
    }
    document.querySelector('#escribir').innerHTML = caracter;
    tecla = '';
  }
});
