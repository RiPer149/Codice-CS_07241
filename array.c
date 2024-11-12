#include <stdio.h>

int main()
{
    int numeri[3];
    numeri[0] = 1;
    numeri[1] = 4;
    numeri[2] = 89;
    printf("0x = %d\n", &numeri[2], numeri[2]);
    return 0;
}