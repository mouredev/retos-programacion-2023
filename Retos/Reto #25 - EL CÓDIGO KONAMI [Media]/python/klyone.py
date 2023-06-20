#!/usr/bin/env python3

import sys
import tty
import os
import termios

def configure_stdin():
    stdin_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    return stdin_settings

def restore_stdin(stdin_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, stdin_settings)

def check_konami_code(key, partial_code):
    konami_code = ["up", "up", "down", "down", "left", "right", "left", "right"]

    partial_code.append(key)

    for i in range(len(partial_code)):
        if konami_code[i] != partial_code[i]:
            partial_code = []
            return [partial_code, False]

    if len(konami_code)-1 == i:
        found = True
    else:
        found = False

    return [partial_code, found]

def is_control_code(key):
    if len(key) == 3:
        return True
    else:
        return False

def read_key():

    arrow_keys = {
        65: "up",
        66: "down",
        67: "right",
        68: "left"
    }

    character = os.read(sys.stdin.fileno(), 3).decode()
    key_name = "Unknown"
    if is_control_code(character):
        character = ord(character[2])
        if character in arrow_keys:
            key_name = arrow_keys[character]
    else:
        character = ord(character)
        key_name = chr(character)

    return key_name

if __name__ == "__main__":

    settings = configure_stdin()
    partial_code = []

    while True:
        key = read_key()
        [partial_code, found] = check_konami_code(key, partial_code)
        if found:
            print("Congratullations: Konami code introduced!")
            break

    restore_stdin(settings)
