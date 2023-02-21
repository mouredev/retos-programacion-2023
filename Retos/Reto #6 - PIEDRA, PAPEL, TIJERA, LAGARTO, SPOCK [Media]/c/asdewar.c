#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef enum {
    piedra = 0,
    papel = 1,
    tijera = 2,
    lagarto = 3,
    spock = 4,
    NUM_ARMAS = 5
} Arma;

typedef struct {
    Arma arma;
    Arma vence_contra[2];
} Jugada;

// Array con todas las jugadas posibles.
Jugada todas_las_jugadas[NUM_ARMAS] = {
    {.arma = piedra,  .vence_contra = {lagarto, tijera}},
    {.arma = papel,   .vence_contra = {spock, piedra}},
    {.arma = tijera,  .vence_contra = {lagarto, papel}},
    {.arma = lagarto, .vence_contra = {papel, spock}},
    {.arma = spock,   .vence_contra = {piedra, tijera}}
};

// Convierte una cadena de texto a arma.
Arma convertir_cadena_a_arma(char *cadena) {
    if (strcasecmp(cadena, "\"🗿\"") == 0)
        return piedra;
    else if (strcasecmp(cadena, "\"📄\"") == 0)
        return papel;
    else if (strcasecmp(cadena, "\"✂️\"") == 0)
        return tijera;
    else if (strcasecmp(cadena, "\"🦎\"") == 0)
        return lagarto;
    else if (strcasecmp(cadena, "\"🖖\"") == 0)
        return spock;
    else
        return -1;
}

int main(int argc, char const *argv[])
{
    // Read line from user input.
    char *line = NULL;
    size_t malloc_size = 0, string_size = 0;
    printf("Introduce: ");
    string_size = getline(&line, &malloc_size, stdin) - 1;
    line[string_size--] = '\0';

    // Comprobar y borrar [].
    if (line[0] != '[' && line[string_size] != ']') {
        printf("Las jugadas deben estar dentro de [] -> %s\n", line);
        return 1;
    }
    line[string_size] = '\0';
    char *jugadas = line + 1;

    // Iterar por cada jugada.
    int puntuacion_jugadores[2] = {0};
    bool hay_resultado = true;
    while (true) {
        // Comprobar y borrar ().
        char *ultimo_parentesis = strchr(jugadas, ')');
        if (jugadas[0] != '(' || ultimo_parentesis == NULL) {
            printf("Mal formato de jugada () -> %s\n", jugadas);
            hay_resultado = false;
            break;
        }
        jugadas++;
        *ultimo_parentesis = '\0';
        // Coger primer y segundo string.
        char *primera_arma = jugadas;
        char *segunda_arma = strchr(jugadas, ',');
        if (segunda_arma == NULL) {
            printf("Mal formato de jugada, no hay contrincantes -> %s\n", jugadas);
            hay_resultado = false;
            break;
        }
        *segunda_arma = '\0';
        segunda_arma++;

        // Se convierte de string a arma.
        Arma arma_jugador_1 = convertir_cadena_a_arma(primera_arma);
        Arma arma_jugador_2 = convertir_cadena_a_arma(segunda_arma);
        printf("%d, %d\n", arma_jugador_1, arma_jugador_2);
        // Se comprueban ganadores.
        for (int i = 0; i < NUM_ARMAS; i++) {
            if(todas_las_jugadas[i].arma == arma_jugador_1) {
                Jugada *j = &todas_las_jugadas[i];
                // Se checkea si gana arma 1 o arma 2.
                if (arma_jugador_1 == arma_jugador_2) {
                    // No se hace nada, empate.
                    printf("Empate\n");
                } else if (arma_jugador_2 == j->vence_contra[0] || arma_jugador_2 == j->vence_contra[1]) {
                    printf("Gana 2\n");
                    puntuacion_jugadores[1]++;
                } else {
                    printf("Gana 1\n");
                    puntuacion_jugadores[0]++;
                }
                break;
            }
        }

        // Comprobar el final de la jugada.
        if (ultimo_parentesis[1] == ',' && ultimo_parentesis[2] == ' ') {
            jugadas = ultimo_parentesis + 3;
        } else if (ultimo_parentesis[1] == '\0') {
            break;
        } else {
            printf("Mal formato de jugada -> %s\n", jugadas);
            hay_resultado = false;
            break;
        }
    }

    // Si se ha llegado a algun resultado, se calcula.
    if (hay_resultado) {
        // Se imprimen los resultados.
        if (puntuacion_jugadores[0] ==  puntuacion_jugadores[1]) {
            printf("Tie\n");
        } else if (puntuacion_jugadores[0] > puntuacion_jugadores[1]) {
            printf("Player 1\n");
        } else {
            printf("Player 2\n");
        }
    }

    // Free line introduced by user.
    free(line);
    return 0;
}
