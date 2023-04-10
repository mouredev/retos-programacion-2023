#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int convert_octal(int num);
char* convert_hexa(int num);

int main(){
    int num;
    puts("Give me a decimal number:");
    scanf("%i", &num);
    
    printf("Octal: %i\n", convert_octal(num));
    printf("Hexadecimal: %s\n", convert_hexa(num));

    return 0;
}

int convert_octal(int num){
    int aux=0, i=1;
    while(num !=0){
        aux += (num % 8) * i;
        num /= 8;
        i *= 10;
    }
    return aux;
}

char* convert_hexa(int num){
    int aux=0, i=0;
    char *hexa=NULL;
    while(num != 0){
        aux = num % 16;
        num /= 16;
        hexa = (char*) realloc(hexa, (i+1) * sizeof(char));
        if (aux <= 9 && aux >= 0){
            hexa[i] = aux + '0'; 
        }else{
            hexa[i] = aux - 10 + 'A';
        }
        i++;
    }
    hexa[i] = '\0'; 
    int j, k;
    char temp;
    //Change of order
    for (j = 0, k = i - 1; j < k; j++, k--){
        temp = hexa[j];
        hexa[j] = hexa[k];
        hexa[k] = temp;
    }
    return hexa;
}
