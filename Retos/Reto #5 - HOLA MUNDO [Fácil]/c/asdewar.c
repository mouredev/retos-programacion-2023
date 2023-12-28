#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

#define RESET_COLOR "\033[0;0m"

char *colors[] ={
    "\033[0;30m",
    "\033[0;31m",
    "\033[0;32m",
    "\033[0;33m",
    "\033[0;34m",
    "\033[0;35m",
    "\033[0;36m",
    "\033[0;37m"
};

char *get_random_color() {
    int num_colors = sizeof(colors) / sizeof(colors[0]);
    return colors[rand() % num_colors];
}

typedef struct {
    char letter_i_must_protect_above_my_live;
    pthread_mutex_t mutex_used_to_synchronize_my_live;
    pthread_t the_incredibly_thread_id;
} ThreadMostValuableInformation;

void *official_letter_printer(void *some_data_that_may_be_useful) {
    ThreadMostValuableInformation *info = (ThreadMostValuableInformation*) some_data_that_may_be_useful;

    if (pthread_mutex_lock(&info->mutex_used_to_synchronize_my_live)) {
        printf("GRAN FALLO EN EL PROTECTOR DE LA LETRA %c\n", info->letter_i_must_protect_above_my_live);
    }

    // Imprime la letra y ya.
    printf("%s%c", get_random_color(), info->letter_i_must_protect_above_my_live);
    fflush(stdout);

    return NULL;
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
    char *text_to_print = "Hello world mi panita, espero tengas una agradable estancia en este programa <3";
    int num_of_hello_world_threads = strlen(text_to_print);
    ThreadMostValuableInformation *incredibly_hello_world_thread_information = (ThreadMostValuableInformation*) malloc (sizeof(ThreadMostValuableInformation) * num_of_hello_world_threads);
    for (int i = 0; i < num_of_hello_world_threads; i++) {
        incredibly_hello_world_thread_information[i].letter_i_must_protect_above_my_live = text_to_print[i];
    }

    // Primero, crear cada protector letrado.
    for (int i = 0; i < num_of_hello_world_threads; i++) {
        ThreadMostValuableInformation *the_thread_data = &incredibly_hello_world_thread_information[i];
        if (pthread_mutex_init(&the_thread_data->mutex_used_to_synchronize_my_live, NULL)) {
            printf("FRACASO EN EL MUTEX DEL PROTECTOR %d\n", i);
            return 1;
        }
        if (pthread_mutex_lock(&the_thread_data->mutex_used_to_synchronize_my_live)) {
            printf("NA SI PA QUE\n");
        }
        if (pthread_create(&the_thread_data->the_incredibly_thread_id, NULL, official_letter_printer, the_thread_data)) {
            printf("FRACASO EN EL HILO DEL PROTECTOR %d\n", i);
            return 1;
        }
    }

    // Despues, la fantasia aparece.
    for (int i = 0; i < num_of_hello_world_threads; i++) {
        ThreadMostValuableInformation *the_thread_data = &incredibly_hello_world_thread_information[i];
        // Dormir más en espacios para dar apariencia.
        if (the_thread_data->letter_i_must_protect_above_my_live == ' ') {
            usleep(400000);
        } else {
            usleep(40000);
        }
        if (pthread_mutex_unlock(&the_thread_data->mutex_used_to_synchronize_my_live)) {
            printf("QUE DESGRACIA POR DIOS\n");
            return 1;
        }
        pthread_join(the_thread_data->the_incredibly_thread_id, NULL);
        pthread_mutex_destroy(&the_thread_data->mutex_used_to_synchronize_my_live);
    }

    free(incredibly_hello_world_thread_information);
    printf(RESET_COLOR "\n");
    return 0;
}
