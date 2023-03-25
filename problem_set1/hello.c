#include "cs50.h"
#include <stdio.h>

int main()
{
    //Taking input for name
    string name = get_string("What is your name ?\n");

    //Printing hello with the entered name by the user
    printf("Hello, %s!\n", name);
    
    return 0;

}