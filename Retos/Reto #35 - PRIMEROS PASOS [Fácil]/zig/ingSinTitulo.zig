const std = @import("std");

pub fn main() void {
    const stdout = std.io.getStdOut().writer();
    
    // Punto 1: Hola, mundo!
    try stdout.print("Hola, mundo!\n");

    // Punto 2: Crea una variable de texto o string
    const miTexto = "¡Hola desde Zig!\n";

    // Punto 3: Crea una variable de número entero
    const miEntero: i32 = 42;

    // Punto 4: Crea una variable de número con decimales
    const miDecimal: f64 = 3.14;

    // Punto 5: Crea una variable de tipo booleano
    const miBooleano: bool = true;

    // Punto 6: Crea una constante
    const MI_CONSTANTE: i32 = 10;

    // Punto 7: Usa un if, else if y else
    if (miEntero > 50) {
        try stdout.print("El número es mayor que 50\n");
    } else if (miEntero < 50) {
        try stdout.print("El número es menor que 50\n");
    } else {
        try stdout.print("El número es igual a 50\n");
    }

    // Punto 8: Crea un Array
    const miArray = []i32{1, 2, 3, 4, 5};

    // Punto 9: Crea una lista (slice en Zig)
    const miLista = []const u8{"Manzana", "Banana", "Naranja"};

    // Punto 10: Crea una tupla
    const miTupla = (1, "dos", 3.14);

    // Punto 11: Crea un set (no aplicable en Zig)

    // Punto 12: Crea un diccionario (hashmap en Zig)
    const HashMap = std.HashMap;
    var miDiccionario = HashMap(i32, []const u8).init(std.heap.page_allocator);
    _ = miDiccionario.put(1, "uno");
    _ = miDiccionario.put(2, "dos");

    // Punto 13: Usa un ciclo for
    for (miArray) |elemento| {
        try stdout.print("{}, ", .{elemento});
    }
    try stdout.print("\n");

    // Punto 14: Usa un ciclo foreach
    for (miLista) |elemento, index| {
        try stdout.print("Elemento {}: {}\n", .{index + 1, elemento});
    }

    // Punto 15: Usa un ciclo while
    var contador: i32 = 0;
    while (contador < 3) : (contador += 1) {
        try stdout.print("Contador: {}\n", .{contador});
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada
    fn funcionSinParametros() void {
        try stdout.print("Función sin parámetros\n");
    }
    funcionSinParametros();

    // Punto 17: Crea una función con parámetros que no retorne nada
    fn funcionConParametros(param1: i32, param2: []const u8) void {
        try stdout.print("Parámetro 1: {}\n", .{param1});
        try stdout.print("Parámetro 2: {}\n", .{param2});
    }
    funcionConParametros(1, "dos");

    // Punto 18: Crea una función con parámetros que retorne valor
    fn funcionConRetorno(a: i32, b: i32) i32 {
        return a + b;
    }
    const resultado = funcionConRetorno(3, 4);
    try stdout.print("Resultado: {}\n", .{resultado});

    // Punto 19: Crea una estructura (struct en Zig)
    const Persona = struct {
        nombre: []const u8,
        edad: i32,
    };
    const persona = Persona{ .nombre = "Juan", .edad = 30 };
    try stdout.print("Nombre: {}, Edad: {}\n", .{persona.nombre, persona.edad});

    // Punto 20: Muestra control de excepciones (try-catch en Zig)
    const resultadoDivision = dividir(10, 0);
    try resultadoDivision catch |error| {
        try stdout.print("Error: {}\n", .{error});
    }
}

// Punto 20: Muestra control de excepciones (try-catch en Zig)
fn dividir(dividendo: i32, divisor: i32) !i32 {
    if (divisor == 0) {
        return std.error.StackTrace("División por cero");
    }
    return dividendo / divisor;
}
