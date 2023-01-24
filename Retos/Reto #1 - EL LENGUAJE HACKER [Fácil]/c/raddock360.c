#include <stdio.h>
#include <stdlib.h>

char const* alter[]= {
    "4", "8", "[", ")", "3", "|=", "&", "#", "1", ",_|", 
    ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "l2" , 
    "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2"   ,
};

int main(int argc, char* argv[]) {
    int letra = 0;

    printf("Introduce un texto:\n -> ");

    while((letra = getchar()) != EOF && letra != '\n') { 
        if(letra >= 65 && letra <= 90) {
            printf("%s", alter[letra - 65]);
        } else if(letra >= 97 && letra <= 122) {
            printf("%s", alter[letra - 97]);
        } else { printf("%c", letra); }        
    }
    printf("\n");

    return EXIT_SUCCESS;
}
