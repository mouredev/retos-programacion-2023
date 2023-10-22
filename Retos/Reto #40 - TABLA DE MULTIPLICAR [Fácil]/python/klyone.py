#!/usr/bin/env python3

def print_mult_table(n):
    for i in range(1, 11):
        print("{} x {} = {}\n".format(n,i,n*i))

if __name__ == "__main__":
    n = int(input("Number:"))
    print_mult_table(n)
