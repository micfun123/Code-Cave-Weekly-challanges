#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height; //get user input
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int line = 0; line < height; line++)
    {

        for (int space = height - 1; space > line; space = space - 1)   //prints spaces
        {
            printf(" ");
        }

        for (int hash = - 1; hash < line; hash++)   //prints hashes
        {

            printf("#");
        }

        printf("\n"); //new line
    }
}