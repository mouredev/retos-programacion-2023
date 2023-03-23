// Zig is a general-purpose programming language and toolchain for maintaining robust, optimal and reusable software.

// ⚡ A Simple Language
// Focus on debugging your application rather than debugging your programming language knowledge.
// No hidden control flow.
// No hidden memory allocations.
// No preprocessor, no macros.

// ⚡ Comptime
// A fresh approach to metaprogramming based on compile-time code execution and lazy evaluation.
// Call any function at compile-time.
// Manipulate types as values without runtime overhead.
// Comptime emulates the target architecture.

// ⚡ Maintain it with Zig
// Incrementally improve your C/C++/Zig codebase.
// Use Zig as a zero-dependency, drop-in C/C++ compiler that supports cross-compilation out-of-the-box.
// Leverage zig build to create a consistent development environment across all platforms.
// Add a Zig compilation unit to C/C++ projects; cross-language LTO is enabled by default.

// # --------------------------------------------------------------------- #
// Reto #0: EL FAMOSO "FIZZ BUZZ"
// Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
//
// Escribe un programa que muestre por consola (con un print) los
// números de 1 a 100 (ambos incluidos y con un salto de línea entre
// cada impresión), sustituyendo los siguientes:
// - Múltiplos de 3 por la palabra "fizz".
// - Múltiplos de 5 por la palabra "buzz".
// - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
// # --------------------------------------------------------------------- #


const std = @import("std");

fn main() !void {
    var i: u32 = 1;
    while (i <= 100) {
        if (i % 15 == 0) {
            std.debug.warn("FizzBuzz\n");
        } else if (i % 3 == 0) {
            std.debug.warn("Fizz\n");
        } else if (i % 5 == 0) {
            std.debug.warn("Buzz\n");
        } else {
            std.debug.warn("%d\n", i);
        }
        i += 1;
    }
}