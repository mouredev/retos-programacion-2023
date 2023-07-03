# Reto #27: Cuenta atrás
#### Dificultad: Media | Publicación: 03/07/23 | Corrección: 10/07/23

## Enunciado

```
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
```

## Solución
Para esta solución implemente un comando, esto, para empezar a integrar los retos que vengan a futuro, de esta forma, ir actualizando mi centro de soluciones.

Es importante que la ejecución se haga donde se encuentre el archivo 'retos.exe', se creo así por mi SO que tengo; si se requiere un comando para linux/mac, solo hay que ejecutar el comando:
```bash
$ cargo build --release
```

En el sistema operativo que se requiera y se genera en la carpeta: ./target/releases/retos. En este caso, se renombro a mouredev por los requerimientos del PR, al crearlo, se puede usar como retos decrementar tiempo 10 2 o si se renombra como biene los comandos de abajo.

### Comandos
```bash
# Ayuda para comando principal
$ mouredev --help

# Ayuda para comando decrementar
$ mouredev decrementar --help

# Ayuda para subcomando de decrementar, en este caso tiempo
$ mouredev decrementar tiempo --help

# Ejecutar Reto 27
$ mouredev decrementar tiempo <comienza> <segundos>
$ mouredev decrementar tiempo 10 2
```

### Modo Desarrollo
```bash
# Ingresar a la carpeta code y ejecutar
$ cargo run -- --help

# Probar Decrementar
cargo run decrementar --help
cargo run decrementar tiempo --help
cargo run decrementar tiempo 10 2
```