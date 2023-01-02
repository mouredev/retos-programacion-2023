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