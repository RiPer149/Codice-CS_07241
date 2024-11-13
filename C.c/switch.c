#include <stdio.h>

int main()
{
    int scelta;
    printf("\nPremi:\n1 per le nostre offerte\n2 per parlare con un operatore\n9 se non vuoi più ricevere i nostri servizi");
    scanf("%d", &scelta);
    switch(scelta)
    {
        case 1:
            printf("\nA soli 69.99 euro al mese avrà accesso alla nostra bacheca settimanale");
            break;
        case 2:
            printf("\nQuesta chiamata sarà gestita dall'India");
            break;
        case 3:
            printf("\nGrazie per aver chiamato");
            break;
        default:
            printf("Grazie Artur per averci contattato");
    }
    return 0;
}