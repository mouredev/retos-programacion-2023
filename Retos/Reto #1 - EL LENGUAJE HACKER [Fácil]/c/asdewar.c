#include <stdio.h>
#include <stdbool.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <curl/curl.h>


// Estructura que contiene una letra en alfabeto normal y su conversión a leet.
typedef struct {
    char normal_letter;
    char leet_letter[5];
} LeetLetter;

// Array con todas las letras y su conversión al alfabeto leet.
LeetLetter leet_alphabet[] = {
    {'A', "4"},
    {'B', "I3"},
    {'C', "["},
    {'D', ")"},
    {'E', "3"},
    {'F', "|="},
    {'G', "&"},
    {'H', "#"},
    {'I', "|"},
    {'J', ",_|"},
    {'K', ">|"},
    {'L', "|_"},
    {'M', "/\\/\\"},
    {'N', "^/"},
    {'O', "0"},
    {'P', "|*"},
    {'Q', "(_,)"},
    {'R', "I2"},
    {'S', "5"},
    {'T', "7"},
    {'U', "(_)"},
    {'V', "\\/"},
    {'W', "\\/\\/"},
    {'X', "><"},
    {'Y', "j"},
    {'Z', "2"},
    {'0', "o"},
    {'1', "L"},
    {'2', "R"},
    {'3', "E"},
    {'4', "A"},
    {'5', "S"},
    {'6', "b"},
    {'7', "T"},
    {'8', "B"},
    {'9', "g"}};

/*
    Primera solución: se genera un hilo por cada letra que tiene conversión, cada hilo se encarga de responder por su letra de la que se encarga.
    El hilo principal crea todos los hilos (uno por letra) y va iterando el string preguntando a los hilos quien tiene la conversión del caracter en lectura.
    Para el texto A2J, responderían los 3 hilos correspondientes en orden, el de la A, el de la 2 y el de la J.
    Cabe destacar que esta versión es mega-ultra-hiper-ineficiente, tener 35 hilos corriendo a la vez genera muchas interrupciones.
    Este problema se podría resolver con mutex, pero tampoco tiene mucho sentido.
*/
// Tiempo máximo que el hilo principal espera a una solución de un hilo (en segundos).
#define MAX_ELAPSED_TIME 2

// Este puntero apuntará al caracter en formato normal que se quiere convertir.
char normal_letter_to_convert;
// Este puntero apuntará al caracter en formato leet que se acaba de convertir.
char *leet_letter_converted;

// Flag que indica que la conversion de un caracter ha finalizado.
bool character_conversion_finished;
// Flag que indicará a los threads cuando ha acabado la conversión.
bool converter_running;

// Función del hilo que ENCARGADO de buscar y responder por la letra pasada por parámetro.
void *leet_searcher(void *leet_letter_pointer) {
    // Get the leet letter struct passed by param.
    LeetLetter *leet_letter = (LeetLetter *)leet_letter_pointer;
    // Mientras no se llegue al final de la conversión.
    while (converter_running) {
        // Se checkea que el caracter del que se encarga el hilo es el buscado.
        if (tolower(normal_letter_to_convert) == tolower(leet_letter->normal_letter)) {
            // Se guarda el caracter convertido.
            leet_letter_converted = leet_letter->leet_letter;
            // Se resetea el caracter a convertir.
            normal_letter_to_convert = '\0';
            // Se activa el flag de caracter convertido.
            character_conversion_finished = true;
        }
    }
    return NULL;
}

// Hilo principal del conversor.
void thread_converter(char *string_to_convert, int string_size) {
    // Se obtiene el número de caracteres que se pueden convertir.
    int leet_alphabet_size = sizeof(leet_alphabet) / sizeof(LeetLetter);
    // Array con cada id de cada hilo creado (uno por cada LeetLetter).
    pthread_t *tids = (pthread_t *)malloc(leet_alphabet_size * sizeof(pthread_t));

    // Se activa el flag de conversor corriendo.
    converter_running = true;

    // Se itera por cada letra del alfabeto.
    int th_i;
    for (th_i = 0; th_i < leet_alphabet_size; th_i++) {
        // Se crea el hilo.
        if (pthread_create(&tids[th_i], NULL, leet_searcher, &leet_alphabet[th_i])) {
            fprintf(stderr, "Fallo en la inicialización del hilo %d\n", th_i);
            th_i--;
            break;
        }
    }
    // Se comrpueba que todos los hilos se han inicializado.
    if (th_i == leet_alphabet_size) {
        // Iterar por cada caracter de string.
        for (int i = 0; i < string_size; i++) {
            // Se activa el conversor.
            normal_letter_to_convert = string_to_convert[i];
            // Se espera a que alguien tenga un resultado.
            double started_time = clock();
            while (!character_conversion_finished) {
                // Si se ha llegado al max tiempo, se sale del bucle.
                if ((clock() - started_time) >= (MAX_ELAPSED_TIME * CLOCKS_PER_SEC)) {
                    break;
                }
            }
            // Se imprime el resultado por pantalla. Si no se ha resuelto, se imprime la letra sin convertir.
            if (character_conversion_finished) {
                printf("%s", leet_letter_converted);
            } else {
                printf("%c", normal_letter_to_convert);
            }
            // Se resetea la conversión para pasar a la siguiente iteración.
            character_conversion_finished = false;
        }
        // Se imprime salto de línea para que quede más vistoso.
        printf("\n");
    }

    // Se activa el flag de finalización.
    converter_running = false;
    // Se espera a cada hilo.
    for (int j = 0; j < th_i; j++) {
        pthread_join(tids[j], NULL);
    }
    // Se libera el array de ids de los threads reservados.
    free(tids);
}

