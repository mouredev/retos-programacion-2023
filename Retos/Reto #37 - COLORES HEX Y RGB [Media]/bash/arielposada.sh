#!/bin/bash


rgb_to_hex() {
    local r=$1
    local g=$2
    local b=$3
    printf "#%02x%02x%02x\n" "$r" "$g" "$b"
}


hex_to_rgb() {
    local hex=$1
    # Eliminar el símbolo '#' si está presente
    hex=${hex#\#}
    local r
    local g
    local b
    r=$((16#${hex:0:2}))
    g=$((16#${hex:2:2}))
    b=$((16#${hex:4:2}))
    echo "(r: $r, g: $g, b: $b)"
}

echo "Examples:"

echo "RGB to HEX (midnight blue):"
rgb_to_hex 25 25 112

echo "HEX to RGB (royal blue):"
hex_to_rgb "#4169E1"
