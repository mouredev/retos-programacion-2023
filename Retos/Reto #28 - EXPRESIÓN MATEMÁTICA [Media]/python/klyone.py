#!/usr/bin/env python3

import re

def is_expr(expr):
    if re.fullmatch("\s*[+-]?\d+\.?\d*\s*([+-/*%]\s*[+-]?\d+\.?\d*\s*){0,}", expr) != None:
        return True
    return False

if __name__ == "__main__":
    print(is_expr("-4 + 5.8 % 0.3 - 4"))
    print(is_expr("5 + 6 / 7 - 4"))
    print(is_expr("4 a 6"))