/*
    Segunda solución: la solución simple (y eficaz), itera por el alfabeto creado arriba, y si la letra coincide, imprime el carácter que corresponde.
*/
void normal_converter(char *string_to_convert, int string_size) {
    // Se obtiene el número de caracteres que se pueden convertir.
    int leet_alphabet_size = sizeof(leet_alphabet) / sizeof(LeetLetter);
    // Se itera por cada caracter del string.
    for (int i = 0; i < string_size; i++) {
        // Se itera por cada letra del alfabeto.
        int j;
        for (j = 0; j < leet_alphabet_size; j++) {
            if (tolower(string_to_convert[i]) == tolower(leet_alphabet[j].normal_letter)) {
                printf("%s", leet_alphabet[j].leet_letter);
                break;
            }
        }
        // Se comprueba que esté dentro del alfabeto.
        if (j == leet_alphabet_size) {
            printf("%c", string_to_convert[i]);
        }
    }
    printf("\n");
}

/*
    Tercera solución: esta solución hace una request a la api the api.funtranslations.com e imprime el resultado.
*/
#define URL_API_PATTERN_START "translated\": \""
#define URL_API_PATTERN_END   "\""

// Esta función recibe como parámetro el buffer de datos 
size_t url_handler(char *buffer, size_t size, size_t nitems, void *userdata) {
    // printf("Len: %ld, %ld, %ld, \n%s\n", size, nitems, strlen(buffer), buffer);
    // Buscar el patron del inicio del string.
    char *start_str = strstr(buffer, URL_API_PATTERN_START);
    if (start_str == NULL) {
        printf("Cannot get start pattern from API response\n");
    } else {
        // Buscar el patron del final del string.
        start_str += strlen(URL_API_PATTERN_START);
        char *end_str = strstr(start_str, URL_API_PATTERN_END);
        if (end_str == NULL) {
            printf("Cannot get end pattern from API response\n");
        } else {
            // Imprime el string recogido de la URI.
            end_str += strlen(URL_API_PATTERN_END) - 1;
            *end_str = '\0';
            printf("%s\n", start_str);
        }
    }
    // Se debe retornar el tamaño de la response.
    return size * nitems;
}

// Función principal de la tercera solución, que hace una petición a una API.
void api_converter(char *string_to_convert, int string_size) {
    // Primero montamos la url.
    char url[2000] = "https://api.funtranslations.com/translate/leetspeak.json?text=";
    for (int i = 0, j = strlen(url); i < string_size; i++, j++) {
        char c = string_to_convert[i];
        if (c == ' ') {
            url[j++] = '%';
            url[j++] = '2';
            url[j] = '0';
        } else {
            url[j] = c;
        }
    }

    // Creamos las variables necesarias para la API.
    CURL *curl;
    CURLcode res;
    curl = curl_easy_init();
    if(curl) {
        // Se cambian las opciones de la APi para que sea URL y tenga un url handler.
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, url_handler);

        // Se ejecuta la petición.    
        res = curl_easy_perform(curl);

        // Control de errores.
        if(res != CURLE_OK) {
            fprintf(stderr, "Fallo en la petición, error: %s\n", curl_easy_strerror(res));
        }

        /* always cleanup */
        curl_easy_cleanup(curl);
    }
}

// Para compilar el programa:
int main() {
    // Puntero al string para convertir.
    char *string_to_convert = NULL;
    // Variables para la longitud del string leido.
    size_t len = 0;
    ssize_t lineSize = 0;
    // Se lee la línea.
    printf("Introduce la línea que quieras convertir a leet: ");
    lineSize = getline(&string_to_convert, &len, stdin);
    // Se le resta uno al line size para omitir el \n del final.
    lineSize--;

    // Variables para el cálculo de tiempo.
    clock_t t;
    double time_taken;

    // Primera solución. Con calculo del tiempo.
    t = clock();
    thread_converter(string_to_convert, lineSize);
    t = clock() - t;
    time_taken = ((double)t) / CLOCKS_PER_SEC; // calculate the elapsed time
    printf("Primera versión ha tardado %f segundos\n", time_taken);

    // Segunda solución. Con calculo del tiempo.
    t = clock();
    normal_converter(string_to_convert, lineSize);
    t = clock() - t;
    time_taken = ((double)t) / CLOCKS_PER_SEC; // calculate the elapsed time
    printf("Segunda versión ha tardado %f segundos\n", time_taken);

    // Tercera solución. Con calculo del tiempo.
    t = clock();
    api_converter(string_to_convert, lineSize);
    t = clock() - t;
    time_taken = ((double)t) / CLOCKS_PER_SEC; // calculate the elapsed time
    printf("Tercera versión ha tardado %f segundos\n", time_taken);

    // Se libera la línea.
    free(string_to_convert);
}
