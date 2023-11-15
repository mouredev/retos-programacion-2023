#include <stdio.h>

struct vector
{
    float coordenada[2];
    float velocidad[2];
};
void rellenarVector(struct vector *p)
{
    int i;
    for (i = 0; i < 2; i++)
    {
        printf("Datos iniciales Vector #%d: \n", i + 1);
        printf("En [m]... \n");
        printf("Ingrese Xi: ");
        scanf("%f", &((p + i)->coordenada[0]));
        printf("Ingrese Yi: ");
        scanf("%f", &((p + i)->coordenada[1]));
        printf("En [m/s]... \n");
        printf("Ingrese Vxi: ");
        scanf("%f", &((p + i)->velocidad[0]));
        printf("Ingrese Vyi: ");
        scanf("%f", &((p + i)->velocidad[1]));
    }
}

float colision(struct vector *p, float *px, float *py)
{
    float vx, vy;
    float posx, posy;
    float tiempox, tiempoy, tiempo;

    vx = (p + 0)->velocidad[0] - (p + 1)->velocidad[0];
    vy = (p + 0)->velocidad[1] - (p + 1)->velocidad[1];
    posx = (p + 1)->coordenada[0] - (p + 0)->coordenada[0];
    posy = (p + 1)->coordenada[1] - (p + 0)->coordenada[1];

    if (vx != 0 && vy != 0)
    {
        tiempox = posx / vx;
        tiempoy = posy / vy;
        if (tiempox == tiempoy)
        {
            *px = (p + 0)->coordenada[0] + ((p + 0)->velocidad[0] * tiempox);
            *py = (p + 0)->coordenada[1] + ((p + 0)->velocidad[1] * tiempoy);

            tiempo = tiempox;
        }
        else
        {
            tiempo = -1;
        }
    }
    else
    {
        tiempo = -1;
    }

    return tiempo;
}

int main(void)
{
    struct vector v[2];
    float px, py, t;

    rellenarVector(v);
    printf("\n");

    t = colision(v, &px, &py);
    if (t >= 0)
    {
        printf("Los vectores colisionan en [%.2f,%.2f] a los %.2f segundos\n", px, py, t);
    }
    else
    {
        printf("Los vectores no colisionan\n");
    }

    return 0;
}