#include <stdio.h>

int main()
{
    int numero1, numero2, somma;
    float media;
    printf("\nScrivi il primo numero ");
    scanf("%d", &numero1);                   // Primo numero da inserire
    printf("\nScrivi il secondo numero ");
    scanf("%d", &numero2);                  // Secondo numero da inserire

    somma = numero1 + numero2;
    printf("\nLa somma dei due numeri è: %d", somma);

    media = (float)somma / 2;
    printf("\nLa media sarà: %f", media);

    return 0;
}