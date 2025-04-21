#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    srand(time(NULL));

    int aleatori = rand() % 100;

    printf("Nombre aleatori generat: %d\n", aleatori);

    return 0;
}