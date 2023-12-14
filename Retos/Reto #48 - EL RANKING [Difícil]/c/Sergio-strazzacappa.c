/*
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas. 
 */

#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE (10000)
#define USERS (150000)


struct user
{
    char name[MAX_SIZE];
    int number_ex;
} user;


struct user users[USERS];
int cant_users = 0;
int cant_correcciones = 0;

char *root_name = "../../";
DIR *root;
struct dirent *root_entry;

char challenge_name[MAX_SIZE];
DIR *challenge;
struct dirent *challenge_entry;

char lang_name[MAX_SIZE];
DIR *lang;
struct dirent *lang_entry;

int check_dir(DIR* dir) {
    if (dir == NULL) {
        perror("Unable to read directory\n");
        return 1;
    }
    return 0;
}

void get_username(char* file, char* username) {
    strcpy(username, file);

    char *end = username + strlen(username);

    while (end > username && *end != '.') {
        --end;
    }

    if (end > username) {
        *end = '\0';
    }
    //printf("USER: %s\n", username);
}

void print_users() {
    printf("USERS: \n");
    for (int i = 0; i < cant_users; i++) {
        printf("[ %s, %d ]\n", users[i].name, users[i].number_ex);
    }
}

void add_user(char* username) {
    bool exist = false;
    for (int i = 0; i < cant_users; i++) {
        if (!strcmp(username, users[i].name)) {
            // El usuario ya existe
            users[i].number_ex++;
            exist = true;
            cant_correcciones++;
            break;
        }
    }
    if (!exist) {
        // El usuario no existe
        struct user u;
        strcpy(u.name, username);
        u.number_ex = 1;
        users[cant_users] = u;
        cant_users++;
        cant_correcciones++;
    }
}


int lang_dir() {
    strcpy(lang_name, challenge_name);
    strcat(lang_name, "/");
    lang = opendir(strcat(lang_name, challenge_entry->d_name));

    if (check_dir(lang)) {
        return 1;
    }

    while (lang_entry = readdir(lang)) {
        if (strcmp(lang_entry->d_name, ".") &&
            strcmp(lang_entry->d_name, "..") &&
            strcmp(lang_entry->d_name, "a.out") &&
            strcmp(lang_entry->d_name, "output.txt")) {
                //printf("%s\n", lang_entry->d_name);

                char username[MAX_SIZE] = "";
                get_username(lang_entry->d_name, username);
                add_user(username);
            }
    }
    closedir(lang);
}

int challenge_dir() {
    strcpy(challenge_name, root_name);
    challenge = opendir(strcat(challenge_name, root_entry->d_name));

    if (check_dir(challenge)) {
        return 1;
    }

    while (challenge_entry = readdir(challenge)) {
        if (strcmp(challenge_entry->d_name, ".") &&
            strcmp(challenge_entry->d_name, "..") &&
            strcmp(challenge_entry->d_name, "ejercicio.md")) {

            //printf("--- Lenguaje: %s ---\n", challenge_entry->d_name);
            lang_dir();
        }
    }
    closedir(challenge);
}

int root_dir() {
    root = opendir(root_name);

    if (check_dir(root)) {
        return 1;
    }

    while (root_entry = readdir(root)) {
        if (root_entry->d_name[0] == 'R') {
            //printf("*******************************************************\n");
            //printf("Entrando en %s\n", root_entry->d_name);
            //printf("*******************************************************\n");
            challenge_dir();
        }
    }
    closedir(root);
}

void swap(struct user* xp, struct user* yp) { 
    struct user temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
}

void sort_users() { 
    int i, j, min_idx; 

    for (i = 0; i < cant_users - 1; i++) {  
        min_idx = i; 
        for (j = i + 1; j < cant_users; j++) 
            if (users[j].number_ex > users[min_idx].number_ex) 
                min_idx = j;  
        swap(&users[min_idx], &users[i]); 
    } 
} 

int main() {
    root_dir();
    sort_users();
    print_users();
    printf("La cantidad de usuarios es: %d\n", cant_users);
    printf("La cantidad de correcciones es de: %d\n", cant_correcciones);

    return 0;
}