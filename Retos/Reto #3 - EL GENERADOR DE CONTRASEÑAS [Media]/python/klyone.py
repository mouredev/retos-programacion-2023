#!/usr/bin/env python3

import random

class PasswordConfig:
    def __init__(self, size=8, allowed_mayus=False, allowed_numbers=False, allowed_symbols=False):
        if size < 8 or size > 16:
            raise Exception("Error: Size should be inside the range [8,16]")

        self.size = size
        self.allowed_chars = "abcdefghijklmnopqrstuvwxyz"
        if allowed_mayus:
            self.allowed_chars = self.allowed_chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if allowed_numbers:
            self.allowed_chars = self.allowed_chars + "1234567890"
        if allowed_symbols:
            self.allowed_chars = self.allowed_chars + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~."

    def get_password_size(self):
        return self.size
    def get_allowed_chars(self):
        return self.allowed_chars

def generate_password(password_config=PasswordConfig()):
    size = password_config.get_password_size()
    allowed_chars = password_config.get_allowed_chars()
    passwd = ""
    random.seed()

    for i in range(0,size):
        passwd = passwd + random.choice(allowed_chars)
    return passwd

if __name__ == "__main__":
    print(generate_password())
    print(generate_password(PasswordConfig(size=13)))
    print(generate_password(PasswordConfig(allowed_mayus=True)))
    print(generate_password(PasswordConfig(allowed_numbers=True)))
    print(generate_password(PasswordConfig(allowed_symbols=True)))
    print(generate_password(PasswordConfig(size=14, allowed_mayus=True, allowed_numbers=True, allowed_symbols=True)))
