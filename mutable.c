#include <stdio.h>
int main()
{
    char L[10]="abcccba";
    L[2]='k';
    printf("%s",L); //output: abkccba
    return 0;
}