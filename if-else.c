#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;

    printf("\nInserisci primo numero: ");
    scanf("%d", &primo);

    printf("\nInserisci secondo numero: ");
    scanf("%d", &secondo);

    risultato = primo + secondo;
    if (secondo != 0)
    {
        printf("\n%d / %d = %d\n", primo, secondo, primo / secondo);
        printf("\n%d / %d ha resto %d\n", primo, secondo, primo % secondo);
    }
    else
    {
        printf("\nNon posso dividere per zero e non mi và di dimostrarti il perchè");
    }
    printf("\nHai appena sbloccato una gemma dell'infinito!!!");

    return 0;
}