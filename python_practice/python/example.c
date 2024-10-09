#include <stdio.h>

int main()
{
    char buffer[64];
    gets(buffer);
    printf("You entered: %s\n", buffer);
    return 0;
}