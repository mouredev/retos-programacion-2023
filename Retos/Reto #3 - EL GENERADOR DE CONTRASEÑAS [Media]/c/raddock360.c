/* 
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * ( Pudiendo combinar todos estos parámetros entre ellos )
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned char const letters[] = {
    // Normal letters 
    97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
    109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 
    120, 121, 122,
};

unsigned char const capital[] = {
    // Capital letters
    65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
    79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
};

unsigned char const symbols[] = {
    // From here to end symbols 
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 
    58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 
    124, 125, 126
};

unsigned char const numbers[] = {
    // Numbers 
    48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
};

// Password creation structure
typedef struct {
    unsigned char lenght;  // Password lenght [8 - 16]
    unsigned char options; // Options [ capital letters - numbers - symbols ]
    char password[16];     // Generated password
} T_Password;

/*
 * GET THE USER OPTIONS
 * INPUT: T_Password *p -> pointer to password structure
 * OUPUT: EXIT_FAILURE on error
 *        EXIT_SUCCESS on success
 */
int get_options(T_Password *p) {
    unsigned char op;

    printf("Configuring password:\n");
    printf("How many chars lenght?\n[8 - 16]-> ");
    scanf("%hhu", &p->lenght);
    if(p->lenght < 8 || p->lenght > 16) {
        printf("Incorrect password size.\n");
        return EXIT_FAILURE;
    }

    while(getchar() != '\n');
    printf("Do you want capital letters?\n[y/n]-> ");
    op = getchar();
    if(op == 'y' || op == 'Y') { p->options |= 0x04; }

    while(getchar() != '\n');
    printf("Do you want numbers?\n[y/n]-> ");
    op = getchar();
    if(op == 'y' || op == 'Y') { p->options |= 0x02; }

    while(getchar() != '\n');
    printf("Do you want symbols?\n[y/n]-> ");
    op = getchar();
    if(op == 'y' || op == 'Y') { p->options |= 0x01; }

    return EXIT_SUCCESS;
}

/*
 * GENERATES THE PASSWORD WITH THE USER OPTIONS PREVIOUSLY GIVEN
 * INPUT: T_Password *p -> pointer to password structure
 * OUPUT: EXIT_FAILURE on error
 *        EXIT_SUCCESS on success
 */
int pass_generator(T_Password *p) {
    srand(time(NULL));
    unsigned char x = 0;
    unsigned char random_number = 0;
    unsigned char created = 0;

    for(unsigned char i = 0; i < p->lenght; ++i) {
        random_number = 1 + rand() / (RAND_MAX / 4);
        created = 0;
        
        if(random_number == 1) {
            if(p->options & 0x04) {
                x = rand() / (RAND_MAX / sizeof(capital));
                p->password[i] = capital[x];
                created = 1;
            }
        } 
        if(random_number == 2) {
            if(p->options & 0x01) {
                x = rand() / (RAND_MAX / sizeof(symbols));
                p->password[i] = symbols[x];
                created = 1;
            }
        } 
        if(random_number == 3) {
            if(p->options & 0x02) {
                x = rand() / (RAND_MAX / sizeof(numbers));
                p->password[i] = numbers[x];
                created = 1;
            }
        } 
        if(random_number == 4 || !created){
            x = rand() / (RAND_MAX / sizeof(letters));
            p->password[i] = letters[x];
        }
    } 
    
    return EXIT_SUCCESS;
}

/* 
 * HERE IS WHERE THE MAGIC IS DONE
 */
int main(int argc, char *argv[]) {
    T_Password pass = {0};
    unsigned char error = 0;

    error = get_options(&pass);
    if(!error) { error = pass_generator(&pass); }
    if(!error) { printf("%s\n", pass.password); }

    if(!error) { return EXIT_SUCCESS; }
    else { return EXIT_FAILURE; }
}
