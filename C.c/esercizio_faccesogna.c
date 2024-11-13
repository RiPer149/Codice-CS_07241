#include <stdio.h>

int main()
{
    int num1, num2, somma;
    float media;
    printf("\nScrivi il primo numero ");
    scanf("%d", &num1);                      //Primo numero da inserire
    printf("\nScrivi il secondo numero ");
    scanf("%d", &num2);                     //Secondo numero da inserire

    somma = num1 + num2;
    printf("\nLa somma dei due numeri è: %d", somma);

    media = (float)somma / 2;
    printf("\nLa media sarà: %f", media);

    return 0;
}