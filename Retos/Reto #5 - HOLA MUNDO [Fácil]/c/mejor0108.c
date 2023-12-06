/****************************************************
 *
 *  Program: mejor0108.c
 *  Compile: gcc mejor0108.c -o mejor0108
 *
 * ****************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const char *msg = "\tHola Mundo, I love programming!\n";
const char *msg2 = "\tSencillo y lindo\n";

int main() {
    write(1, msg, strlen(msg));
    write(1, msg2, strlen(msg2));
    exit(0);
}
