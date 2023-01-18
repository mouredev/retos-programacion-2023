import { gameApp } from './src/game-app'
import './style.css'


document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://github.com/webferrol/retos-programacion-2023/blob/main/Retos/Reto%20%232%20-%20EL%20PARTIDO%20DE%20TENIS%20%5BMedia%5D/ejercicio.md" target="_blank">
      Partido de tenis
    </a>
    <h1>El partido de tenis</h1>
    <div class="card">
      <button id="counter" type="button">Punto</button>
    </div>
    <div data-id="root">
      Click on the Vite logo to learn more
    </div>
  </div>
`

gameApp(document.querySelector('[data-id=root]'));


