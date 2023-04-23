#include <stdio.h>
#include <string.h>

int main(){
string name;

        name = puts("What is your  name? ");
    scanf("%s", &name);
    int n = 0;
    while (name[n] != "\0") n++;

    printf("%i", n);

return 0;
}
