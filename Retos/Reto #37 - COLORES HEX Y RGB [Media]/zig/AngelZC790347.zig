const std = @import("std");
pub fn main() !void {
    comptime var color = [_]u8{ 255, 3, 4 };
    comptime var hex = [_]u8{ 'F', 'F', '0', '3', '0', '4' };
    const res = try from_rgb_to_hex(color);
    const res_2 = try from_hex_to_rgb(hex);
    std.debug.print("#{s}\n", .{res});
    std.debug.print("{d}\n", .{res_2});
}
fn from_rgb_to_hex(rgb: [3]u8) ![6]u8 {
    const bufPrint = std.fmt.bufPrint;
    var hex: [6]u8 = undefined;
    var index: u8 = 0;
    for (rgb) |c| {
        var b: [2]u8 = undefined;
        var slices = try bufPrint(&b, "{X}", .{c});
        if (slices.len == 2) {
            hex[index] = b[0];
            hex[index + 1] = b[1];
        } else {
            hex[index] = 48; // 48 is 0 in ACII
            hex[index + 1] = b[0];
        }
        index += 2;
    }
    return hex;
}
fn from_hex_to_rgb(hex: [6]u8) ![3]u8 {
    var index: u8 = 0;
    var rgb: [3]u8 = [_]u8{ 0, 0, 0 };
    while (index < hex.len) : (index += 2) {
        // std.debug.print("{d}", .{hex[index]});
        rgb[index / 2] = (try std.fmt.charToDigit(hex[index], 16)) * 16 + (try std.fmt.charToDigit(hex[index + 1], 16));
    }
    return rgb;
}
