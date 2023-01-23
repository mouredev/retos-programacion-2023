#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int MIN_LENGTH = 8;
int MAX_LENGTH = 16;

int main(int argc, char *argv[]){

    static const char lower_case_letters[] = "abcdefghijklmnopqrstuvwxyz";
    static const char upper_case_letters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    static const char *numbers = "1234567890";
    static const char *symbols = "!$&()=~,.-;:_";

    char characters[80] = {};

    int length_characters = 0;

    int length_password = 0;

    int i, len;
    time_t t;

    if (argc == 1) {
        printf("\nUsage: %s num [OPTIONS] \n\n\
Get a multicharacter password (Default: lower case letters) \n\n\
- num: number of characters of the password. \n\n\
- OPTIONS: \n\
    U: Upper case letters \n\
    n: Numbers \n\
    s: Symbol s \n\
    ", argv[0]);
        exit(0);
    }

    len = atoi(argv[1]);

    length_password = (len >= MIN_LENGTH && len <= MAX_LENGTH) ? len : 0;

    if (length_password == 0) {
        printf("The password length must be %d and %d", MIN_LENGTH, MAX_LENGTH);
        exit(0);
    }

    strcat(characters, lower_case_letters);
    length_characters += strlen(lower_case_letters);;
    
    if (argc == 3) {

        if ( strchr(argv[2], 'U') != NULL ) {
            length_characters += strlen(upper_case_letters);;
            strcat(characters, upper_case_letters); 
        }
         
        if (strchr(argv[2], 'n') != NULL ) {
            length_characters += strlen(numbers);
            strcat(characters, numbers);
        }
        
        if (strchr(argv[2], 's') != NULL ) {
            length_characters += strlen(symbols);
            strcat(characters, symbols);        }
    }

    srand((unsigned) time(&t));

    printf("Password --> ");
    for (i=0; i < length_password; i++){
        printf("%c", characters[rand() % length_characters]);
    }   
}